from django.test import TestCase
from unittest.mock import patch
from products.services.subscribe import send_subscription_email, subscribe
from .models import Subscriber, Product, Subscription

class SubscriptionServiceTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="Test Product",
            url="http://example.com/product",
            price=100
        )
        self.email = "user@example.com"

    # Patch ต้องชี้ไปที่โมดูลที่ใช้ send_mail จริง ๆ คือ subscribe.py
    @patch('products.services.subscribe.send_mail')
    def test_subscribe_creates_subscriber_and_subscription(self, mock_send_mail):
        subscription = subscribe(self.email, self.product.url, target_price=90)
        subscriber = Subscriber.objects.get(email=self.email)
        self.assertTrue(subscriber.is_active)
        self.assertIsNotNone(subscriber.unsubscribe_token)
        self.assertTrue(Subscription.objects.filter(subscriber=subscriber, product=self.product).exists())
        self.assertEqual(subscription.target_price, 90)
        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args
        self.assertIn(self.email, kwargs['recipient_list'])
        self.assertIn("Test Product", kwargs['subject'])

    @patch('products.services.subscribe.send_mail')
    def test_send_subscription_email_generates_unsubscribe_link(self, mock_send_mail):
        subscriber = Subscriber.objects.create(email=self.email)
        subscription = Subscription.objects.create(
            subscriber=subscriber,
            product=self.product,
            target_price=90
        )
        send_subscription_email(subscription)
        mock_send_mail.assert_called_once()
        args, kwargs = mock_send_mail.call_args
        message = kwargs['message']
        self.assertIn(str(subscriber.unsubscribe_token), message)
        self.assertIn("ยกเลิก", message)
