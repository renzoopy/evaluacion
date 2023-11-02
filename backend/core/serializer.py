from rest_framework import serializers
from core.models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

    def validate_name(self, value):
        if not self.instance and Category.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "There is already a category with that name."
            )
        return value


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "product", "image")


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.FileField(
            max_length=1000000, allow_empty_file=False, use_url=False
        ),
        write_only=True,
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "status",
            "category",
            "product_images",
            "uploaded_images",
        )

    def validate_name(self, value):
        if not self.instance and Product.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "A product with this name already exists."
            )
        return value

    def create(self, validated_data):
        uploaded_data = validated_data.pop("uploaded_images")
        if len(uploaded_data) > 10:
            raise serializers.ValidationError("Only up to 10 images may be uploaded.")

        product = Product.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            ProductImage.objects.create(product=product, image=uploaded_item)
        return product


class LimitedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "status")
