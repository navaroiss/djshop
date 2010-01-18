from django.db import models
from django.conf import settings

class Category(models.Model):
    catname = models.CharField(max_length=255, verbose_name="Category name")
    catparent = models.ForeignKey('self', default=0, blank=True, null=True, related_name='child_set',
                                  verbose_name="Parent")
    def __unicode__(self):
        return '%s' % (self.catname)
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    proname = models.CharField(max_length=255, verbose_name="Product name")
    prodesc = models.TextField(verbose_name="Product description")
    procolor = models.CharField(max_length=255, verbose_name="Product color")
    proprice = models.IntegerField(max_length=11, verbose_name="Product price(USD)")
    profeatured = models.BooleanField(default=False, verbose_name="Product featured")
    prorelevant = models.CharField(max_length=255, blank=True, verbose_name="Product relevant")
    procat = models.ForeignKey(Category, verbose_name="Product category")
    
    proimg = models.ImageField(upload_to='images', verbose_name="Product image")
    
    def __unicode__(self):
        return '%s' % (self.proname)
    
    class Meta:
        verbose_name_plural = "Products"

class Image(models.Model):
    imgname = models.ImageField(upload_to='images')
    imgpro = models.ForeignKey(Product, verbose_name="Image of product")
    
    def __unicode__(self):
        return 'Product %d : %s' % (self.imgpro.id, self.imgname)
