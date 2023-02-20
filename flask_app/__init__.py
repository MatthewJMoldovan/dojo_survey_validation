from flask import Flask, flash

app = Flask(__name__)


DATABASE = "dojo_survery_db"

app.secret_key = "password"