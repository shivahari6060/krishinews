from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Articles)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Subsector)
admin.site.register(NewsComment)
