import asyncio
import os
import sqlite3

import asyncpg

import click
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy.ext.asyncio import create_async_engine


async def get_db():
    if 'db' not in g:
        g.db = await asyncpg.connect(current_app.config['DATABASE_CONNECTION_STRING'])
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        asyncio.run(db.close())


async def init_db():
    db = await get_db()

    with current_app.open_resource('scheme.sql') as f:
        await db.execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():

    """Clear the existing data and create new tables."""
    asyncio.run(init_db())
    click.echo('Initialized the database.')


async def seed_async():
    db = await get_db()
    with current_app.open_resource('seeds\\privileges.sql') as f:
        await db.execute(f.read().decode('utf8'))

    with current_app.open_resource('seeds\\users.sql') as f:
        await db.execute(f.read().decode('utf8'))


@click.command('seed')
@with_appcontext
def seed():
    asyncio.run(seed_async())


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed)
