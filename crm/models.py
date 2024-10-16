from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.

class Venda(models.Model):
    loja = models.ForeignKey('Loja',
                             on_delete=models.CASCADE,
                            )
    data = models.DateField()
    vendedor = models.ForeignKey('Vendedor',
                                 on_delete=models.CASCADE,
                                 )
    produto = models.ForeignKey('Produto',
                                 on_delete=models.CASCADE,
                                 )
    quantidade = models.IntegerField(validators = [MinValueValidator(1)])
    
    cliente = models.ForeignKey('Cliente',
                                 on_delete=models.CASCADE,
                                 )

class Loja(models.Model):
    pass 

class Vendedor(models.Model):
    pass

class Produto(models.Model):
    pass

class Cliente(models.Model):
    pass