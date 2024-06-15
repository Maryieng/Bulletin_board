from django.contrib import admin

from announcement.models import Announcement, Review


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'author', 'created_at', 'image',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at',)
