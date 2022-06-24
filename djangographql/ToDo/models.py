from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

class Todo(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    Description = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    status = models.BooleanField()
    date_completed = models.DateField(null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title