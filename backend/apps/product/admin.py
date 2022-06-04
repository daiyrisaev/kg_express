from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from .models import *
from django.forms import ModelForm,CharField

from django.forms import ModelForm, CharField, widgets


class ProductAdminForm(ModelForm):
    description = CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    prepopulated_fields = {"slug": ('name',)}


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('name','category', 'slug', 'id')
    prepopulated_fields = {"slug":('name',)}
    list_filter = ('category',)
    search_fields = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'category', 'subcategory', 'created', 'updated', 'price']


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ['name','add_link','image','created_at','updated']
    list_filter = ['created_at']