# Generated by Django 4.2.6 on 2023-11-20 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_orderitem_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
            preserve_default=False,
        ),
    ]
