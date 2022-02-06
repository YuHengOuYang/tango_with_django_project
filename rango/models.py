from django.db import models
from django.template.defaultfilters import slugify

# Create your models here. model其实就是ERD里面的entity
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views=models.IntegerField(default=0)
    likes=models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#因为指定的是外键所以不用说type
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    #变量名= 左边是fields 右边是types
    def __str__(self):
        return self.title