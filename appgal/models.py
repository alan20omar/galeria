from django.db import models, migrations
from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.operations import HStoreExtension, UnaccentExtension

# Create your models here.

class Migration(migrations.Migration):
    operations = [
        HStoreExtension(),
        UnaccentExtension(),
    ]

class Galeria(models.Model):
    image = models.ImageField(upload_to="toGaleria")
    name = models.CharField(max_length=50)