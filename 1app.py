import bigcommerce
from flask import Flask

app = Flask(__name__)

app.config['APP_URL'] = 'https://aviorsalestax.herokuapp.com/'
app.config['APP_CLIENT_ID'] = 'bz7n5kiqlallwmyoaabgta5nm0wv4dm'
app.config['APP_CLIENT_SECRET'] = '03b1001757b002d0c4ccd46ff335eb8df26b645731176e1a32651980a2cde3f6'
app.config['SESSION_SECRET'] = os.urandom(64)





@app.route("/auth")
def auth():

    return "login"

@app.route("/")
def index():
    return "Hello World!"