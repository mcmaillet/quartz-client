def route(app):
    @app.route('/api/createfile', methods=['POST'])
    def createfile_post():
        from flask import jsonify, request
        return jsonify({'message': f"Your request to create a file at '{request.json['selectedDate']}' was dispatched."})
