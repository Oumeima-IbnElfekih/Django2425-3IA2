from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
# Create your models here.

def validate_letters_only(value):
    if not re.match(r'^[A-Za-z\s]+$',value):
        raise ValidationError('This field should only contain letters')



class Category(models.Model):
    letters_only=RegexValidator(r'^[A-Za-z\s]+$','Only letters are allowed')
    title=models.CharField(max_length=255, validators=[validate_letters_only]) 
    created_at= models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
        return f"category title = {self.title}"
    