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
    def __str__(self):
        return f'{self.loja} - {self.vendedor} - {self.produto}'

class Loja(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome}'

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor_unitario = models.FloatField(validators = [MinValueValidator(0.01)])

    def __str__(self):
        return f'{self.nome}'

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    numero_fiscal = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'