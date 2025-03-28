import os
from dotenv import load_dotenv

from flask import Flask, session, render_template, redirect, url_for
from flask_login import LoginManager, login_required
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from . import create_app
from src.accounts.models import Account
from src.accounts.urls import accounts
from src.accounts.controllers import limiter

# ----------------------------------------------- #

# Load .env value from parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

app = create_app(os.getenv("CONFIG_MODE", "default"))
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")

# ----------------------------------------------- #

#app init

limiter.init_app(app)
csrf = CSRFProtect(app)

app.register_blueprint(accounts, url_prefix='/accounts', template_folder='views')

# ----------------------------------------------- #

login_manager = LoginManager()
login_manager.login_view = "accounts.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id)) if user_id.isdigit() else None

# ----------------------------------------------- #

@login_required
@app.route('/')
def root():
    return redirect(url_for('home'))

# ----------------------------------------------- #

@login_required
@app.route('/home')
def home():
    return render_template('home.html', username=session['username']) if 'loggedin' in session else redirect(url_for('accounts.login'))