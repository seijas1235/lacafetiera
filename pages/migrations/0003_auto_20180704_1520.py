# Generated by Django 2.0.2 on 2018-07-04 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
    ]