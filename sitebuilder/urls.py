from django.conf.urls import url
from .views import page

urlpatterns = (
    # Slugs delimited with hyphens
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    # Starts and ends with nothing
    url(r'^$', page, name='homepage')
)
