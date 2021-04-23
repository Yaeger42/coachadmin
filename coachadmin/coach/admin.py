from django.contrib import admin
from coach.models import Coach
# Register your models here.

@admin.register(Coach)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'phoneNumber', 'firstName', 'lastName', 'phone')
    list_display_links = ('pk', 'email', 'phoneNumber', 'firstName', 'lastName', 'phone')

    search_fields = ('coach__email', 'coach__phoneNumber', 'coach__firstName', 'coach__lastName')

    list_filter = (
        'coach__is_active',
        'coach__is_staff',
        'created',
        'lastUpdated'
    )


admin.site.unregister(Coach)
admin.site.register(Coach)