from rest_framework import viewsets
from rest_framework.response import Response
from core.serializer import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
    LimitedProductSerializer,
)
from core.models import Category, Product, ProductImage
from core.decoratos import user_is_approved


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name", "status", "category__name"]

    def get_serializer_class(self):
        if not self.request.user.is_authenticated or not self.request.user.is_approved:
            return LimitedProductSerializer
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        user = self.request.user
        if user.is_superuser or user.is_authenticated and user.is_approved:
            for product_data in serializer.data:
                product = Product.objects.get(id=product_data["id"])
                images = []
                for image in product.images.all():
                    images.append(
                        {
                            "id": image.id,
                            "product": image.product.id,
                            "image": request.build_absolute_uri(image.image.url),
                        }
                    )
                product_data["product_images"] = images
        return Response(serializer.data)

    @user_is_approved
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @user_is_approved
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
