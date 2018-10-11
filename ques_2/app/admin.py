from django.contrib import admin
from .models import Pincode, State,City,Profile
# Register your models here.

admin.site.register(Pincode)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Profile)