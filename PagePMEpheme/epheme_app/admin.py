from django.contrib import admin
from .models import Video, Category
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'author', 'date', 'category_name')
    list_filter = ('date', 'category_name')
    search_fields = ('title', 'author', 'description', 'tags')
    date_hierarchy = 'date'
    ordering = ('-date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'description', 'video_url', 'thumbnail_url', 'date', 'tags', 'category_name')
        }),
    )
class CategoryAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','id')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name','slug')
        }),
    )
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)