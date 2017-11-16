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
    email_id = models.EmailField(max_length= 30, blank= True)
    mobile_number = models.IntegerField(unique= True)
    year = models.CharField(max_length=1, choices= YEAR_CHOICES)
    hostel_name = models.CharField(max_length= 1, choices= HOSTEL_NAME)

    def __str__(self):
        return ("%s %s" % (self.first_name, self.last_name))



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return  self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #add a boolean attribute to check if it is a correct-choice
    is_correct_choice = models.BooleanField(default= True)

    def __str__(self):
        return self.choice_text

