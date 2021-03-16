# Generated by Django 2.2.17 on 2021-02-08 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('buyersguide', '0009_auto_20210127_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Locale'),
        ),
        migrations.AddField(
            model_name='buyersguideproductcategory',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Locale'),
        ),
        migrations.AddField(
            model_name='productprivacypolicylink',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='locale',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Locale'),
        ),
        migrations.AddField(
            model_name='update',
            name='translation_key',
            field=models.UUIDField(editable=False, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='buyersguideproductcategory',
            unique_together={('translation_key', 'locale')},
        ),
        migrations.AlterUniqueTogether(
            name='productprivacypolicylink',
            unique_together={('translation_key', 'locale')},
        ),
        migrations.AlterUniqueTogether(
            name='update',
            unique_together={('translation_key', 'locale')},
        ),
    ]