# Generated by Django 3.2 on 2021-05-01 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added'], 'verbose_name_plural': 'comments'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='pizza',
        ),
    ]
