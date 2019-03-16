from rest_framework import serializers
from . import models

class JobsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details')

class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('name',)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('tag',)

class DetailsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True)
    class Meta:
        model = models.Details
        fields = ('id', 'job_name', 'time_from', 'time_to', 'duration', 'pay_per_hour', 'tags', 'address', 'description', 'required_experience')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        details = models.Details.objects.create(**validated_data)
        for obj in tags_data:
            tag = models.Tag.objects.filter(text=obj.tag)
            if tag.exists():
                new_tag = tag.first()
            else:
                new_tag = Tag.objects.get(**obj)
                tags.add(new_tag)
        return details

class JobsCreationSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=False)
    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details')

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        job = models.Job.objects.create(**validated_data)
        models.Details.objects.create(**details_data)
        return job
