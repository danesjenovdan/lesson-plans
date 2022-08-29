from rest_framework.routers import DefaultRouter

from lessons.views import LessonViewSet, DownloadViewSet

app_name = "lessons"

router = DefaultRouter()
router.register(r"lessons", LessonViewSet)
router.register(r"download", DownloadViewSet)

urlpatterns = []

urlpatterns += router.urls
