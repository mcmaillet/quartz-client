def route(app):
    if app is None:
        raise Exception('No app to attach')

    from . import createfile

    createfile.route(app)
