# -*- coding: utf-8 -*-

from datetime import datetime
from unittest import mock

from django.test import TestCase

from orders.models import Order
from orders.tasks import create_order


class SimpleTest(TestCase):

    @mock.patch('orders.tasks.datetime', )
    def test_create_order(self, mock_datetime,):
        mock_datetime.now.return_value = datetime(2021, 2, 1, )
        with mock.patch('orders.tasks.get_number', mock.Mock(return_value=1)):
            create_order('test,test,', 2.50)
            order = Order.objects.order_by('-id').first()
            self.assertEqual(order.order_number, '20210201-00001')
        with mock.patch('orders.tasks.get_number', mock.Mock(return_value=2)):
            create_order('test,test,', 2.50)
            order = Order.objects.order_by('-id').first()
            self.assertEqual(order.order_number, '20210201-00002')
