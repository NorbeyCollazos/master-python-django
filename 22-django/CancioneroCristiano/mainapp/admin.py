from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import *

#para configurar el panel de administracion
class PageAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre',)

class PageAdminCanciones(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':120, 'cols':80, 'class': 'textarea_cancion'})},
    }

    search_fields = ('titulo','cancion','artista')
    list_display = ('titulo', 'artista')
    list_filter = ('artista',)
    ordering = ('titulo',)
     

# Register your models here.
admin.site.register(Artistas, PageAdmin)
admin.site.register(Canciones, PageAdminCanciones)

