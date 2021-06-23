# Generated by Django 3.2 on 2021-05-27 16:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_presupuesto_valor_presupuesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='valor_gasto',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='fecha_presupuesto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='valor_presupuesto',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]