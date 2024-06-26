import os
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

app.secret_key = os.getenv("APP_SECRET_KEY")
