# Generated by Django 3.2 on 2021-07-09 17:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_departamento_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bono', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('fechaBono', models.DateField()),
                ('motivo', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='departamento',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.AddField(
            model_name='bono',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usuario'),
        ),
    ]
