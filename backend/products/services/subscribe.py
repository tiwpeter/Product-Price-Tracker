from ..models import Subscriber, Subscription, Product
from django.core.mail import send_mail

def subscribe(email, product_url, target_price=None):
    # 1. Get or create subscriber
    subscriber, created = Subscriber.objects.get_or_create(email=email)
    
    # 2. Get product
    product = Product.objects.get(url=product_url)
    
    # 3. Create subscription (if not exists)
    sub, _ = Subscription.objects.get_or_create(
        subscriber=subscriber,
        product=product,
        defaults={'target_price': target_price}
    )
    
    # 4. Send confirmation / email alert setup
    send_subscription_email(sub)
    return sub

def send_subscription_email(subscription):
    unsubscribe_link = f"https://tracker.com/unsubscribe/{subscription.subscriber.unsubscribe_token}/"
    message = f"คุณติดตามสินค้า {subscription.product.title} แล้ว\nยกเลิก: {unsubscribe_link}"
    send_mail(
        subject=f"[Tracker] ติดตามสินค้า {subscription.product.title}",
        message=message,
        from_email="noreply@tracker.com",
        recipient_list=[subscription.subscriber.email]
    )
