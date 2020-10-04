def route(app):
    @app.route('/api/createfile', methods=['POST'])
    def createfile_post():
        import requests
        from flask import jsonify, request
        from util.config_reader import ConfigReader
        config_reader = ConfigReader()
        if 'selectedDate' not in request.json.keys():
            return jsonify(
                {'message': "Bad request. Date + time required."})

        url = config_reader.get('CreateFileURL')

        if url is None:
            return jsonify({
                'message': "Client not configured. Missing URL."})
        try:
            requests.post(url,
                          json={
                              "message": request.json.get('message', "This is a default message"),
                              "selectedDate": request.json['selectedDate']
                          })
        except Exception:
            print(f"Bad request to '{url}'.", request.json)
            return jsonify({
                'message': "Your request was unsuccessful."})
        return jsonify({
            'message': f"Your request to create a file at '{request.json['selectedDate']}' was dispatched."})
