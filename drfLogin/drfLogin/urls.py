from django.contrib import admin
from django.urls import path, include, re_path as url

# 스웨거 설정
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# 스웨거 설정
schema_url_patterns = [ 
    path('', include('user.urls')),
    ]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="drfLogin Test API",
        default_version='v1',
        description="Development drfLogin Test Document",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('allauth.urls')),
    path('api/user/', include('user.urls')),
    

    # 스웨거 설정
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

