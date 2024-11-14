from django.contrib import admin
from .models import Client, Review, Property, CompanyInfo, FAQ
from django import forms
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
import django.contrib.humanize

# Register your models here.

class MyAdminSite(admin.AdminSite):
    site_header = 'Административная панель'
    site_title = "Мой сайт администрирования"
    index_title = "Добро пожаловать в панель администратора"

admin.site = MyAdminSite()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('surname', 'name', 'phone', 'email', 'property', 'created_at')
    list_filter = ('created_at','city',)
    search_fields = ('name', 'phone', 'email','created_at','city')
    ordering = ['surname']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm
    list_display = ('name', 'rating', 'comment', 'email','created_at')
    list_filter = ('created_at',)
    search_fields = ('created_at',)
    ordering = ['created_at']



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm
    list_display = ('adress', 'price', 'city', 'rooms', 'floor')
    search_fields = ('adress', 'city')
    list_filter = ('city',)
    ordering = ['city']

admin.site.register(Client, ClientAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(CompanyInfo)
admin.site.register(FAQ)
