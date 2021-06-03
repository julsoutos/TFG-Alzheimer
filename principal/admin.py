from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Solution)
admin.site.register(Activity_Result)
admin.site.register(Training)
admin.site.register(Activity_Training)
admin.site.register(Patient_training)
admin.site.register(Mental_Test)
admin.site.register(Test_Result)