from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views  import TokenObtainPairView, TokenRefreshView, TagViewSet
from . import views  
# PostViewSet, TagViewSet
# from main.urls import urls as main_urls, TodoView


urlpatterns = [
    path('', views.index, name='home'),
    path('about123', views.about, name='about'),
    path('log_in', views.log_in, name='log_in'),
]

# router = DefaultRouter()

# router.register(r'tags', TagViewSet, basename='tags')
# router.register(r'posts', views.PostViewSet, basename='posts')
# router.register(r'topic', views.TopicViewSet, basename='topic')

# api_urlpatterns = router.urls + [
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

# ]
