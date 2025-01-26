from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*.onrender.com']


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

DATABASES['default']['CONN_MAX_AGE'] = 600  # 10 minutes

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT', '5432'),
#     }
# }


# Security settings
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


""" if needed here are AWS settings for using S3 to store static and more importantly media files """
# # AWS settings

# AWS_STORAGE_BUCKET_NAME = 's3bucketname'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_FILE_OVERWRITE = False


# STORAGES = {
#     # Media files(images)management
#     "default": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     }, 

#     # Static files(CSS, JavaScript) management
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
#     },

# }

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

