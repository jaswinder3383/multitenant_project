from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tenant-login/', TenantLoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('select-plan/<int:pk>/', TenantSelectPlanView.as_view()),
    path('create-user/', CreateTenantUserView.as_view()),
    path('use-feature/', UseFeatureView.as_view()),
]
