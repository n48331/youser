from msilib.schema import Class
from unicodedata import name
from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from accounts.models import City

# Create your models here.
POST_TYPE = (
    ('ad', 'Ad'),
    ('event', 'Event'),
)


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pics/docs/",
                              default="pics/default.jpg")
    type = models.CharField(max_length=6, choices=POST_TYPE, default='ad')
    desc = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by_name = models.CharField(max_length=255,
                                       default=None, blank=True, null=True)
    location_city = models.CharField(max_length=255,
                                     default=None, blank=True, null=True)

    def __str__(self):
        return self.title+' || ' + self.type
