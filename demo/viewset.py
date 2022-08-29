from rest_framework import viewsets, status
from demo import modelss
from rest_framework.decorators import action
from . import serializers
from rest_framework.response import Response

from .modelss import Teacher

print(modelss)


class TeacherViewSet(viewsets.ModelViewSet):
    """
    Create a custom method for post
    """
    queryset = modelss.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializers

    @action(detail=True, methods=['POST'])
    def rate_teacher(self, req, pk = None):
        if 'email' in req.data:
            teacher  = modelss.Teacher.objects.get(teacher_id=pk)
            print('teacher name:-', teacher.teacher_name)
            res = {'message': 'its working'}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {'message': 'You need to provide the email'}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)





class StudentClassesSerializer(viewsets.ModelViewSet):
    queryset = modelss.StudentClasses.objects.all()
    # queryset = modelss.Teacher.objects.all()

    serializer_class = serializers.StudentClassesSerializer

class StudentsSerializer(viewsets.ModelViewSet):
    queryset = modelss.Student.objects.all()
    serializer_class = serializers.StudentClassesSerializer


class HomeworksSerializer(viewsets.ModelViewSet):
    queryset = modelss.Homeworks.objects.all()
    serializer_class = serializers.StudentClassesSerializer

class SubjectSerializer(viewsets.ModelViewSet):
    queryset = modelss.Subject.objects.all()
    serializer_class = serializers.StudentClassesSerializer
