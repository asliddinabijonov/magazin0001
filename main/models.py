from django.db import models

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

# Testimonial Model
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['name']

# Slider Model
class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"
        ordering = ['title']

# Why Shop With Us Model
class WhyShop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Storing font-awesome class names

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Why Shop With Us"
        verbose_name_plural = "Why Shop With Us"
        ordering = ['title']

# Gift Model
class Gift(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gifts/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"
        ordering = ['title']

# Saving Section Model
class Saving(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='savings/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Saving"
        verbose_name_plural = "Savings"
        ordering = ['title']
