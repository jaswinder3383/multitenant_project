from rest_framework import serializers
from .models import Tenant, TenantUser, Plan, Feature, FeatureUsage

class TenantLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantUser
        fields = '__all__'


class FeatureUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureUsage
        fields = '__all__'
