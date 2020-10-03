import configparser

from flask import Flask

from config import *
from setup import *

config = configparser.ConfigParser()
config.read(ENVIRONMENT)

default_config = config['DEFAULT']
default_config.get('CreateFileURL', None)

app = Flask(__name__, static_folder='build', static_url_path='/')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


initialize_api_routes(app)

if __name__ == '__main__':
    print('app run start')
    app.run(debug=default_config.getboolean('Debug'),
            use_reloader=default_config.getboolean('UseReloader'))
    print('app run end')
