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

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location','job_summary', 'start_date', 'end_date','updated_date', 'created_date']
    search_fields =['company_name', 'job_title', 'job_location','job_summary']
    list_editable = ['company_name', 'job_title', 'job_location','job_summary', 'start_date', 'end_date']
    class Meta:
        model = Experience

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'major', 'department','education_summary', 'start_date', 'end_date', 'updated_date' , 'created_date']
    search_fields =['school_name', 'major', 'department','education_summary']
    list_editable = ['school_name', 'major', 'department', 'start_date', 'end_date','education_summary']
    class Meta:
        model = Education


@admin.register(My_Community)
class My_CommunityAdmin(admin.ModelAdmin):
    list_display = ['id', 'community_tag', 'community_name', 'community_place','community_start_date', 'community_end_date','updated_date', 'created_date']
    search_fields = ['community_tag', 'community_name', 'community_place']
    list_editable = ['community_tag', 'community_name', 'community_place','community_start_date', 'community_end_date']

    class Meta:
        model = My_Community


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter','updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter',]
    list_editable = [ 'description', 'parameter']

    class Meta:
        model = Certificate



