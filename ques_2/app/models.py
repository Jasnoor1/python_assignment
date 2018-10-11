from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250, null=False,blank=False)
    state = models.ForeignKey(State,on_delete=models.CASCADE, related_name='city')

    def __str__(self):
        return self.name

class Pincode(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='pincode')

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length= 200, null=False, blank=False)
    state = models.ForeignKey(State, related_name='profile_state', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='profile_state', on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode, related_name='profile_pincode', on_delete=models.CASCADE)

    def __str__(self):
        return self.name