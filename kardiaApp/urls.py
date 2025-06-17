from rest_framework import routers
from django.urls import path, include
from .views import ZettelCardViewSet, CustomFieldViewSet, CustomFieldValueViewSet

router = routers.DefaultRouter()
router.register(r'cards', ZettelCardViewSet)
router.register(r'fields', CustomFieldViewSet)
router.register(r'values', CustomFieldValueViewSet)

urlpatterns = router.urls  # don't wrap this in `path()` again
