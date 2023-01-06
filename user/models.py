from hashlib import sha1

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class UsrInfo(AbstractBaseUser):
    usr_key = models.CharField(db_column='USR_KEY', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='PWD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usr_id = models.CharField(db_column='USR_ID', max_length=100, blank=True, null=True, unique=True)  # Field name
    # made
    # lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    usr_typ = models.CharField(db_column='USR_TYP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usr_knd = models.CharField(db_column='USR_KND', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usr_nm = models.CharField(db_column='USR_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gen = models.CharField(db_column='GEN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birth = models.CharField(db_column='BIRTH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lunisolar = models.CharField(db_column='LUNISOLAR', max_length=1, blank=True, null=True)
    tel = models.CharField(db_column='TEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    htel = models.CharField(db_column='HTEL', max_length=13, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=7, blank=True, null=True)  # Field name made lowercase.
    addr1 = models.CharField(db_column='ADDR1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    addr2 = models.CharField(db_column='ADDR2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_dttm = models.DateTimeField(db_column='REG_DTTM', blank=True, null=True)  # Field name made lowercase.
    join_dttm = models.DateTimeField(db_column='JOIN_DTTM', blank=True, null=True)  # Field name made lowercase.
    mdf_dttm = models.DateTimeField(db_column='MDF_DTTM', blank=True, null=True)  # Field name made lowercase.
    del_dttm = models.DateTimeField(db_column='DEL_DTTM', blank=True, null=True)  # Field name made lowercase.
    cash = models.IntegerField(db_column='CASH', blank=True, null=True)  # Field name made lowercase.
    point = models.IntegerField(db_column='POINT', blank=True, null=True)  # Field name made lowercase.
    not_pwd = models.IntegerField(db_column='NOT_PWD', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='LAST_LOGIN', blank=True, null=True)  # Field name made lowercase.
    mthd = models.CharField(db_column='MTHD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sns_knd = models.CharField(db_column='SNS_KND', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dvs_cnt = models.IntegerField(db_column='DVS_CNT', blank=True, null=True)  # Field name made lowercase.
    usr_thum = models.CharField(db_column='USR_THUM', max_length=100, blank=True, null=True)
    sms_yn = models.CharField(db_column='SMS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mail_yn = models.CharField(db_column='MAIL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usr_eng_nm = models.CharField(db_column='USR_ENG_NM', max_length=30, blank=True, null=True)
    job = models.CharField(db_column='JOB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usr_msg = models.CharField(db_column='USR_MSG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usr_img = models.CharField(db_column='USR_IMG', max_length=100, blank=True, null=True)  # Field name made lowercase.

    objects = UserManager()

    # 고유한 식별자로 사용되는 필드명
    USERNAME_FIELD = 'usr_id'
    # 사용자를 만들 때 필수로 입력하게 되는 필드리스트
    # REQUIRED_FIELDS = ['usr_id']

    class Meta:
        managed = False
        db_table = 'USR_INFO'

    def check_password(self, raw_password):
        print(raw_password)
        hash_raw_password = "*" + (sha1(sha1(raw_password.encode(encoding='UTF-8')).digest()).hexdigest()).upper()
        return bool(self.password == hash_raw_password)

    class UsrDtl(models.Model):
        usr_key = models.OneToOneField('UsrInfo', models.DO_NOTHING, db_column='USR_KEY',
                                       primary_key=True)  # Field name made lowercase.
        rcm_id = models.CharField(db_column='RCM_ID', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
        rcm_key = models.CharField(db_column='RCM_KEY', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
        path = models.CharField(db_column='PATH', max_length=3, blank=True, null=True)  # Field name made lowercase.
        path_etc = models.CharField(db_column='PATH_ETC', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
        job = models.CharField(db_column='JOB', max_length=100, blank=True, null=True)  # Field name made lowercase.
        job_career_years = models.IntegerField(db_column='JOB_CAREER_YEARS', blank=True,
                                               null=True)  # Field name made lowercase.
        goal = models.CharField(db_column='GOAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
        pps = models.CharField(db_column='PPS', max_length=100, blank=True, null=True)  # Field name made lowercase.
        std_dt = models.CharField(db_column='STD_DT', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
        std_lvl = models.CharField(db_column='STD_LVL', max_length=3, blank=True,
                                   null=True)  # Field name made lowercase.
        std_line = models.CharField(db_column='STD_LINE', max_length=3, blank=True,
                                    null=True)  # Field name made lowercase.
        sch_yaer = models.CharField(db_column='SCH_YAER', max_length=3, blank=True,
                                    null=True)  # Field name made lowercase.
        sms_yn = models.CharField(db_column='SMS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
        mail_yn = models.CharField(db_column='MAIL_YN', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
        dm_yn = models.CharField(db_column='DM_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
        usr_auth_seq = models.IntegerField(db_column='USR_AUTH_SEQ', blank=True,
                                           null=True)  # Field name made lowercase.
        band_cd = models.CharField(db_column='BAND_CD', max_length=3, blank=True,
                                   null=True)  # Field name made lowercase.
        ad_seq = models.CharField(db_column='AD_SEQ', max_length=12, blank=True,
                                  null=True)  # Field name made lowercase.
        etc1 = models.CharField(db_column='ETC1', max_length=100, blank=True, null=True)  # Field name made lowercase.
        etc2 = models.CharField(db_column='ETC2', max_length=100, blank=True, null=True)  # Field name made lowercase.
        step1_alim = models.CharField(db_column='STEP1_ALIM', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
        step2_alim = models.CharField(db_column='STEP2_ALIM', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.

        class Meta:
            managed = False
            db_table = 'USR_DTL'
