from django.contrib import admin
from .models import Comment
from .models import Posts
from .models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserManager

# Register your models here.
class MyUserAdmin(BaseUserManager):
    list_display=('email','Uname','phone','date_joined','last_login','is_admin','is_active')
    search_fields=('email','Uname')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','Uname','phone','age','country','password1','password2'),
        }),
    )

    ordering=('email',)


admin.site.register(Comment)
admin.site.register(Posts)
admin.site.register(MyUser,MyUserAdmin)