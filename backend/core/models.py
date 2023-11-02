from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Represents a product category."""

    name = models.CharField(verbose_name=_("Name"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """Represents a product in the API."""

    ACTIVE = 1
    INACTIVE = 2
    STATUS_CHOICES = (
        (ACTIVE, "Activo"),
        (INACTIVE, "Inactivo"),
    )

    name = models.CharField(verbose_name=_("Name"), max_length=60)
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Status"), choices=STATUS_CHOICES
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="products",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.name}"


class ProductImage(models.Model):
    """Represents the image of a product."""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.product.name}"
