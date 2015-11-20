from geokey.extensions.base import register

VERSION = (0, 0, 0)
__version__ = '.'.join(map(str, VERSION))

register(
    'geokey_checklist',
    'Checklist',
    display_admin=True,
    superuser=False
)
