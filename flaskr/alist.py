import concurrent
import functools
import time
import json
from flask import jsonify

from collections import OrderedDict
import aiofiles
import requests
import threading
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from sqlalchemy.sql import select


bp = Blueprint('alist', __name__, url_prefix='/sources')

thread_local = threading.local()
resp = []

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


@bp.route('/first')
async def first():
    async with aiofiles.open('sources/first-source.json', mode='r') as f:
        contents = await f.read()
    return contents


@bp.route('/second')
async def second():
    async with aiofiles.open('sources/second-source.json', mode='r') as f:
        contents = await f.read()
    return contents


@bp.route('/third')
async def third():
    async with aiofiles.open('sources/third-source.json', mode='r') as f:
        contents = await f.read()
    return contents


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def get_content_from_source(url):
    session = get_session()
    with session.get(url) as response:
        resp.extend(json.loads(response.content))


def get_content_from_sources(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_content_from_source, urls)



@bp.route('/list')
async def list():
    sources = [
        "http://localhost:5000/sources/first",
        "http://localhost:5000/sources/second",
        "http://localhost:5000/sources/third",
    ]
    get_content_from_sources(sources)
    return str(resp)
    list = {}
    k = 0
    for i in range(0, len(resp), 10):
        index = resp[k]["id"] // 10
        t = resp[k:k + 10]
        list[index] = t
        k += 10

    s = []
    for i in sorted(list.keys()):
        s.extend(list[i])
    return jsonify(s)

