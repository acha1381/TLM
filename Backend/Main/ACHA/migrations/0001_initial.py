# Generated by Django 5.0.3 on 2024-05-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('content', models.TextField()),
            ],
        ),
    ]