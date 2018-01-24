from django.conf.urls import url
from vector_style import views

urlpatterns = [
    url(r'^datalayer/(?P<datalayer>\d+)/styles/$', views.get_datalayer_styles),
    url(r'^datalayer/(?P<datalayer>\d+)/styles/(?P<style>\d+)/$', views.get_datalayer_style)
]
