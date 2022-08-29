from demo.viewset import TeacherViewSet, StudentClassesSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet)
router.register('All', StudentClassesSerializer)


