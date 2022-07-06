from django.contrib import admin

from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'text', 'rating']


admin.site.register(Review, ReviewAdmin)
