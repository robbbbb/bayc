from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TransferEvent
from .serializer import TransferEventSerializer


# get all transfer events
class TransferEventsView(APIView):
    def get(self, request):
        transfer_events = TransferEvent.objects.all()
        serializer = TransferEventSerializer(transfer_events, many=True)
        return Response(serializer.data)


# get specific transfer event by token id
class TransferEventDetailView(APIView):

    def get(self, request, token_id):
        transfer_event = TransferEvent.objects.get(token_id=token_id)
        serializer = TransferEventSerializer(transfer_event)
        return Response(serializer.data)
