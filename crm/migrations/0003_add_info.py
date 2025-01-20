
from django.db import migrations
from crm.models import Loja, Cliente, Produto

def create_infos(apps, schema_editor):
    for info in range(1,4):
        Loja.objects.create(
            nome=f'Loja 0{info}',
            )
        Cliente.objects.create(
            nome=f'Cliente 0{info}',
            numero_fiscal=f'0000000000{info}',
            )
        Produto.objects.create(
            nome=f'Produto 0{info}',
            valor_unitario=float(info),
        )

class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_add_new_user'),
    ]

    operations = [
        migrations.RunPython(create_infos),
    ]