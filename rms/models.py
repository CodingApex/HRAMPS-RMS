from django.db import models


class HsHrEmployee(models.Model):
    emp_number = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=50, blank=True, null=True)
    emp_lastname = models.CharField(max_length=100)
    emp_firstname = models.CharField(max_length=100)
    emp_middle_name = models.CharField(max_length=100)
    emp_nick_name = models.CharField(max_length=100, blank=True, null=True)
    emp_smoker = models.SmallIntegerField(blank=True, null=True)
    ethnic_race_code = models.CharField(max_length=13, blank=True, null=True)
    emp_birthday = models.DateField(blank=True, null=True)
    nation_code = models.ForeignKey('OhrmNationality', models.DO_NOTHING, db_column='nation_code', blank=True, null=True)
    emp_gender = models.SmallIntegerField(blank=True, null=True)
    emp_marital_status = models.CharField(max_length=20, blank=True, null=True)
    emp_ssn_num = models.CharField(max_length=100, db_collation='latin1_swedish_ci', blank=True, null=True)
    emp_sin_num = models.CharField(max_length=100, blank=True, null=True)
    emp_other_id = models.CharField(max_length=100, blank=True, null=True)
    emp_dri_lice_num = models.CharField(max_length=100, blank=True, null=True)
    emp_dri_lice_exp_date = models.DateField(blank=True, null=True)
    emp_military_service = models.CharField(max_length=100, blank=True, null=True)
    emp_status = models.ForeignKey('OhrmEmploymentStatus', models.DO_NOTHING, db_column='emp_status', blank=True, null=True)
    job_title_code = models.ForeignKey('OhrmJobTitle', models.DO_NOTHING, db_column='job_title_code', blank=True, null=True)
    eeo_cat_code = models.ForeignKey('OhrmJobCategory', models.DO_NOTHING, db_column='eeo_cat_code', blank=True, null=True)
    work_station = models.ForeignKey('OhrmSubunit', models.DO_NOTHING, db_column='work_station', blank=True, null=True)
    emp_street1 = models.CharField(max_length=100, blank=True, null=True)
    emp_street2 = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=100, blank=True, null=True)
    coun_code = models.CharField(max_length=100, blank=True, null=True)
    provin_code = models.CharField(max_length=100, blank=True, null=True)
    emp_zipcode = models.CharField(max_length=20, blank=True, null=True)
    emp_hm_telephone = models.CharField(max_length=50, blank=True, null=True)
    emp_mobile = models.CharField(max_length=50, blank=True, null=True)
    emp_work_telephone = models.CharField(max_length=50, blank=True, null=True)
    emp_work_email = models.CharField(max_length=50, blank=True, null=True)
    sal_grd_code = models.CharField(max_length=13, blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    emp_oth_email = models.CharField(max_length=50, blank=True, null=True)
    termination = models.ForeignKey('OhrmEmpTermination', models.DO_NOTHING, blank=True, null=True)
    custom1 = models.CharField(max_length=250, blank=True, null=True)
    custom2 = models.CharField(max_length=250, blank=True, null=True)
    custom3 = models.CharField(max_length=250, blank=True, null=True)
    custom4 = models.CharField(max_length=250, blank=True, null=True)
    custom5 = models.CharField(max_length=250, blank=True, null=True)
    custom6 = models.CharField(max_length=250, blank=True, null=True)
    custom7 = models.CharField(max_length=250, blank=True, null=True)
    custom8 = models.CharField(max_length=250, blank=True, null=True)
    custom9 = models.CharField(max_length=250, blank=True, null=True)
    custom10 = models.CharField(max_length=250, blank=True, null=True)
    purged_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hs_hr_employee'


class OhrmJobTitle(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.CharField(max_length=400, blank=True, null=True)
    note = models.CharField(max_length=400, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ohrm_job_title'


class OhrmSubunit(models.Model):
    name = models.CharField(unique=True, max_length=100)
    unit_id = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    lft = models.PositiveSmallIntegerField(blank=True, null=True)
    rgt = models.PositiveSmallIntegerField(blank=True, null=True)
    level = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ohrm_subunit'


class OhrmNationality(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ohrm_nationality'


class OhrmJobCategory(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ohrm_job_category'


class OhrmEmploymentStatus(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'ohrm_employment_status'


class OhrmEmpTermination(models.Model):
    emp_number = models.ForeignKey('HsHrEmployee', models.DO_NOTHING, db_column='emp_number', blank=True, null=True)
    reason = models.ForeignKey('OhrmEmpTerminationReason', models.DO_NOTHING, blank=True, null=True)
    termination_date = models.DateField()
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ohrm_emp_termination'


class OhrmEmpTerminationReason(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ohrm_emp_termination_reason'