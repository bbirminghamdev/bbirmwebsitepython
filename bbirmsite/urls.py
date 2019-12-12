# from django.conf.urls import url
# from django.urls import path, include
#
# from rest_framework import routers
# from .views import CustViewSet, HomePageView, LinksPageView, Customers, CalcTest
#
#
# router = routers.DefaultRouter()
# router.register(r'customers', CustViewSet)
#
# urlpatterns = [
#      url(r'^$', HomePageView.as_view()),
#      url(r'^links/$', LinksPageView.as_view()),  # simple view
#      url(r'^getcust/$', Customers.getCust),  # simple view
#      url(r'^apitest/$', CalcTest),  # for REST API test
# ]

from django.conf.urls import url

from .api import YearApi, TaxBracketApi, TaxCreditApi, EIRateApi, CPPRateApi

urlpatterns = [
    url(r'^years$', YearApi.as_view()),
    url(r'^tax_brackets', TaxBracketApi.as_view()),
    url(r'^tax_credits$', TaxCreditApi.as_view()),
    url(r'^ei_rates$', EIRateApi.as_view()),
    url(r'^cpp_rates$', CPPRateApi.as_view())
]
