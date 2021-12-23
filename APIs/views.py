import sys

from django.http import Http404
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from django.http import Http404
from .utils import *

@api_view(['GET'])
@precheck(['payment_id'])
def getOrder(request):
    try:
        data = request.GET
        print(data)
        payment_id = data['payment_id']
        orders = get_list_or_404(Order, payment_id=str(payment_id))
        email = orders[0].email

        serializer = OrderSerializer(orders, many=True)
        print(serializer.data)
        return Response({'action': "Order Serializer", 'message': "Found", 'data': serializer.data,
                         'payment_id': payment_id, 'email': email},
                        status=status.HTTP_200_OK)
    except Http404:
        return Response({'action': "Order Serializer", 'message': "Not Found", },
                        status=status.HTTP_404_NOT_FOUND)
    except:
        print("Unexpected error:", sys.exc_info())
        return Response({'action': "Order Serializer", 'message': "Something Went Wrong!"},
                        status=status.HTTP_400_BAD_REQUEST)




