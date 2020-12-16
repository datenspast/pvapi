from django.contrib import admin
from .models import YieldPerKwp

class YieldPerKwpAdmin(admin.ModelAdmin):
    pass

admin.site.register(YieldPerKwp, YieldPerKwpAdmin)
