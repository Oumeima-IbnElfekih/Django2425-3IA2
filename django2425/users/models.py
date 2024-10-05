from django.db import models
from django.contrib.auth.models import AbstractUser
from conferences.models import Conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
def email_validator(value):
    if not value.endswith('@esprit.tn') :
        raise ValidationError('Email Invalid , only @esprit.tn domain are allowed')
class Participant(AbstractUser):
    cin_validator= RegexValidator(
        regex=r'^\d{8}$',
        message="This field mush contain excatly 8 digits"
    )
    cin= models.CharField(primary_key=True,max_length=8,validators=[cin_validator] )
    email= models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255, unique=True)
    USERNAME_FIELD='username'
    CHOICES=(
        ('etudiant','etudiant'),
        ('chercheur','chercheur'),
        ('docteur','docteur'),
        ('enseignant','enseignant'),
    )
    participant_category= models.CharField(max_length=255, choices=CHOICES)
    reservations = models.ManyToManyField(Conference,
                                          through='Reservation',
                                          related_name='reservations')
    created_at= models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)



class Reservation(models.Model):
    conference= models.ForeignKey(Conference,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
    confirmed=models.BooleanField(default=False)
    reservation_date=models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.conference.start_date < timezone.now().date():
            raise ValidationError('you can only reserve for upcomming conference')
        reservation_count=Reservation.objects.filter(
            participant=self.participant,
            reservation_date=self.reservation_date
        )
        if reservation_count >= 3:
            raise ValidationError("You can only make up to 3 reservations per day")
    class Meta:
        unique_together=('conference','participant')
        verbose_name_plural="Reservations"