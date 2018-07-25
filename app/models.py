# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    shipping_time = models.CharField(max_length=1000, blank=True, null=True)
    urlh = models.CharField(unique=True, max_length=60, blank=True, null=True)
    crawl_time = models.DateTimeField(blank=True, null=True)
    crawl_date = models.DateField(blank=True, null=True)
    mrp = models.FloatField(blank=True, null=True)
    available_price = models.FloatField(blank=True, null=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    source = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    subcategory = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    stock = models.CharField(max_length=50, blank=True, null=True)
    variant = models.CharField(max_length=1000, blank=True, null=True)
    offers = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=1000, blank=True, null=True)
    sku = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    price_change = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    timestamp = models.DateTimeField()
    brand = models.CharField(max_length=200, blank=True, null=True)
    cashback = models.CharField(max_length=1000, blank=True, null=True)
    shipping_charges = models.CharField(max_length=1000, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    warranty = models.CharField(max_length=500, blank=True, null=True)
    seller = models.CharField(max_length=500, blank=True, null=True)
    others = models.TextField(blank=True, null=True)
    meta = models.CharField(max_length=1500, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'products'
