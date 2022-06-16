from django.db import models
import datetime


class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    massage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject


class Category(models.Model):
    name = models.TextField(max_length=200)
    slug = models.SlugField(max_length=40)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug


class Projects (models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    stack = models.CharField(max_length=50)
    link=models.URLField(max_length = 200,blank=True)
    githublink = models.URLField(max_length = 200,blank=True)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self) -> str:
        return self.name


class Feedback (models.Model):
    name = models.CharField(max_length=50)
    project_comment = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True)
    from_where = models.CharField(max_length=50)
    massage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.massage
