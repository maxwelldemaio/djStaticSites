import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)


settings.configure(
    DEBUG=True,
    SECRET_KEY=os.urandom(32),
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
    # Directory where all our prototype templates will live
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    # Where our complete HTML files will be generated
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    # Enable static content to live inside the build directory
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
