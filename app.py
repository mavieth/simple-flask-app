from flask import Flask
from flask_script import Manager

from blueprints import simple_page

app = Flask(__name__)
# configure your app
app.register_blueprint(simple_page)
# end configure

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
