from django.urls import path, conf
from rest_framework.routers import DefaultRouter
from core.views import CategoryViewSet, ProductImageViewSet, ProductViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("product-images", ProductImageViewSet, basename="cities")
router.register("products", ProductViewSet, basename="products")


urlpatterns = [
    path("", conf.include(router.urls)),
]
