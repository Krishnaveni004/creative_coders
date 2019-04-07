from django.contrib import admin
from .models import Test_Form,ContactForm, Newsletter,DataVirtualizationForm
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Test_Form)
@admin.register(ContactForm)
@admin.register(Newsletter)
@admin.register(DataVirtualizationForm)
class PersonAdmin(ImportExportModelAdmin):
    pass;
