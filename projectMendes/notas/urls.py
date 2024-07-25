from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoriaViewSet, NotaViewSet

router = DefaultRouter()
router.register(r"notas", NotaViewSet)

"nome-do-modelo - list", "nota/"
"nome-do-modelo - detail", "nota/{id}"
router.register(r"categorias", CategoriaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
