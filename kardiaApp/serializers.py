from rest_framework import serializers
from .models import ZettelCard, Tag, Topic, Verse, Reference, MediaResource, CustomField, CustomFieldValue

class ZettelCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZettelCard
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'

class MediaResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaResource
        fields = '__all__'

class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'

class CustomFieldValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFieldValue
        fields = '__all__'