import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

from sqlalchemy.sql import select


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
async def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = await get_db()
        error = None
        user = await db.fetchrow(
        'SELECT * FROM users WHERE name = $1', username)
        if user is None:
            error = 'Неправильное имя пользователя.'
        elif not check_password_hash(user['password'], password):
            error = 'Неправильный пароль.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return "auth"

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
async def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = await get_db().fetchrow(
        'SELECT * FROM users WHERE name = $1', user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view