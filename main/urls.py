from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views  import TokenObtainPairView, TokenRefreshView, TagViewSet
from . import views  
from django.conf import settings
from django.conf.urls.static import static
# PostViewSet, TagViewSet
# from main.urls import urls as main_urls, TodoView


urlpatterns = [
    path('', views.index, name='home'),
    path('about123', views.about, name='about'),
    path('log_in', views.log_in, name='log_in'),
    path('section', views.section, name='section'),
    path('info', views.info, name='info'),
    path('theme1/', views.theme1, name='theme1'),
    path('theme2/', views.theme2, name='theme2'),
    path('theme3/', views.theme3, name='theme3'),
    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# router = DefaultRouter()

# router.register(r'tags', TagViewSet, basename='tags')
# router.register(r'posts', views.PostViewSet, basename='posts')
# router.register(r'topic', views.TopicViewSet, basename='topic')

# api_urlpatterns = router.urls + [
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# ]
