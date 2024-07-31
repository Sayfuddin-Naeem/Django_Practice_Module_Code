from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

class Medium(models.Model):
    auto_field  = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    email_field = models.EmailField()
    url_field = models.URLField()
    time_field = models.TimeField()
    small_integer_field = models.SmallIntegerField()
    slug_field = models.SlugField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    json_field = models.JSONField()
    integer_field = models.IntegerField()
    generic_ip_address_field = models.GenericIPAddressField()
    
    # def __str__(self) -> str:
    #     return f"Name : {self.name}"
    

def comma_separated_validator(value):
    if not re.match(r'^(\w+,)*\w+$', value):
        raise ValidationError('Enter values separated by commas.')
    
class Medium2(models.Model):
    big_auto_field = models.BigAutoField(primary_key=True)
    binary_field = models.BinaryField()
    comma_separated_field = models.CharField(
        validators=[comma_separated_validator],
        max_length=255
    )
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='upload/')
    file_path_field = models.FilePathField(path='upload/')
    uuid_field = models.UUIDField()
    text_field = models.TextField()
    float_field = models.FloatField()
    positive_integer_field = models.PositiveIntegerField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    image_field = models.ImageField(upload_to='upload/')
    # one_to_one_field = models.OneToOneField(Medium, on_delete=models.CASCADE)
    # many_to_many_field = models.ManyToManyField(Medium)
    foreign_key = models.ForeignKey(Medium, on_delete=models.CASCADE)
    
    