# Generated by Django 3.1.7 on 2021-12-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210829_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default/article.jpg', upload_to='articles'),
        ),
    ]
