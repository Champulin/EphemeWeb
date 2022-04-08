from django.contrib import admin
from .models import Video, Category, Source
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
            'fields': ('title', 'author', 'description', 'video_url', 'source_name', 'thumbnail_url', 'date', 'tags', 'category_name','home')
        }),
    )
class CategoryAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','id','description')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name','slug','alphabetic_order','description')
        }),
    )
    prepopulated_fields = {'slug': ('name',)}
class SourceAdmin(admin.ModelAdmin):
    pass
    list_display = ('name','id')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
admin.site.register(Source, SourceAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)