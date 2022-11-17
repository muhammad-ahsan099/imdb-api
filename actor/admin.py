from django.contrib import admin
from actor.models import Celebrity, CelebrityRole

# Register your models here.


# admin.site.register(CelebrityRole)
# admin.site.register(Celebrity)
# @admin.register(CelebrityDetail)

@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rank', 'gender', 'dob',
                    'height', 'is_married']

@admin.register(CelebrityRole)
class CelebrityRoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'celebrity', 'movie', 'director', 'writer', 'producer', 'actor']
