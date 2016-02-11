#! /usr/bin/env python3
from werkzeug.serving import run_simple
from main import app

HOST = 'localhost'
PORT = 8080
APP = app

run_simple(HOST, PORT, APP, use_reloader=True, use_debugger=True)
