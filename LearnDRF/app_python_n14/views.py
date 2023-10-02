from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pupils
from .serializers import PupilsSerializer


# Create your views here.
class PupilsListView(ListAPIView):
    # queryset = Pupils.objects.all()
    serializer_class = PupilsSerializer

    def get_queryset(self):
        try:
            pass_score = self.request.GET["pass_score"]
            queryset = Pupils.objects.filter(exam_mark__gte=pass_score).value()
        except:
            queryset = Pupils.objects.all().values()
        return queryset


class PupilsView(APIView):
    def get(self, request):
        try:
            pass_score = request.GET["pass_score"]
            pupils = Pupils.objects.filter(exam_mark=pass_score).value()
        except:
            pupils = Pupils.objects.all().values()
        return Response({"pupils": list(pupils)})

    def post(self, request):
        new_pupil = Pupils.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            exam_mark=request.data["exam_mark"],
        )
        return Response({"new_pupil": model_to_dict(new_pupil)})

    def delete(self, request):
        try:
            pupil_id = request.GET["pupil_id"]
            Pupils.objects.filter(pk=pupil_id).delete()
            return Response(
                {
                    "result": "success",
                    "desc": f"Pupil with id{pupil_id} successfully deleted",
                }
            )
        except:
            return Response(
                {"result": "error", "desc": "Internal server error! Please try later."}
            )
