# Generated by Django 5.1.4 on 2024-12-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_baseint_baseintmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseintmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
