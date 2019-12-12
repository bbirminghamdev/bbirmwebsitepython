from rest_framework import serializers

from .models import Year, TaxBracket, TaxCredit, EIRate, CPPRate


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class TaxBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxBracket
        fields = '__all__'


class TaxCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCredit
        fields = '__all__'


class EIRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EIRate
        fields = '__all__'


class CPPRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPPRate
        fields = '__all__'
