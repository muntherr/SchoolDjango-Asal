from rest_framework import serializers
from demo.modelss import Teacher as teacher, Student, Classes, Subject, StudentClasses


class TeacherSerializers(serializers.ModelSerializer):
    print("GGGGGGGGEEEEOOOOO")

    class Meta:
        model = teacher
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ClassesSerialize(serializers.ModelSerializer):
    subject = SubjectSerializers(many=False)
    teacher = TeacherSerializers(many=False)

    class Meta:
        model = Classes
        fields = ['name', 'subject', 'teacher', 'date_from', 'date_to']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentClassesSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False)
    name = ClassesSerialize(many=False)

    class Meta:
        model = StudentClasses
        fields = ['student', 'name', 'date_from', 'date_to']

# class All(serializers.ModelSerializer):
#     cl = Student(many=True)
#     #subject = Subject(many=True )
#
#     class Meta:
#         model = Student
#         fields = ['student_id', 'student_name', 'phone', 'gender', 'dob' , 'cl']
