from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_superuser = None
    first_name = None
    last_name = None
    is_staff = None
    date_joined = None
    last_login = None

    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=32, blank=True,
                                    null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=128, blank=True,
                                null=True)  # Field name made lowercase.
    wcactoken = models.CharField(db_column='WCACTOKEN', max_length=32, blank=True,
                                 null=True)  # Field name made lowercase.
    id_card_no = models.CharField(db_column='ID_CARD_NO', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    birth = models.DateField(db_column='BIRTH', blank=True, null=True)  # Field name made lowercase.
    avatar = models.ImageField(upload_to='avatar', db_column='AVATAR', max_length=32, blank=True,
                               null=True)  # Field name made lowercase.
    intro = models.CharField(db_column='INTRO', max_length=512, blank=True, null=True)  # Field name made lowercase.
    present_address = models.CharField(db_column='PRESENT_ADDRESS', max_length=128, blank=True,
                                       null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(auto_now=True)
    status = models.CharField(db_column='STATUS', max_length=32, blank=True, null=True,
                              default='FALSE')  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_user'


class Role(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(to='User', to_field='id', db_column="USER_ID", on_delete=models.CASCADE,
                             related_name='role', blank=True,
                             null=True)
    role_id = models.IntegerField(db_column="ROLE_ID", blank=True, null=True)
    name = models.CharField(db_column="NAME", max_length=32, blank=True, null=True)
    assign_id = models.CharField(db_column="ASSIGN_ID", max_length=32, blank=True, null=True)
    assign_time = models.DateTimeField(db_column="ASSIGN_TIME", blank=True, null=True)

    class Meta:
        managed = True
        db_table = "ego_role"
