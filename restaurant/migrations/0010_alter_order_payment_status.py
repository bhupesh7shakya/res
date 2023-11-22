# Generated by Django 4.2.6 on 2023-11-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('C', 'Completed'), ('P', 'Pending')], default='P', max_length=1),
        ),
    ]
