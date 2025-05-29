from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=50)

class Feature(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    plans = models.ManyToManyField(Plan, related_name='features')

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class TenantUser(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128) 
    is_admin = models.BooleanField(default=False)

class FeatureUsage(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    usage_count = models.PositiveIntegerField(default=0)
