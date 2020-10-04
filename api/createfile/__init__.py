from config import *


def route(app):
    @app.route('/api/createfile', methods=['POST'])
    def createfile_post():
        import requests
        from flask import jsonify, request
        parsed_config = get_parsed_config()
        if 'selectedDate' not in request.json.keys():
            return jsonify(
                {'message': "Bad request. Date + time required."})

        url = parsed_config.get('CreateFileURL', None)

        if url is None:
            return jsonify({
                'message': "Client not configured. Missing URL."})
        try:
            requests.post(url,
                          json={
                              "message": request.json.get('message', "This is a default message"),
                              "scheduledFor": request.json['selectedDate']
                          })
        except Exception:
            print(f"Bad request to '{url}'.", request.json)
            return jsonify({
                'message': "Your request was unsuccessful."})
        return jsonify({
            'message': f"Your request to create a file at '{request.json['selectedDate']}' was dispatched."})
