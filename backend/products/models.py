from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.utils import timezone

# 1. Product 
class Product(models.Model):
    title = models.CharField(max_length=255)  
    url = models.URLField(unique=True)      
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    currency = models.CharField(max_length=10, default='THB')    
    last_updated = models.DateTimeField(auto_now=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 2. Subscriber 
class Subscriber(models.Model):
    email = models.EmailField(unique=True)            
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)     
    unsubscribe_token = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )  # Token

    def __str__(self):
        return self.email


# 3. Subscription 
class Subscription(models.Model):
    subscriber = models.ForeignKey(
        Subscriber, on_delete=models.CASCADE, related_name='subscriptions'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='subscriptions'
    )
    target_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  
    notify_when_lower = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    last_notified = models.DateTimeField(null=True, blank=True)  

    class Meta:
        unique_together = ('subscriber', 'product') 

    def __str__(self):
        return f"{self.subscriber.email} subscribes {self.product.title}"


# 4. (Optional) Price History -
class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='price_history'
    )
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    changed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.title}: {self.old_price} -> {self.new_price}"
