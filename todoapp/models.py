from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

class Profile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=30, null=True,default='')
    Mobile = models.CharField(max_length=10, null=True,default='')
    State = models.CharField(max_length=25, null=True,default='')
    City= models.CharField(max_length=25, null=True,default='')
    Address= models.CharField(max_length=150, null=True,default='')

    class Meta:
        db_table = 'profile'

