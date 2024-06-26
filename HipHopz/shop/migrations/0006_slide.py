# Generated by Django 5.0 on 2024-03-22 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/slide')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.sub_category')),
            ],
        ),
    ]
