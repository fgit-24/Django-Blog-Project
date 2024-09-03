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


class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        validators=[EmailValidator()],
        unique=True,
        error_messages={
            'unique': 'A subscriber with this email address already exists.'
        }
    )
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email