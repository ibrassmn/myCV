from django.shortcuts import render
from myCV.models import GeneralSetting, ImageSetting


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    about_myself_footer = GeneralSetting.objects.get(name="about_myself_footer").parameter
    about_myself_title = GeneralSetting.objects.get(name="about_myself_title").parameter
    about_myself_about_section = GeneralSetting.objects.get(name="about_myself_about_section").parameter
    about_myself_about_section_1 = GeneralSetting.objects.get(name="about_myself_about_section_1").parameter
    about_myself_about_section_long = GeneralSetting.objects.get(name="about_myself_about_section_long").parameter
    skills_section = GeneralSetting.objects.get(name="skills_section").parameter
    resume_section_0 = GeneralSetting.objects.get(name="resume_section_0").parameter
    certificate_section = GeneralSetting.objects.get(name="certificate_section").parameter

    # Images

    about_photo = ImageSetting.objects.get(name="about_photo").file




    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'about_myself_footer': about_myself_footer,
        'about_myself_about_section': about_myself_about_section,
        'about_myself_about_section_1': about_myself_about_section_1,
        'about_myself_about_section_long': about_myself_about_section_long,
        'about_myself_title': about_myself_title,
        'skills_section': skills_section,
        'resume_section_0': resume_section_0,
        'certificate_section': certificate_section,
        'about_photo': about_photo,



    }
    return render(request, 'index.html', context=context)

