from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.conf import settings
from accounts.models import Account

class CustomProduct(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)  # Add slug field
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    custom_text = models.CharField(max_length=200, blank=True, null=True)  # Field for custom text
    custom_logo = models.ImageField(upload_to='photos/logos/', blank=True, null=True)  # Field for custom logo
    images = models.ImageField(upload_to='photos/custom_products')
    images_hover = models.ImageField(upload_to='photos/custom_products_hover')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate slug before saving
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('custom_product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name


class VariationManager_Custom(models.Manager):
    def colors(self):
        return super(VariationManager_Custom, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager_Custom, self).filter(variation_category='size', is_active=True)


variation_category_choise_Custom = (
        ('color', 'color'),
        ('size', 'size'),
    )


class Variation_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choise_Custom)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)

    objects = VariationManager_Custom()

    def __str__(self):
        return self.variation_value



class ProductGallery_Custom(models.Model):
    product = models.ForeignKey(CustomProduct, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/custom_products/', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'


class Cart_Custom(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id



class CartItem_Custom(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    custom_product = models.ForeignKey(CustomProduct, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation_Custom, blank=True)
    cart = models.ForeignKey(Cart_Custom, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.custom_product)