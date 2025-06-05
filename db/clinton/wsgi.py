import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings  # ✅ Correct import
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinton.settings')

application = get_wsgi_application()
app = WhiteNoise(application, root=os.path.join(
    settings.BASE_DIR, 'staticfiles'))


