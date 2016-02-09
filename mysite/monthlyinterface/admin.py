from django.contrib import admin

# Register your models here.
from .models import Creation
from .models import Desired_Format
from .models import Material

admin.site.register(Creation)
admin.site.register(Desired_Format)
admin.site.register(Material)
