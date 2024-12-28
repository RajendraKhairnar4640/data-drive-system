from django.contrib import admin
from .models import Folder 

# Register the Folder model
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'owner')  # Fields to display in the list view
    search_fields = ('name', 'owner__username')  # Add a search filter for name and owner
    list_filter = ('parent', 'owner')  # Add filters for parent folder and owner


# Register the models with the custom admin classes
admin.site.register(Folder, FolderAdmin)
