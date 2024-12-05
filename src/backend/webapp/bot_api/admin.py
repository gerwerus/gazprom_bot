from django.contrib import admin
from .models import Region, UserType, QuestionType, Answer


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "region_name")
    search_fields = ("region_name",)


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "is_individual_person")
    list_filter = ("region", "is_individual_person")
    search_fields = ("id",)


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    search_fields = ("type",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "user_type", "question_type", "text")
    list_filter = ("user_type", "question_type")
    search_fields = ("text",)
