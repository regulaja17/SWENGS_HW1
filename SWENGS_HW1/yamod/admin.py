from django.contrib import admin

from SWENGS_HW1.yamod.models import Student


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)