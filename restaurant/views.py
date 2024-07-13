from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import menu, booking
from .serializers import MenuSerializer, Bookingserializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view
@permission_classes
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message:this view is protected"})

class MenuItemView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):

    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet): # automatically creates all CRUD options // works seemlesly with DRF routing / tidier code

    queryset = booking.objects.all()
    serializer_class = Bookingserializer
    permission_classes = [permissions.IsAuthenticated] 

