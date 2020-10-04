def get_parsed_config():
    import configparser

    config = configparser.ConfigParser()
    config.read('env.ini')

    default_config = config['DEFAULT']
    if len(default_config.items()) == 0:
        import os
        return {
            k: v
            for k, v in os.environ.items()
        }

    return default_config
