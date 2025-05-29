"""
URL configuration for multitenant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="Multi-Tenant API", default_version='v1'),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Superadmin
    path('create-tenant/', views.CreateTenantView.as_view()),
    path('list-tenants/', views.ListTenantsView.as_view()),
    path('list-users/<int:tenant_id>/', views.TenantUsersView.as_view()),
    path('create-plan/', views.CreatePlanView.as_view()),
    path('add-feature/<int:pk>/', views.AddFeatureToPlanView.as_view()),

    # Billing trigger
    path('send-billings/', views.TriggerBillingEmailView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
