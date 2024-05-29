from django.contrib import admin
from . import models

admin.site.register(models.Word)
admin.site.register(models.Category)
admin.site.register(models.Question)
admin.site.register(models.TestResult)

