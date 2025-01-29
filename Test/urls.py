from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views  import TokenObtainPairView, TokenRefreshView
from news import views
# from main import views  
# PostViewSet, TagViewSet
# from main.urls import urls as main_urls, TodoView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
        path('', views.test_home, name='test_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TestDetailView.as_view(), name='test-detail'),
    path('<int:pk>/update', views.TestUpdateView.as_view(), name='test-update'),
    path('<int:pk>/delete', views.TestDeleteView.as_view(), name='test-delete')
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = DefaultRouter()

# router.register(r'tags', TagViewSet, basename='tags')
# router.register(r'posts', views.PostViewSet, basename='posts')
# router.register(r'topic', views.TopicViewSet, basename='topic')

api_urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
