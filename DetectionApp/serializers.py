from rest_framework import serializers
from .models import *


class ItemDetectionHistorySerializer(serializers.ModelSerializer):
    cg_name = serializers.CharField(required=False, source= 'cg_idx.cg_name')
    # cnt = serializers.IntegerField(required=False)
    class Meta:
        model = ItemdetectionSHistory
        fields = ('cg_idx', 'cg_name')

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class UploadCleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_Clean
        fields = '__all__'


class CategoryRegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRegulation
        fields = ('cg_name', )


class WasteCategorySSerializer(serializers.ModelSerializer):

    regulation = CategoryRegulationSerializer(source= 'categoryregulation_set', many=True)

    class Meta:
        model = WasteCategoryM
        fields = ('idx', 'cg_name', 'regulation')

class PointHistorySerializer(serializers.ModelSerializer):

    msg = serializers.CharField(max_length=45, required=False)
    code = serializers.IntegerField( required=False)
    user_name = serializers.CharField(source= 'user_idx.user_id', required=False)
    description = serializers.CharField(source= 'point_description.cg_name', required=False)

    class Meta:
        model = PointHistory
        fields =['idx','date', 'value', 'user_idx', 'point_description', 'msg', 'code', 'user_name', 'description']