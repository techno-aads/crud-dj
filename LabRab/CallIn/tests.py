import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Telecast
from django.urls import reverse


def create_telecast(tel_name, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Telecast.objects.create(question_text=tel_name,
                                   tel_date=time, tel_descr="null")


class TelecastMethodTests(TestCase):
    def test_was_published_recently_with_future_telecast(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_telecast = Telecast(tel_date=time)
        self.assertIs(future_telecast.was_pub(), False)

    def test_was_published_recently_with_old_telecast(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_telecast = Telecast(tel_date=time)
        self.assertIs(old_telecast.was_pub(), False)

    def test_was_published_recently_with_recent_telecast(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_telecast = Telecast(tel_date=time)
        self.assertIs(recent_telecast.was_pub(), True)


class TelecastViewTests(TestCase):
    def test_index_view_with_no_telecast(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('CallIn:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No telecasts are available.")
        self.assertQuerysetEqual(response.context['latest_telecast_list'], [])

    def test_index_view_with_a_past_telecast(self):

        create_telecast(tel_name="Past telecast.", days=-30)
        response = self.client.get(reverse('CallIn:index'))
        self.assertQuerysetEqual(
            response.context['latest_telecast_list'],
            ['<Telecast: Past telecast.>']
        )

    def test_index_view_with_a_future_telecast(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_telecast(tel_name="Future telecast.", days=30)
        response = self.client.get(reverse('CallIn:index'))
        self.assertContains(response, "No telecast are available.")
        self.assertQuerysetEqual(response.context['latest_telecast_list'], [])

    def test_index_view_with_future_telecast_and_past_telecast(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_telecast(tel_name="Past telecast.", days=-30)
        create_telecast(tel_name="Future telecast.", days=30)
        response = self.client.get(reverse('CallIn:index'))
        self.assertQuerysetEqual(
            response.context['latest_telecast_list'],
            ['<Telecast: Past telecast.>']
        )

    def test_index_view_with_two_past_telecast(self):
        """
        The questions index page may display multiple questions.
        """
        create_telecast(tel_name="Past telecast 1.", days=-30)
        create_telecast(tel_name="Past telecast 2.", days=-5)
        response = self.client.get(reverse('CallIn:index'))
        self.assertQuerysetEqual(
            response.context['latest_telecast_list'],
            ['<Telecast: Past telecast 2.>', '<Telecast: Past telecast 1.>']
        )

class TelecastIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_telecast(self):

        future_telecast = create_telecast(tel_name='Future telecast.', days=5)
        url = reverse('CallIn:detail', args=(future_telecast.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_telecast(self):

        past_telecast = create_telecast(tel_name='Past telecast.', days=-5)
        url = reverse('CallIn:detail', args=(past_telecast.id,))
        response = self.client.get(url)
        self.assertContains(response, past_telecast.tel_name)