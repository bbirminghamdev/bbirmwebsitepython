from django.contrib import admin

# Register your models here.

from .models import Year, TaxBracket, TaxCredit, EIRate, CPPRate

admin.site.register(Year)
admin.site.register(TaxBracket)
admin.site.register(TaxCredit)
admin.site.register(EIRate)
admin.site.register(CPPRate)
