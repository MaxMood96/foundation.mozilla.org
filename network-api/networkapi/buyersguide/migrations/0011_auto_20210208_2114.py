# Generated by Django 2.2.17 on 2021-02-08 21:11

from django.db import migrations
from wagtail.core.models import BootstrapTranslatableModel


class Migration(migrations.Migration):
    dependencies = [
        ('buyersguide', '0010_auto_20210208_2111'),
    ]

    # Add one operation for each model to bootstrap here
    # Note: Only include models that are in the same app!
    operations = [
        BootstrapTranslatableModel('buyersguide.BuyersGuideProductCategory'),
        BootstrapTranslatableModel('buyersguide.ProductPrivacyPolicyLink'),
        BootstrapTranslatableModel('buyersguide.Update'),
    ]