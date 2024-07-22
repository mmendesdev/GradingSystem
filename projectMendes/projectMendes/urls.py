from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path

# from notas.views import home    #caminho para minha template

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("notas.urls")),
    path("api-auth/", include("rest_framework.urls")),
    # path("", home, name="home"),  # ccaminho para minha template
    path("", lambda request: HttpResponseRedirect("/admin/")),
]
