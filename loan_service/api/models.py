import uuid
from django.db import models


class LoanRequest(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    birthdate = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    terms = models.IntegerField()
    income = models.DecimalField(max_digits=7, decimal_places=2)
