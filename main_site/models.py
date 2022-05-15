from django.db import models

# Create your models here.
class CompanyInfo(models.Model):

	symbol = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
	sector = models.CharField(max_length = 255, default = 'N/A')
	price = models.FloatField()
	price_earnings = models.FloatField()
	dividend_yeild = models.FloatField()
	earning_per_share = models.FloatField()
	marker_cap = models.FloatField()
	EBITDA = models.FloatField()
	price_per_sales = models.FloatField()
	price_per_book = models.FloatField()
	link = models.URLField(max_length=200)