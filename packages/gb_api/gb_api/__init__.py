from gb_api.api import config


with open(config.ROOT_PATH / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
