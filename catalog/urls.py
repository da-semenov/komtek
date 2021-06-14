from rest_framework import routers

from .views import CatalogViewSet, ElementViewSet, ValidateViewSet

router = routers.DefaultRouter()
router.register(r'catalogs', CatalogViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'validate', ValidateViewSet)
urlpatterns = router.urls
