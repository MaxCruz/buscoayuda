from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('polls.urls', namespace="principal")),
    url(r'^admin/', admin.site.urls),
]
