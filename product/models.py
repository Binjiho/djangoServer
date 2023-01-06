from django.db import models


class Goods(models.Model):
    sal_cd = models.AutoField(db_column='SAL_CD', primary_key=True)  # Field name made lowercase.
    sal_mthd = models.CharField(db_column='SAL_MTHD', max_length=3)  # Field name made lowercase.
    sal_nm = models.CharField(db_column='SAL_NM', max_length=200)  # Field name made lowercase.
    sal_mng_nm = models.CharField(db_column='SAL_MNG_NM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sal_snm = models.CharField(db_column='SAL_SNM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prod_knd_cd = models.ForeignKey('ProdKnd', models.DO_NOTHING, db_column='PROD_KND_CD')  # Field name made lowercase.
    cost_price = models.IntegerField(db_column='COST_PRICE', blank=True, null=True)  # Field name made lowercase.
    sal_amt = models.PositiveIntegerField(db_column='SAL_AMT')  # Field name made lowercase.
    dlv_typ = models.CharField(db_column='DLV_TYP', max_length=3)  # Field name made lowercase.
    cash_use_yn = models.CharField(db_column='CASH_USE_YN', max_length=1)  # Field name made lowercase.
    point_use_yn = models.CharField(db_column='POINT_USE_YN', max_length=1)  # Field name made lowercase.
    cpn_use_yn = models.CharField(db_column='CPN_USE_YN', max_length=1)  # Field name made lowercase.
    sal_sdt = models.DateField(db_column='SAL_SDT', blank=True, null=True)  # Field name made lowercase.
    sal_edt = models.DateField(db_column='SAL_EDT', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2)  # Field name made lowercase.
    reg_dttm = models.DateTimeField(db_column='REG_DTTM')  # Field name made lowercase.
    adm_id = models.CharField(db_column='ADM_ID', max_length=20)  # Field name made lowercase.
    basic_yn = models.CharField(db_column='BASIC_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dp_state = models.CharField(db_column='DP_STATE', max_length=3)  # Field name made lowercase.
    use_mthds = models.CharField(db_column='USE_MTHDS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sal_thum = models.CharField(db_column='SAL_THUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sal_thum2 = models.CharField(db_column='SAL_THUM2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sal_intro = models.TextField(db_column='SAL_INTRO', blank=True, null=True)  # Field name made lowercase.
    sal_sintro = models.CharField(db_column='SAL_SINTRO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sal_bft = models.CharField(db_column='SAL_BFT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sal_cate = models.IntegerField(db_column='SAL_CATE')  # Field name made lowercase.
    sal_scate = models.IntegerField(db_column='SAL_SCATE')  # Field name made lowercase.
    etc_gb = models.CharField(db_column='ETC_GB', max_length=3)  # Field name made lowercase.
    dp_sal_cd = models.IntegerField(db_column='DP_SAL_CD', blank=True, null=True)  # Field name made lowercase.
    grp_seq = models.IntegerField(db_column='GRP_SEQ', blank=True, null=True)  # Field name made lowercase.
    dp_info = models.CharField(db_column='DP_INFO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dp_ord = models.PositiveSmallIntegerField(db_column='DP_ORD', blank=True, null=True)  # Field name made lowercase.
    menu_nm = models.CharField(db_column='MENU_NM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    r_badge = models.CharField(db_column='R_BADGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dp_state_yn = models.CharField(db_column='DP_STATE_YN', max_length=1)  # Field name made lowercase.
    action_yn = models.CharField(db_column='ACTION_YN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    top_yn = models.CharField(db_column='TOP_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dvs_cnt = models.IntegerField(db_column='DVS_CNT', blank=True, null=True)  # Field name made lowercase.
    etc_gb2 = models.DateField(db_column='ETC_GB2', blank=True, null=True)  # Field name made lowercase.
    sal_dt = models.TextField(db_column='SAL_DT', blank=True, null=True)  # Field name made lowercase.
    store = models.IntegerField(db_column='STORE', blank=True, null=True)  # Field name made lowercase.
    sal_url = models.CharField(db_column='SAL_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chr_stage = models.IntegerField(db_column='CHR_STAGE', blank=True, null=True)  # Field name made lowercase.
    live_type = models.IntegerField(db_column='LIVE_TYPE', blank=True, null=True)  # Field name made lowercase.
    live_limit = models.IntegerField(db_column='LIVE_LIMIT', blank=True, null=True)  # Field name made lowercase.
    live_manual = models.IntegerField(db_column='LIVE_MANUAL', blank=True, null=True)  # Field name made lowercase.
    live_sal_sdt = models.DateTimeField(db_column='LIVE_SAL_SDT', blank=True, null=True)  # Field name made lowercase.
    live_sal_edt = models.DateTimeField(db_column='LIVE_SAL_EDT', blank=True, null=True)  # Field name made lowercase.
    cpn_mas = models.IntegerField(db_column='CPN_MAS', blank=True, null=True)  # Field name made lowercase.
    off_grp = models.IntegerField(db_column='OFF_GRP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GOODS'
        unique_together = (('sal_cd', 'sal_mthd'),)


class GoodsDtl(models.Model):
    dtl_seq = models.AutoField(db_column='DTL_SEQ', primary_key=True)  # Field name made lowercase.
    sal_cd = models.IntegerField(db_column='SAL_CD')  # Field name made lowercase.
    info_knd = models.CharField(db_column='INFO_KND', max_length=3, db_collation='utf8_general_ci')  # Field name made lowercase.
    info_img = models.CharField(db_column='INFO_IMG', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    info_ttl = models.CharField(db_column='INFO_TTL', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    info_cmnt = models.TextField(db_column='INFO_CMNT', blank=True, null=True)  # Field name made lowercase.
    ref_vod = models.IntegerField(db_column='REF_VOD', blank=True, null=True)  # Field name made lowercase.
    ref_ttl = models.CharField(db_column='REF_TTL', max_length=200, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    ref_cmnt = models.TextField(db_column='REF_CMNT', blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1, db_collation='utf8_general_ci')  # Field name made lowercase.
    dp_ord = models.IntegerField(db_column='DP_ORD')  # Field name made lowercase.
    reg_dttm = models.DateTimeField(db_column='REG_DTTM')  # Field name made lowercase.
    mdf_dttm = models.DateTimeField(db_column='MDF_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GOODS_DTL'


class ProdKnd(models.Model):
    prod_knd_cd = models.CharField(db_column='PROD_KND_CD', primary_key=True, max_length=2)  # Field name made lowercase.
    prod_knd_nm = models.CharField(db_column='PROD_KND_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_dttm = models.DateTimeField(db_column='REG_DTTM')  # Field name made lowercase.
    adm_id = models.CharField(db_column='ADM_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='USE_YN', max_length=1)  # Field name made lowercase.
    dlv_yn = models.CharField(db_column='DLV_YN', max_length=1)  # Field name made lowercase.
    del_yn = models.CharField(db_column='DEL_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROD_KND'
