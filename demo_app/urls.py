from django.urls import re_path
from demo_app import api, views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'demo_app'

apipatterns = [
    re_path(r'^test/$', api.TestView.as_view(), name='api_test')
]

urlpatterns = [
    re_path(r'^$', views.TestView.as_view(), name='test')
]

urlpatterns += format_suffix_patterns(apipatterns)
