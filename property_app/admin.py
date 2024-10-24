from django.contrib import admin

from property_app.models import Property,Units,Agreement,Renter

# register
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    @admin.register(Units)
    class UnitsAdmin(admin.ModelAdmin):
        @admin.register(Renter)
        class RenterAdmin(admin.ModelAdmin):
            @admin.register(Agreement)
            class AgreementAdmin(admin.ModelAdmin):
                list_display = ('renter','unit','start_date','end_date')