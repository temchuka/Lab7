from django.contrib import admin
from .models import Lease


class LeaseAdmin(admin.ModelAdmin):
    list_display = ('contract', 'outlet', 'tenant', 'start_date', 'end_date', 'get_cost', 'get_excerpt')


admin.site.register(Lease, LeaseAdmin)
