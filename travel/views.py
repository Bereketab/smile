from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class DemoView(APIView):
    def get(self, request):
        content = {'message': 'Hello! This is a Demo!'}
        return Response(content)


def index(request):
    return render(request,'travel/index.html')