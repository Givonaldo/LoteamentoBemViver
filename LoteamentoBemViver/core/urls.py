from django.conf.urls import url
from LoteamentoBemViver.core.views import *

app_name = 'core'

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),


]