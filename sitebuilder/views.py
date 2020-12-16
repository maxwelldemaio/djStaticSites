import json
import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader_tags import BlockNode
from django.utils._os import safe_join

# Function to grab our template for the requested static content
def get_page_or_404(name):
    """ Return page content as a Django template or raise 404 error """
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        # Get HTML content 
        page = Template(f.read())

    return page

def page(request, slug='index'):
    # TODO: learn what slugs are in Django
    """ Render the requested page if found """
    