from django.db import models


class Region(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region_name = models.CharField(max_length=255)


class UserType(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    is_individual_person = models.BooleanField()


class QuestionType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
