# Generated by Django 5.0.6 on 2024-07-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_product_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user', models.CharField(max_length=40)),
                ('recipient', models.CharField(max_length=40)),
            ],
        ),
    ]