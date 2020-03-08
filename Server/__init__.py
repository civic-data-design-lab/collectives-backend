from flask import Flask
import os

project_root = os.path.dirname(__file__)
template_path = os.path.abspath(os.path.join(project_root, '..', 'templates'))

app = Flask(__name__, template_folder=template_path)
