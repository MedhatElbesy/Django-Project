# Generated by Django 5.0.3 on 2024-04-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_activationkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationkey',
            name='key',
            field=models.CharField(default='58e6158c7dc649d2bb09d3e618a8a748', max_length=32),
        ),
    ]
