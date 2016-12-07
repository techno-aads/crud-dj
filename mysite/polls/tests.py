import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Order


class OrderMethodTests(TestCase):

    def test_was_ordered_recently_with_future_order(self):
        """
        was_ordered_recently() should return False for orders whose
        date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_order = Order(date=time)
        self.assertIs(future_order.was_ordered_recently(), False)

    def test_was_ordered_recently_with_old_order(self):
        """
        was_ordered_recently() should return False for orders whose
        date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_order = Order(date=time)
        self.assertIs(old_order.was_ordered_recently(), False)

    def test_was_ordered_recently_with_recent_order(self):
        """
        was_ordered_recently() should return True for orders whose
        date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_order = Order(date=time)
        self.assertIs(recent_order.was_ordered_recently(), True)