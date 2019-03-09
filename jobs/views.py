from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.core.exceptions import PermissionDenied

class JobListView(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobsSerializer

class CreateJobView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.JobsSerializer
    queryset = models.Job.objects.all()
    def perform_create(self, serializer_class):
        if self.request.user.user_type == 'E':
            serializer_class.save()
        else:
            PermissionDenied


# class CreateQuote(generics.CreateAPIView):
# 	authentication_classes = (TokenAuthentication,SessionAuthentication,)
# 	permission_classes = (IsAuthenticated,)
# 	serializer_class = QuoteSerializer
# 	queryset = Quote.objects.all()
# 	def perform_create(self, serializer_class):
# 		book = Booking.objects.get(id=self.kwargs['pk'])
# 		if book.act.user == self.request.user:
# 			serializer_class.save(booking = book)
# 			book.quote_received = True
# 			book.save()
# 			send_mail('quote',book.client,book.act,book)
#
# 		else:
# 			PermissionDenied
