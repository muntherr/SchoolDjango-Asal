from django.db import models


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True, null=False)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'teacher'


class Classes(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classes'


class Homeworks(models.Model):
    homework_id = models.IntegerField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    fromg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homeworks'


class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)

    #  subject = models.OneToOneField(Subject, null =True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'student'


class StudentClasses(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    name = models.ForeignKey(Classes, on_delete=models.CASCADE, db_column='name')
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    #
    # def __str__(self):  # Convert the object to string and show it in the admin site
    #     return self.student.name

    class Meta:
        managed = False
        db_table = 'student_classes'
        unique_together = (('student', 'name', 'date_from'),)


class Teacherassignedclass(models.Model):
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, blank=True, null=True)
    class_field = models.OneToOneField(Classes, models.DO_NOTHING, db_column='class_id',
                                       primary_key=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'teacherassignedclass'
