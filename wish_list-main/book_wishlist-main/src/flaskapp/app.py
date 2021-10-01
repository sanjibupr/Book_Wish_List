#!/usr/bin/env python
"""
An extremely simple app to demo how to deploy to kubernetes
"""

import logging
import os
import sys

import json_logging
import psycopg2
import yaml
from flask import Flask

from .api import views
from .extensions import db

# Disable startup banner
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None



def setup_logging(APP_NAME, app):
    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(sys.stdout))


class Config(object):
    """Maps environment variables and other runtime configurations into code"""
    APP_NAME = 'book_wish_list_app'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SQLALCHEMY_DATABASE_URI="postgres://postgres@postgres:5432/zonar"
    ENV = os.environ.get('ENVIRONMENT_NAME', None)

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:@localhost/zonar_test"

def create_app(config_object=Config):

    app = Flask(config_object.APP_NAME)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    setup_logging(app.config['APP_NAME'], app)
    # verify db is up
    try:
        conn = psycopg2.connect(dsn=app.config['SQLALCHEMY_DATABASE_URI'])
    except psycopg2.OperationalError as e:
        # bail if it isn't
        print(e)
        sys.exit(-1)
    conn.close()
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.main_blueprint)
    return None
