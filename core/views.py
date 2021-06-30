from django.shortcuts import render
from .models import Encoder, Decoder
from .serializer import EncoderSerialzier, DecoderSerialzier
from rest_framework import viewsets


class EncoderViewSet(viewsets.ModelViewSet):
    queryset = Encoder.objects.all()
    serializer_class = EncoderSerialzier

    def get_queryset(self):

        data = Encoder.objects.all()

        return data


class DecoderViewSet(viewsets.ModelViewSet):
    queryset = Decoder.objects.all()
    serializer_class = DecoderSerialzier

    def get_queryset(self):

        data = Decoder.objects.all()

        return data

