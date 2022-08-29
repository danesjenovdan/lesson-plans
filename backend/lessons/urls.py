from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from lessons.views import LessonViewSet

app_name = "lessons"

router = DefaultRouter()
router.register(r"", LessonViewSet)

urlpatterns = []

urlpatterns += router.urls
