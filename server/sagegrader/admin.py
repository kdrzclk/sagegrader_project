from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Institution, User

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("inst_name", "inst_city", "inst_state_code", "inst_country")
    search_fields = ("inst_name",)
    list_per_page = 20

class CustomUSerAdmin(UserAdmin):
    model = User
    list_display = ('email', 'institutions', 'first_name', 'last_name', 'user_role', 'is_staff', 'user_is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'user_is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Personel Info', {'fields':(
            'institutions', 'first_name', 'last_name', 'user_role','user_is_active')}),
        ('Permissions', {'fields':('groups',
        'user_permissions', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'user_is_active', 'is_superuser')
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(Institution, InstitutionAdmin)
admin.site.register(User, CustomUSerAdmin)