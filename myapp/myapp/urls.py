from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, viewsets, serializers
from django.contrib import admin

from . import views


# #serializers define the api representation
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# #viewsets define the view behavior
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# #routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include('snippets.urls')),
#     # path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


from snippets.views import RegisterView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('snippets.urls')),  # Aquí se incluyen las URLs de tu aplicación
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
]

# Agregamos el inicio de sesión y cierre de sesión de la API
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
   
]