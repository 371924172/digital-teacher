from django.db import models


# Create your models here.
class Class(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    college_id = models.ForeignKey('College', on_delete=models.CASCADE, db_column='college_id')
    major_id = models.ForeignKey('Major', on_delete=models.CASCADE, db_column='major_id')
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    estab_date = models.DateField(db_column='ESTAB_DATE', blank=True, null=True)  # Field name made lowercase.
    year_number = models.IntegerField(db_column='YEAR_NUMBER', blank=True, null=True)  # Field name made lowercase.
    crated_by = models.CharField(db_column='CRATED_BY', max_length=32, blank=True,
                                 null=True)  # Field name made lowercase.
    crated_time = models.DateTimeField(db_column='CRATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_class'


class College(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=128, blank=True,
                                  null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    president = models.CharField(db_column='PRESIDENT', max_length=32, blank=True,
                                 null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_college'


class Lesson(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_lesson'


class Major(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=128, blank=True,
                                  null=True)  # Field name made lowercase.
    estab_date = models.DateField(db_column='ESTAB_DATE', blank=True, null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    tuition_fee = models.CharField(db_column='TUITION_FEE', max_length=32, blank=True,
                                   null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_major'


class Organization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=128, blank=True,
                                  null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_organization'


class Selclass(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='user_id')
    lesson_id = models.ForeignKey('Lesson', on_delete=models.CASCADE, db_column='lesson_id')
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, db_column='class_id')
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_selclass'


class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organization_id = models.ForeignKey("Organization", on_delete=models.CASCADE, db_column='organization_id')
    college_id = models.ForeignKey('College', on_delete=models.CASCADE, db_column='college_id')
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, db_column='class_id')
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    entry_date = models.DateField(db_column='ENTRY_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_student'


class Teacher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    college_id = models.ForeignKey('College', on_delete=models.CASCADE, db_column='college_id')
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_teacher'


class Instruct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE, db_column='teacher_id')
    class_id = models.ForeignKey('Class', on_delete=models.CASCADE, db_column='class_id')
    lesson_id = models.ForeignKey('Lesson', on_delete=models.CASCADE, db_column='lesson_id')
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_instruct'
