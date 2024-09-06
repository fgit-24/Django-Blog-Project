from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, EmailValidator
from django.utils import timezone

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return self.user.username

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        validators=[EmailValidator()],
        error_messages={
            'invalid': 'Enter a valid email address.'
        }
    )
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email