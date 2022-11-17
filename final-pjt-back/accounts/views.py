from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .serializers import *


# Create your views here.



