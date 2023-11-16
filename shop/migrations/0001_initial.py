# Generated by Django 4.2.5 on 2023-11-09 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('left', models.CharField(choices=[('min', 'Осталось мало'), ('max', 'Осталось много'), ('mid', 'Осталось достаточно')], default='min', max_length=10)),
                ('info', models.TextField()),
                ('cover', models.ImageField(blank=True, upload_to='product_cover')),
                ('on_site', models.BooleanField(default=False)),
                ('sale', models.FloatField()),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.maker')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.type')),
            ],
        ),
    ]