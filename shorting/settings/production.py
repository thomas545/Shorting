from .development import *

DEBUG = False

ALLOWED_HOSTS = ["cuturls.live", "www.cuturls.live"]

STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / "statics"]