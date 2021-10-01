# -*- coding: utf-8 -*-
"""Create an application instance."""
from flaskapp.app import create_app, Config

app = create_app(Config)
