# Generated by Django 4.1.2 on 2022-10-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='categoria',
        ),
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.ManyToManyField(to='core.categoria', verbose_name='Categpría'),
        ),
    ]
