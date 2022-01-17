import csv

from django.shortcuts import get_object_or_404

from APIs.models import Order, Product

import datetime

def CleanOrders():
    Order.objects.all().delete()

def addOrders():
    try:
        with open('IIT Dh Merch-final.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['payment status'] == 'captured':
                    order = Order(
                        name=row['name'],
                        email=row['email'],
                        phone=row['phone'],
                        order_id=row['order_id'],
                        payment_id=row['payment id'],
                        order_status='Confirmed',
                        # 19/12/2021 18:20:56 convert to datetime
                        order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                        # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                    )
                    if row['item name'] == 'HB':
                        order.product = get_object_or_404(Product, id='HB')
                        order.product_size = row['hb_size']
                    elif row['item name'] == 'TW':
                        order.product = get_object_or_404(Product, id='TW')
                        order.product_size = row['tw_size']
                    elif row['item name'] == 'TR':
                        order.product = get_object_or_404(Product, id='TR')
                        order.product_size = row['tr_size']
                    elif row['item name'] == 'TB20':
                        order.product = get_object_or_404(Product, id='TB20')
                        order.product_size = row['tb20_size']
                    elif row['item name'] == 'TB21':
                        order.product = get_object_or_404(Product, id='TB21')
                        order.product_size = row['tb21_size']
                    else:
                        continue
                        # raise Exception('Invalid product name')

                    order.save()

    except Exception as e:
        print(e)

# generate random order id
def generateOrderId():
    import random
    import string

    order_id = ''
    for i in range(0, 10):
        order_id += random.choice(string.ascii_letters)
    return order_id

def addOrdersCash():
    try:
        with open('IITDh Merchandise - Form Responses 1.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                    orderID = "order_" + generateOrderId()
                    paymentID = "pay_" + generateOrderId()

                    if row['T Shirts'] is not None:
                        if row['T Shirts'] == 'HB 21 (Black) Rs. 599':
                            order = Order(
                                name=row['Name'],
                                email=row['Email'],
                                phone=row['Phone Number'],
                                order_id=orderID,
                                payment_id=paymentID,
                                order_status='Confirmed',
                                # 12/26/2021 11:06:23 convert to datetime
                                order_date_time=datetime.datetime.strptime(row['Timestamp'], '%m/%d/%Y %H:%M:%S'),

                                # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                            )
                            order.product = get_object_or_404(Product, id='TB21')
                            order.product_size = row['T Shirt Size']
                            order.save()
                        elif row['T Shirts'] == 'HW (White) Rs. 529':
                            order = Order(
                                name=row['Name'],
                                email=row['Email'],
                                phone=row['Phone Number'],
                                order_id=orderID,
                                payment_id=paymentID,
                                order_status='Confirmed',
                                # 12/26/2021 11:06:23 convert to datetime
                                order_date_time=datetime.datetime.strptime(row['Timestamp'], '%m/%d/%Y %H:%M:%S'),
                            )
                            order.product = get_object_or_404(Product, id='TW')
                            order.product_size = row['T Shirt Size']
                            order.save()

                    if row['Hoodie'] == 'Ordered':
                        order = Order(
                            name=row['Name'],
                            email=row['Email'],
                            phone=row['Phone Number'],
                            order_id=orderID,
                            payment_id=paymentID,
                            order_status='Confirmed',
                            # 12/26/2021 11:06:23 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['Timestamp'], '%m/%d/%Y %H:%M:%S'),
                        )
                        order.product = get_object_or_404(Product, id='HB')
                        order.product_size = row['Hoodie Size']
                        order.save()



    except Exception as e:
        print(e)

def addOrdersDelivery():
    try:
        with open('IITDh Merch Delivery.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['payment status'] == 'captured':
                    if row['item name'] == '2 TEE RW Combo':
                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                            # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                        )
                        order.product = get_object_or_404(Product, id='TR')
                        order.product_size = row['t_shirt_size']
                        order.save()

                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                            # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                        )
                        order.product = get_object_or_404(Product, id='TW')
                        order.product_size = row['t_shirt_size']
                        order.save()

                    elif row['item name'] == '3 TEE Combo':
                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                            # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                        )
                        order.product = get_object_or_404(Product, id='TR')
                        order.product_size = row['t_shirt_size']
                        order.save()

                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                            # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                        )
                        order.product = get_object_or_404(Product, id='TW')
                        order.product_size = row['t_shirt_size']
                        order.save()

                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),

                            # order_date_time = datetime.strftime(row['payment date'], '%d/%m/%Y %H:%M:%S')
                        )
                        order.product = get_object_or_404(Product, id='TB21')
                        order.product_size = row['t_shirt_size']
                        order.save()

                    elif row['item name'] == 'HB':
                        order = Order(
                            name=row['name'],
                            email=row['email'],
                            phone=row['phone'],
                            order_id=row['order_id'],
                            payment_id=row['payment id'],
                            order_status='Confirmed',
                            address=row['address'],
                            # 19/12/2021 18:20:56 convert to datetime
                            order_date_time=datetime.datetime.strptime(row['payment date'], '%d/%m/%Y %H:%M:%S'),
                        )
                        order.product = get_object_or_404(Product, id='HB')
                        order.product_size = row['hoodie_size']
                        order.save()
                    else:
                        continue
                        # raise Exception('Invalid product name')

                    order.save()

    except Exception as e:
        print(e)

# git remote set-url origin https://gowtham3105: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@github.com/gowtham3105/iitdh-merch

def run():
    # CleanOrders()
    # addOrders()
    # addOrdersCash()
    # addOrdersDelivery()
    print("Done")
