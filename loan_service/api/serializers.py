from rest_framework import serializers
from loan_service.api.models import LoanRequest


class LoanRequestSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['name', 'cpf', 'birthdate', 'amount', 'terms', 'income']

    def validate_terms(self, terms):
        if terms not in (6, 9, 12):
            raise serializers.ValidationError("Valores disponíveis: 6, 9 ou 12")
        return terms

    def validate_amount(self, amount):
        if amount < 1000 or amount > 4000:
            raise serializers.ValidationError('O valor deve ser entre 1000,00 e 4000,00')
        return amount


class LoanRequestSerializerReturn(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['uuid']
