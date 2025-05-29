from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from .tasks import send_billing_emails
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class CreateTenantView(generics.CreateAPIView):
    serializer_class = TenantSerializer
    permission_classes = [permissions.IsAdminUser]

class ListTenantsView(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.IsAdminUser]

class TenantUsersView(generics.ListAPIView):
    serializer_class = TenantUserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        tenant_id = self.kwargs['tenant_id']
        return TenantUser.objects.filter(tenant__id=tenant_id)

class CreatePlanView(generics.CreateAPIView):
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAdminUser]

class AddFeatureToPlanView(generics.CreateAPIView):
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk, *args, **kwargs):
        try:
            plan = Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            return Response({'error': 'Plan not found'}, status=404)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            feature = serializer.save()
            feature.plans.add(plan)  
            return Response({'message': 'Feature created and linked to plan'}, status=201)
        return Response(serializer.errors, status=400)

class TenantSelectPlanView(generics.UpdateAPIView):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()

    def update(self, request, *args, **kwargs):
        tenant = self.get_object()
        plan_id = request.data.get("plan")
        tenant.plan_id = plan_id
        tenant.save()
        return Response({'status': 'Plan selected'})
    

    
class TenantLoginView(generics.GenericAPIView):
    serializer_class = TenantLoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            tenant_user = TenantUser.objects.get(email__iexact=email.strip())
        except TenantUser.DoesNotExist:
            return Response({'error': 'Invalid credentials or not a tenant user'}, status=401)

        if password == tenant_user.password:
            is_admin = tenant_user.is_admin
            role = 'admin' if is_admin else 'user'
            
            refresh = RefreshToken()
            refresh['user_id'] = tenant_user.id
            refresh['tenant_id'] = tenant_user.tenant.id
            refresh['role'] = role
            
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'role': role,
                'tenant_id': tenant_user.tenant.id,
                'user_id': tenant_user.id
            })
        else:
            return Response({'error': 'Invalid credentials or not a tenant user'}, status=401)
class CreateTenantUserView(generics.CreateAPIView):
    serializer_class = TenantUserSerializer

class UseFeatureView(generics.CreateAPIView):
    serializer_class = FeatureUsageSerializer

    def post(self, request, *args, **kwargs):
        tenant_id = request.data.get('tenant')
        feature_id = request.data.get('feature')

        try:
            tenant = Tenant.objects.get(id=tenant_id)
            feature = Feature.objects.get(id=feature_id)
        except Tenant.DoesNotExist:
            return Response({'error': 'Tenant not found'}, status=404)
        except Feature.DoesNotExist:
            return Response({'error': 'Feature not found'}, status=404)

        obj, created = FeatureUsage.objects.get_or_create(
            tenant=tenant,
            feature=feature
        )
        obj.usage_count += 1
        obj.save()

        return Response({'status': 'Feature usage recorded'})
class TriggerBillingEmailView(generics.GenericAPIView):
    def get(self, request):
        send_billing_emails.delay()
        return Response({'status': 'Billing emails sent (queued)'})
