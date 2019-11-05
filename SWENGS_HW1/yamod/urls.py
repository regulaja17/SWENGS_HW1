from django.urls import path

from SWENGS_HW1.yamod import views

urlpatterns = [
    path("students", views.student_list),
    path("students/<int:id>", views.student_adapt),
    path("buildings", views.building_list),
    path("buildings/<int:id>", views.building_adapt)
]