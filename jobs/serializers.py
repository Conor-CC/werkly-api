from rest_framework import serializers
from . import models

class JobsListSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details')

    def get_details(self, obj):
        details = {
            'id': obj.details.id,
            'job_name': obj.details.job_name,
            'date': obj.details.date,
            'time_from': obj.details.time_from,
            'time_to': obj.details.time_to,
            'pay_per_hour': obj.details.pay_per_hour,
            'address': obj.details.address,
            'description': obj.details.description,
            'required_experience': obj.details.required_experience
        }
        return details

class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('name',)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('tag',)

class DetailsSerializer(serializers.ModelSerializer):
    # tags = TagsSerializer(many=True)
    class Meta:
        model = models.Details
        fields = ('id', 'job_name', 'date', 'time_from', 'time_to', 'duration', 'pay_per_hour', 'address', 'description', 'required_experience')


class JobsCreationSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=False)
    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details')

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        job_object = models.Job.objects.create(**validated_data)
        models.Details.objects.create(job=job_object, **details_data)
        return job_object
