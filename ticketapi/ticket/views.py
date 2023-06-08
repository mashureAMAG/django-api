from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.permissions import IsAuthenticated

"""
Below Function going to display all the tasks store in the data base.
"""


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ticketList(request):
    tickets = Ticket.objects.filter(created_by=request.user.id)
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ticketDetail(request, pk):
    tickets = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(tickets, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def ticketUpdate(request, pk):
    ticket = Ticket.objects.get(id=pk)
    serializer = TicketSerializer(instance=ticket, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ticketCreate(request):
    data = {"name": request.data.get("name"), "created_by": request.user.id}

    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ticketReserve(request, pk):
    ticket = Ticket.objects.filter(id=pk, reserved=False).first()
    if ticket is None:
        return Response("Ticket is not available for reservation")

    data = {"reserved": True, "reserved_by": request.user.id}
    serializer = TicketSerializer(ticket, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def ticketDelete(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return Response("Tickets deleted successfully.")
