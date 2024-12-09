
from django.db import migrations
from crm.models import Loja, Cliente, Produto

def create_lojas(apps, schema_editor):
    nomes=['Loja 01', 'Loja 02', 'Loja 03',]
    for nome in nomes:
        Loja.objects.create(
            nome=nome,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]