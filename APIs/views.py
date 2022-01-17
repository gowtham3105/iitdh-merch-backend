import sys
import os
from django.http import Http404
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from .utils import *


@api_view(['GET'])
@precheck(['payment_id'])
def getOrder(request):
    try:
        data = request.GET
        payment_id = data['payment_id']
        orders = get_list_or_404(Order, payment_id=str(payment_id))
        email = orders[0].email
        address = orders[0].address
        serializer = OrderSerializer(orders, many=True)
        return Response({'action': "Order Serializer", 'message': "Found", 'data': serializer.data,
                         'payment_id': payment_id, 'email': email, 'address': address},
                        status=status.HTTP_200_OK)
    except Http404:
        return Response({'action': "Order Serializer", 'message': "Not Found", },
                        status=status.HTTP_404_NOT_FOUND)
    except:
        print("Unexpected error:", sys.exc_info())
        return Response({'action': "Order Serializer", 'message': "Something Went Wrong!"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@precheck(['payment_id', 'password'])
def markOrder(request):
    try:
        PASSWORD = os.environ.get("USER_PASSWORD")

        data = request.data
        payment_id = data['payment_id']
        password = data['password']
        print(password, PASSWORD)
        if password == PASSWORD:
            should_deliver = None
            orders = get_list_or_404(Order, payment_id=str(payment_id))
            for order in orders:
                if order.order_status != 'Delivered':
                    order.order_status = "Delivered"
                    should_deliver = True
                    order.save()
                else:
                    should_deliver = False
            return Response({'action': "Order Marked", 'message': "Successfully Marked",
                             'payment_id': payment_id, "should_deliver": should_deliver},
                            status=status.HTTP_200_OK)
        else:
            return Response({'action': "Order Marked", 'message': "Wrong Password",
                             },
                            status=status.HTTP_401_UNAUTHORIZED)
    except Http404:
        return Response({'action': "Order Marked", 'message': "Not Found", },
                        status=status.HTTP_404_NOT_FOUND)
    except:
        print("Unexpected error:", sys.exc_info())
        return Response({'action': "Order Marked", 'message': "Something Went Wrong!"},
                        status=status.HTTP_400_BAD_REQUEST)
