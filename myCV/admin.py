from django.contrib import admin
from myCV.models import *
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields =['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields =['name', 'description', 'file']
    list_editable = ['description', 'file']
    class Meta:
        model = ImageSetting


@admin.register(SkillLeft)
class SkillLeftAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields =['name',]
    list_editable = ['order', 'name', 'percentage']
    class Meta:
        model = SkillLeft

@admin.register(SkillRight)
class SkillRightAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields =['name',]
    list_editable = ['order', 'name', 'percentage']
    class Meta:
        model = SkillRight

@admin.register(ExperienceLeft)
class ExperienceLeftAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date','updated_date', 'created_date']
    search_fields =['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']
    class Meta:
        model = ExperienceLeft



