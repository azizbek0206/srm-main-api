from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SMSShablon, Qarzdor
from .serializers import SMSShablonSerializer, QarzdorSerializer
from twilio.rest import Client
from django.conf import settings

class SMSShablonViewSet(viewsets.ModelViewSet):
    queryset = SMSShablon.objects.all()
    serializer_class = SMSShablonSerializer

class QarzdorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Qarzdor.objects.all()
    serializer_class = QarzdorSerializer







@api_view(['POST'])
def send_sms(request):
    target = request.data.get('target')
    message = request.data.get('message')

    if not target or not message:
        return Response({'error': 'target va message kerak'}, status=status.HTTP_400_BAD_REQUEST)

    if target == 'Qarzdorlar':
        qarzdorlar = Qarzdor.objects.all()
        numbers = [q.telefon for q in qarzdorlar]
    else:
        return Response({'error': 'Target noto‘g‘ri'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        for number in numbers:
            client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=number
            )
        return Response({'success': True, 'message': 'SMSlar yuborildi'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
