# Generated by Django 3.2.6 on 2023-12-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_etudiant',
            field=models.BooleanField(default=True),
        ),
    ]
