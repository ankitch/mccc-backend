from rest_framework import serializers

from apps.send.models import Replies


class RepliesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['company'] = self.context['request'].company
        return super().create(validated_data)

    class Meta:
        model = Replies
        fields = ('id', 'mobile_number', 'message', 'timestamp')
