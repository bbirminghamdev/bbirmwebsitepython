from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from .serializers import YearSerializer, TaxBracketSerializer, TaxCreditSerializer, EIRateSerializer, CPPRateSerializer
from .models import Year, TaxBracket, TaxCredit, EIRate, CPPRate


class YearApi(ListAPIView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class TaxBracketApi(ListCreateAPIView):
    queryset = TaxBracket.objects.all()
    serializer_class = TaxBracketSerializer

    def get_queryset(self):
        return TaxBracket.objects.all()


class TaxCreditApi(ListAPIView):
    queryset = TaxCredit.objects.all()
    serializer_class = TaxCreditSerializer


class EIRateApi(ListAPIView):
    queryset = EIRate.objects.all()
    serializer_class = EIRateSerializer


class CPPRateApi(ListAPIView):
    queryset = CPPRate.objects.all()
    serializer_class = CPPRateSerializer