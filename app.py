from flask import Flask

from setup import *

app = Flask(__name__, static_folder='build', static_url_path='/')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


initialize_api_routes(app)

if __name__ == '__main__':
    print('app run start')
    from util.config_reader import ConfigReader

    config_reader = ConfigReader()
    app.run(debug=config_reader.get_boolean('Debug'),
            use_reloader=config_reader.get_boolean('UseReloader'))
    print('app run end')
