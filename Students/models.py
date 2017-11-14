from django.db import models


# Create your models here.
class Student(models.Model):
    YEAR_CHOICES = (
        ('1', 'FIRST YEAR'),
        ('2', 'SECOND YEAR'),
        ('3', 'THIRD YEAR'),
        ('4', 'FOURTH YEAR'),
    )

    HOSTEL_NAME = (
        ('Y', 'YASHODHARA BHAVAN'),
        ('K', 'KALPANA BHAVAN'),
        ('V', 'VRINDAVAN BHAVAN'),
        ('S', 'SAKET BHAVAN'),
        ('P', 'PANCHAVATI BHAVAN'),
        ('J', 'JAYBHARAT BHAVAN'),
    )

    roll_no = models.IntegerField(primary_key= True)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    email_id = models.EmailField(max_length= 30)
    mobile_number = models.IntegerField(unique= True)
    year = models.CharField(max_length=1, choices= YEAR_CHOICES)
    hostel_name = models.CharField(max_length= 1, choices= HOSTEL_NAME)