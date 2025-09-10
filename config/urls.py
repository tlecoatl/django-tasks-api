from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet,RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/', include(router.urls)),
    path('api/register/', RegisterUserView.as_view())
]
