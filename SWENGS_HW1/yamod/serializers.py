from rest_framework import serializers

from SWENGS_HW1.yamod.models import Student, Building


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "birthdate", "studies"]

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ["id", "address", "postal_code", "city", "color"]