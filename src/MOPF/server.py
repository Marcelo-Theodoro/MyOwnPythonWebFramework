#! /usr/bin/env python3

# Development server.
# Use: python3 server.py

from werkzeug.serving import run_simple
from main import app

# Change the variables bellow as you want.
HOST = 'localhost'
PORT = 8080
RELOADER = True
DEBUGGER = True
APP = app

run_simple(HOST, PORT, APP, use_reloader=RELOADER, use_debugger=DEBUGGER)
