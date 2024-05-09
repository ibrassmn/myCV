from django.shortcuts import render
from myCV.models import GeneralSetting
# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    about_myself_footer = GeneralSetting.objects.get(name="about_myself_footer").parameter
    about_myself_about_section = GeneralSetting.objects.get(name="about_myself_about_section").parameter

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'about_myself_footer': about_myself_footer,
        'about_myself_about_section': about_myself_about_section,




    }
    return render(request, 'index.html', context=context)

