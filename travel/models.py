from django.db import models
from django.utils.translation import gettext_lazy as _


class Destination(models.Model):
    prod_img = models.ImageField('Product Image', upload_to='destination', null=True, blank=True)
    description = models.TextField(max_length = 1000)
    title = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "destination"
        

class TourPackage(models.Model):
    class choices(models.TextChoices):
         Ethnography = 'Ethnography', _('Ethnography')
         Photography = 'Photography', _('Photography')
         History = 'History', _('History')
         Bird_Watching = 'Bird Watching', _('Bird Watching')
         Hiking = 'Hiking', _('Hiking')
         Sight_Seeing = 'Sight Seeing', _('Sight Seeing')
         Cultural = 'Cultural', _('Cultural')
    
    t_type =  models.CharField(max_length=20,choices=choices.choices)
    prod_img = models.ImageField('Product Image', upload_to='tour_package', null=True, blank=True)
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 1000)
    price = models.FloatField()
    x =  models.FloatField()
    y = models.FloatField()
    
    class Meta:
      db_table = "tour_package"


class Highlights(models.Model):
    prod_img = models.ImageField('Product Image', upload_to='highlights', null=True, blank=True)
    description = models.TextField(max_length = 1000)
    title = models.CharField(max_length = 50)
    price = models.FloatField()
    
    class Meta:
        db_table = "highlights"


class TourExpiriance(models.Model):
    class choices(models.TextChoices):
         History = 'History', _('History')
         Myth_Reality = 'Myth or Reality', _('Myth or Reality')
         Travel_Stories = 'Travel Stories', _('Travel Stories')
         Traditions = 'Traditions', _('Traditions')
    
    t_type =  models.CharField(max_length=20,choices=choices.choices)
    prod_img = models.ImageField('Product Image', upload_to='tour_expiriance', null=True, blank=True)
    description = models.TextField(max_length = 1000)
    title = models.CharField(max_length = 50)
    price = models.FloatField()
    
    class Meta:
        db_table = "tour_expiriance"


class Testimonials(models.Model):
    description = models.TextField(max_length = 1000)
    name = models.CharField(max_length = 50)
    position = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "testimonials"


class BlogVlog(models.Model):
    prod_img = models.ImageField('Product Image', upload_to='blog_vlog', null=True, blank=True)
    description = models.TextField(max_length = 1000)
    title = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "blog_vlog"