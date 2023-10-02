from rest_framework.serializers import ModelSerializer
from .models import Pupils


class PupilsSerializer(ModelSerializer):
    class Meta:
        model = Pupils
        field = "__all__"
