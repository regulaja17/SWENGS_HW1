from django.contrib import admin

from SWENGS_HW1.yamod.models import Student, Building


class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birthdate", "studies")
    search_fields = ["first_name", "last_name", "studies"]
admin.site.register(Student, StudentAdmin)

class BuildingAdmin(admin.ModelAdmin):
    list_display = ("address", "postal_code", "city", "color")
    search_fields = ["address", "postal_code", "city"]
admin.site.register(Building, BuildingAdmin)