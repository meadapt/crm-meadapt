# Generated by Django 5.1.1 on 2024-10-17 21:27

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('numero_fiscal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor_unitario', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('quantidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.cliente')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.loja')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.produto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.vendedor')),
            ],
        ),
    ]
