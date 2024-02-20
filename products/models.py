from django.db import models

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"
class ProductModel(models.Model):
    product_title = models.CharField(max_length=40)
    product_price = models.FloatField()
    product_description = models.TextField()
    product_amount = models.IntegerField()
    product_image = models.FileField(upload_to='product_images')
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
