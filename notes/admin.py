from django.contrib import admin

# Tells our admin portal which tables we're interested in seeing
#   at http://localhost:8000/admin
from .models import (Note, PersonalNote)

# Allows read-only fields to show up in admin portal
class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Registers the 'Note' model with the admin portal
admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, NoteAdmin)