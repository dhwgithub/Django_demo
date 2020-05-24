from django.contrib import admin
from app1.models import Person, Order


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at', 'updated_at')
    list_filter = ('first_name', 'last_name')  # 设置过滤器
    search_fields = ('first_name',)  # 设置搜索项
    readonly_fields = ('first_name', 'created_at', 'updated_at')  # 设置只读项

admin.site.register(Person, PersonAdmin)
