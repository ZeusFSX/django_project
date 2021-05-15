"""datascience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from markup import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'article', views.ArticleViewSet, 'article')
router.register(r'entity', views.EntityViewSet, 'entity')


urlpatterns = [
    path('', include(router.urls)),
    path('account/register', views.UserCreate.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chat/', include('markup.urls')),
    path('openapi',
         get_schema_view(
            title="Markup",
            description="API for text Markup, "
                        "the API can store marked data for Sentimental Analysis and Named Entity Recognition",
            version="1.0.0"
         ),
         name='openapi-schema'),

    path('redoc/',
         TemplateView.as_view(
                    template_name='redoc.html',
                    extra_context={'schema_url': 'openapi-schema'}
         ),
         name='redoc'),

    path('swagger-ui/',
         TemplateView.as_view(
            template_name='swagger-ui.html',
            extra_context={'schema_url': 'openapi-schema'}
         ),
         name='swagger-ui'),
]
