"""KeyboardAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from keys_trening import views as keys_training
from rest_framework_simplejwt import views as jwt_views
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

router.register('keys_training', keys_training.KeyTrainingViewSet, basename='keys_training')
router.register('keys_pair_training', keys_training.KeyPairsTrainingViewSet, basename='keys_pair_training')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls')),

    # ---- JWT AUTHORIZATION START ----
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # ---- AUTHORIZATION END ----
    path('api/key_training/new/', keys_training.CreateKeyTraining.as_view(), name='new_client'),
    path('api/key_pairs_training/new/', keys_training.CreatePairsKeyTraining.as_view(), name='new_client'),

    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)