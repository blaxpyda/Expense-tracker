from django.contrib import admin
from .models import Income, Expense, Goal, UserProfile, Category
# Register your models here.

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Goal)
admin.site.register(UserProfile)
admin.site.register(Category)

