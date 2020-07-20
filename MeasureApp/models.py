from django.db import models
from userApp.models import User
import os
from uuid import uuid4
from django.utils import timezone
from DetectionApp.models import WasteCategoryS

# Create your models here.

def date_upload_measure(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return '/'.join([
        'measure',
        ymd_path,
        uuid_name + extension,
        ])



class MeasureHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image = models.ImageField()
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'measure_history'


class Upload(models.Model):
    image = models.ImageField(upload_to=date_upload_measure)
    class Meta:
        managed = False
        db_table = 'measure_upload'

class RegulationFee(models.Model):
    idx = models.AutoField(primary_key=True)
    fee_flag = models.CharField(max_length=45, blank=True, null=True)
    condition_value = models.FloatField(blank=True, null=True)
    cg_idx = models.ForeignKey(WasteCategoryS, models.DO_NOTHING, db_column='cg_idx', blank=True, null=True)
    over_fee = models.CharField(max_length=45, blank=True, null=True)
    down_fee = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regulation_fee'