from flask import Flask
import os, config

app = Flask(__name__)
app.config.from_object('config.DevelopementConfig')

from app import routes
