from django.contrib import admin

from .models import Student, Teacher, StudentTeachers


class StudentTeachersInline(admin.TabularInline):
    model = StudentTeachers
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "group"]
    list_filter = ['group']
    inlines = [StudentTeachersInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "subject"]
    list_filter = ['subject']
    inlines = [StudentTeachersInline]
