# Generated by Django 5.1.6 on 2025-06-24 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ei', '0008_details1_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table1',
            old_name='district',
            new_name='place',
        ),
    ]
