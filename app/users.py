from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_db

from sqlalchemy.sql import select


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/list')
async def show_users_list():
    return render_template('list.html')
