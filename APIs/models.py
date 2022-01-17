from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)

    order_id = models.CharField(max_length=100, blank=False)
    payment_id = models.CharField(max_length=100, blank=False)

    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=False)
    product_size = models.CharField(max_length=50, choices=[('XS', ' Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'),
                                                            ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large')],
                                    blank=False)

    address = models.CharField(max_length=150, blank=False, default=None, null=True)

    order_date_time = models.DateTimeField(blank=False, default=None, null=True)
    order_status = models.CharField(max_length=100, blank=False, choices=[('Confirmed', 'Confirmed'),
                                                                          ('Cancelled', 'Cancelled'),
                                                                          ('Delivered', 'Delivered'),
                                                                          ('Shipped', 'Shipped')])

    def __str__(self):
        return str(self.order_id)
