# Generated by Django 3.0.8 on 2020-08-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200804_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canciones',
            name='artista',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='canciones',
            name='autor',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='canciones',
            name='cancion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='canciones',
            name='titulo',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='canciones',
            name='url',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
