from django.db import models

# Create your models here.


class Year (models.Model):
    name = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return f'Tax Year: year:{self.name} '


class TaxBracket(models.Model):
    federal = 'F'
    provincial = 'P'
    municipal = 'M'
    gov_type_choices = [(federal, "Federal"), (provincial, "Provincial"), (municipal, "Municipal")]

    startAmount = models.DecimalField(decimal_places=4, max_digits=10)
    endAmount = models.DecimalField(decimal_places=4, max_digits=10)
    percentage = models.DecimalField(decimal_places=4, max_digits=10)
    gov_type = models.CharField(max_length=1, choices=gov_type_choices, default=federal)
    year = models.ForeignKey(Year, related_name="%(class)s_name", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Tax Bracket: start:{self.startAmount} end:{self.endAmount} pct:{self.percentage} ' \
               f'gov:{self.gov_type} year:{self.year.name}'


class CPPRate(models.Model):
    exemption = models.DecimalField(decimal_places=4, max_digits=10)
    rate = models.DecimalField(decimal_places=4, max_digits=10)
    maxPerYear = models.DecimalField(decimal_places=4, max_digits=10)
    year = models.ForeignKey(Year, related_name="%(class)s_name", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'CPP Rate: exemption:{self.exemption} rate:{self.rate} maxPerYear:{self.maxPerYear} ' \
               f'year:{self.year.name}'


class EIRate(models.Model):
    rate = models.DecimalField(decimal_places=4, max_digits=10)
    maxPerYear = models.DecimalField(decimal_places=4, max_digits=10)
    year = models.ForeignKey(Year, related_name="%(class)s_name", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'EI Rate: rate:{self.rate} maxPerYear:{self.maxPerYear} year:{self.year.name}'


class TaxCredit(models.Model):
    name = models.CharField(max_length=100)
    maxClaim = models.DecimalField(decimal_places=4, max_digits=10)
    year = models.ForeignKey(Year, related_name="%(class)s_name", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Tax Credit: name:{self.name} maxClaim:{self.maxClaim} year:{self.year.name}'


# more to come

