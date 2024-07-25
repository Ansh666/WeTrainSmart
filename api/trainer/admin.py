# trainer/admin.py
# from django.contrib import admin
# from api.user.models import CustomUser

# class TrainerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'gender', 'role', 'is_active', 'created_at')
#     search_fields = ('email', 'name')
#     list_filter = ('role', 'is_active')

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         return queryset.filter(role='trainer')

# # No need to register CustomUser again; it's already registered in the user app.
# # We are only creating a custom admin view to filter trainers.
# admin.site.register(CustomUser, TrainerAdmin)


# from django.contrib import admin
# from .models import Trainer

# admin.site.register(Trainer)

# from django.contrib import admin
# from .models import Trainer

# @admin.register(Trainer)
# class TrainerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'password', 'gender', 'dob', 'contact_no', 'state', 'domain']
#     search_fields = ['user__email', 'name']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Trainer

class TrainerAdmin(BaseUserAdmin):
    list_display = ('name', 'email', 'gender', 'dob', 'contact_no', 'state', 'domain')
    search_fields = ('name', 'email')
    ordering = ('name',)
    list_filter = ('domain', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'gender', 'dob', 'contact_no', 'state', 'domain')}),
        ('Permissions', {'fields': ( 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'gender', 'dob', 'contact_no', 'state', 'domain',
                       
                    #    'is_active', 'is_superuser', 'groups', 'user_permissions'
                       )}
        ),
    )
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(Trainer, TrainerAdmin)
