# Generated by Django 5.0.3 on 2024-04-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_activationkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationkey',
            name='key',
            field=models.CharField(default='a49bf5dcf5ab48d68e6cd4ba402c6728', max_length=32),
        ),
    ]
