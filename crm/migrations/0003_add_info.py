
from django.db import migrations
from crm.models import Loja, Cliente, Produto

def create_lojas(apps, schema_editor):
    nomes=['Loja 01', 'Loja 02', 'Loja 03',]
    for nome in nomes:
        Loja.objects.create(
            nome=nome,
            )

def create_cliente(apps, schema_editor):
    for cliente in range(1,4):
        Cliente.objects.create(
            nome=f'Cliente 0{cliente}',
            numero_fiscal=f'0000000000{cliente}',
        )


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_lojas),
        migrations.RunPython(create_cliente)
    ]