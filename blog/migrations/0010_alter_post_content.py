# Generated by Django 3.2.19 on 2023-05-18 14:55

import ckeditor.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(validators=[django.core.validators.MaxLengthValidator(5000)]),
        ),
    ]
