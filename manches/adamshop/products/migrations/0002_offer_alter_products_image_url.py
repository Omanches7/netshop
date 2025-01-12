# Generated by Django 5.0.6 on 2024-06-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('discount', models.FloatField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='image_url',
            field=models.CharField(max_length=2101),
        ),
    ]
