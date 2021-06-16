from django.db import models


class Problem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    problem_id = models.CharField(db_column='PROBLEM_ID', max_length=32)  # Field name made lowercase.
    puid = models.CharField(db_column='PUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128)  # Field name made lowercase.
    problem_decription = models.TextField(db_column='PROBLEM_DECRIPTION', blank=True,
                                          null=True)  # Field name made lowercase.
    module_decription = models.TextField(db_column='MODULE_DECRIPTION', blank=True,
                                         null=True)  # Field name made lowercase.
    input_decription = models.TextField(db_column='INPUT_DECRIPTION', blank=True,
                                        null=True)  # Field name made lowercase.
    output_decription = models.TextField(db_column='OUTPUT_DECRIPTION', blank=True,
                                         null=True)  # Field name made lowercase.
    test_decription = models.CharField(db_column='TEST_DECRIPTION', max_length=32, blank=True,
                                       null=True)  # Field name made lowercase.
    difficulty = models.IntegerField(db_column='DIFFICULTY', blank=True, null=True)  # Field name made lowercase.
    resource_limit = models.DecimalField(db_column='RESOURCE_LIMIT', max_digits=32, decimal_places=10, blank=True,
                                         null=True)  # Field name made lowercase.
    freq_limit = models.DecimalField(db_column='FREQ_LIMIT', max_digits=32, decimal_places=10, blank=True,
                                     null=True)  # Field name made lowercase.
    power_limit = models.DecimalField(db_column='POWER_LIMIT', max_digits=32, decimal_places=10, blank=True,
                                      null=True)  # Field name made lowercase.
    public_status = models.IntegerField(db_column='PUBLIC_STATUS', blank=True, null=True)  # Field name made lowercase.
    platform = models.IntegerField(db_column='PLATFORM', blank=True, null=True)  # Field name made lowercase.
    publish_status = models.IntegerField(db_column='PUBLISH_STATUS', blank=True,
                                         null=True)  # Field name made lowercase.
    pcateory = models.CharField(db_column='PCATEORY', max_length=1024, blank=True,
                                null=True)  # Field name made lowercase.
    ptag = models.CharField(db_column='PTAG', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    online_testbench = models.CharField(db_column='ONLINE_TESTBENCH', max_length=1024, blank=True,
                                        null=True)  # Field name made lowercase.
    online_testbench_md5 = models.CharField(db_column='ONLINE_TESTBENCH_MD5', max_length=128, blank=True,
                                            null=True)  # Field name made lowercase.
    board_testbench = models.CharField(db_column='BOARD_TESTBENCH', max_length=1024, blank=True,
                                       null=True)  # Field name made lowercase.
    board_testbench_md5 = models.CharField(db_column='BOARD_TESTBENCH_MD5', max_length=128, blank=True,
                                           null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_problem'


class Ptag(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_ptag'


class Device(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sn = models.CharField(db_column='SN', max_length=32)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=32)  # Field name made lowercase.
    mmac = models.CharField(db_column='MMAC', max_length=32)  # Field name made lowercase.
    mip = models.CharField(db_column='MIP', max_length=32)  # Field name made lowercase.
    mfr_time = models.DateTimeField(db_column='MFR_TIME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_device'


class Drecord(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    device_id = models.ForeignKey('Device', on_delete=models.CASCADE, db_column='device_id')
    info = models.CharField(db_column='INFO', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_drecord'


class Pcateory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_pcateory'


class Pgroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey("Pgroup", db_column='pid', on_delete=models.SET_NULL, blank=True,
                            null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    decription = models.TextField(db_column='DECRIPTION', blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_pgroup'


class Precord(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE, db_column='PROBLEM_ID')
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, db_column="USER_ID")
    token = models.CharField(db_column='TOKEN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    result = models.IntegerField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase.
    platform = models.IntegerField(db_column='PLATFORM', blank=True, null=True)  # Field name made lowercase.
    resource = models.DecimalField(db_column='RESOURCE', max_digits=32, decimal_places=10, blank=True,
                                   null=True)  # Field name made lowercase.
    freq = models.DecimalField(db_column='FREQ', max_digits=32, decimal_places=10, blank=True,
                               null=True)  # Field name made lowercase.
    power = models.DecimalField(db_column='POWER', max_digits=32, decimal_places=10, blank=True,
                                null=True)  # Field name made lowercase.
    time = models.DecimalField(db_column='TIME', max_digits=32, decimal_places=10, blank=True,
                               null=True)  # Field name made lowercase.
    verify_point = models.CharField(db_column='VERIFY_POINT', max_length=1024, blank=True,
                                    null=True)  # Field name made lowercase.
    verify_server_id = models.CharField(db_column='VERIFY_SERVER_ID', max_length=32, blank=True,
                                        null=True)  # Field name made lowercase.
    verify_start_time = models.DateTimeField(db_column='VERIFY_START_TIME', blank=True,
                                             null=True)  # Field name made lowercase.
    verify_finish_time = models.DateTimeField(db_column='VERIFY_FINISH_TIME', blank=True,
                                              null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_precord'


class Poprecord(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE, db_column='problem_id')
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, db_column='user_id')
    datatime = models.DateTimeField(db_column='DATATIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_poprecord'


class Propcate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE, db_column='problem_id')
    pcateory_id = models.ForeignKey('Pcateory', on_delete=models.CASCADE, db_column='pcateory_id')
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_propcate'


class Propgroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pgroup_id = models.ForeignKey('Pgroup', on_delete=models.CASCADE, db_column='pgroup_id')
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE, db_column='problem_id')
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_propgroup'


class Proptag(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    problem_id = models.ForeignKey('Problem', on_delete=models.CASCADE, db_column='problem_id')
    ptag_id = models.ForeignKey('Ptag', on_delete=models.CASCADE, db_column='ptag_id')
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_proptag'


class Psource(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    decription = models.CharField(db_column='DECRIPTION', max_length=1024, blank=True,
                                  null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='CREATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    # created_by = models.ForeignKey('user.User', db_column='created_by', on_delete="cascade")
    created_time = models.DateTimeField(db_column='CREATED_TIME', blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    updated_time = models.DateTimeField(db_column='UPDATED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ego_psource'
