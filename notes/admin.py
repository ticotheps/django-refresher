from django.contrib import admin

# Tells our admin portal which tables we're interested in seeing
#   at http://localhost:8000/admin
from .models import Note

# Registers the 'Note' model with the admin portal
admin.site.register(Note)
