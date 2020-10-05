from flask import Flask, request, redirect

from config import *
from setup import *

app = Flask(__name__, static_folder='build', static_url_path='/')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.before_request
def force_https():
    if not request.is_secure:
        return redirect(request.url.replace('http://', 'https://'))


initialize_api_routes(app)

if __name__ == '__main__':
    print('app run start')

    parsed_config = get_parsed_config()
    app.run(debug=parsed_config.get('Debug', False),
            use_reloader=parsed_config.get('UseReloader', False))
    print('app run end')
