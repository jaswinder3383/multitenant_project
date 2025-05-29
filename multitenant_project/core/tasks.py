from celery import shared_task
from django.core.mail import send_mail
from .models import Tenant, FeatureUsage

@shared_task
def send_billing_emails():
    for tenant in Tenant.objects.all():
        print('tenant',tenant)
        usages = FeatureUsage.objects.filter(tenant=tenant)
        total = sum(u.usage_count * u.feature.price for u in usages)
        send_mail(
            subject=f"Billing for {tenant.name}",
            message=f"Your total bill is ${total}",
            from_email='jaswinderchandiwala@gmail.com',
            recipient_list=[tenant.email]
        )
