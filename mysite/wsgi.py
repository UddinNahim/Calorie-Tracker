import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # <- import whitenoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='/path/to/static')  # optional
