# Generated by Django 4.0.2 on 2022-03-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iepheme_app', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['alphabetic_order'], 'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.AddField(
            model_name='category',
            name='alphabetic_order',
            field=models.CharField(default='a-', help_text='ordre dans lequel les videos vont apparaitre "a-1"', max_length=200, verbose_name='Ordre alphabétique'),
        ),
    ]
