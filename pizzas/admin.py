from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, Comment

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'pizza', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)