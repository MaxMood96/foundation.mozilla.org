# Generated by Django 2.2.17 on 2021-02-26 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0036_articlepage_article_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_de',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_en',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_es',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_fr',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_fy_NL',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_nl',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_pl',
        ),
        migrations.RemoveField(
            model_name='productpage',
            name='user_friendly_privacy_policy_helptext_pt',
        ),
    ]