from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')

@api_view(['GET'])
def health_check(request):
    return Response('Ok')
