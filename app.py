from flask import Flask, render_template
from config import Configuration
from accounts.blueprint import users


app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(users, url_prefix='/')

if __name__ == '__main__':
    app.run()
