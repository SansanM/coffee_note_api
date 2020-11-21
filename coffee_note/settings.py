from .settings_common import *

DEBUG = False

ALLOWED_HOSTS = ["coffeenoteapi.sankawa.site"]

CORS_ORIGIN_WHITELIST = [
    "https://coffeenote.sankawa.site"
]
DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': BASE_DIR / 'db.sqlite3',
   # }
   'default': {
   'ENGINE': 'django.db.backends.mysql',
   'NAME': 'coffee_note',
   'USER': 'root',
   "PASSWORD": 'gak654jdsafl546',
   'POST': 3306,
   'OPTIONS': {
                'charset': 'utf8mb4',
              },
   }
}