from django.shortcuts import render
from myCV.models import GeneralSetting, ImageSetting, SkillRight, SkillLeft, Experience, Education,My_Community,Certificate

# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameter
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameter
    site_description = GeneralSetting.objects.get(name="site_description").parameter
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameter
    about_myself_footer = GeneralSetting.objects.get(name="about_myself_footer").parameter
    about_myself_title = GeneralSetting.objects.get(name="about_myself_title").parameter
    about_myself_city = GeneralSetting.objects.get(name = "about_myself_city").parameter
    about_myself_country = GeneralSetting.objects.get(name = "about_myself_country").parameter
    about_freelance_section = GeneralSetting.objects.get(name="about_freelance_section").parameter
    about_degree_section = GeneralSetting.objects.get(name="about_degree_section").parameter
    about_myself_about_section = GeneralSetting.objects.get(name="about_myself_about_section").parameter
    about_myself_about_section_1 = GeneralSetting.objects.get(name="about_myself_about_section_1").parameter
    about_myself_about_section_long = GeneralSetting.objects.get(name="about_myself_about_section_long").parameter
    skills_section = GeneralSetting.objects.get(name="skills_section").parameter
    resume_section_0 = GeneralSetting.objects.get(name="resume_section_0").parameter
    certificate_section = GeneralSetting.objects.get(name="certificate_section").parameter

    # Images

    about_photo = ImageSetting.objects.get(name="about_photo").file


    #Skills

    skills_left =SkillLeft.objects.all().order_by("order")
    skills_right = SkillRight.objects.all().order_by("order")

    #Experiences

    experiences = Experience.objects.all().order_by('-start_date')

    #Education

    educations = Education.objects.all().order_by('-start_date')

    #Community

    communities = My_Community.objects.all().order_by('community_name')

    #Certificate

    sql_name = Certificate.objects.get(name="sql_name").parameter
    sql_text = Certificate.objects.get(name="sql_text").parameter
    tech_summit = Certificate.objects.get(name="tech_summit").parameter
    tech_summit_text = Certificate.objects.get(name="tech_summit_text").parameter
    ndg_linux = Certificate.objects.get(name="ndg_linux").parameter
    ndg_linux_text = Certificate.objects.get(name="ndg_linux_text").parameter
    intro_cyber = Certificate.objects.get(name="intro_cyber").parameter
    intro_cyber_text = Certificate.objects.get(name="intro_cyber_text").parameter
    cyber_101 = Certificate.objects.get(name="cyber_101").parameter
    cyber_101_text = Certificate.objects.get(name="cyber_101_text").parameter
    flutter_name = Certificate.objects.get(name="flutter_name").parameter
    flutter_text = Certificate.objects.get(name="flutter_text").parameter



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
        'about_myself_city': about_myself_city,
        'about_myself_country': about_myself_country,
        'about_freelance_section': about_freelance_section,
        'about_degree_section': about_degree_section,
        'skills_section': skills_section,
        'resume_section_0': resume_section_0,
        'certificate_section': certificate_section,
        'about_photo': about_photo,
        'skills_left': skills_left,
        'skills_right': skills_right,
        'experiences': experiences,
        'educations': educations,
        'communities': communities,
        'sql_name': sql_name,
        'sql_text': sql_text,
        'tech_summit': tech_summit,
        'tech_summit_text': tech_summit_text,
        'ndg_linux' : ndg_linux,
        'ndg_linux_text': ndg_linux_text,
        'intro_cyber': intro_cyber,
        'intro_cyber_text': intro_cyber_text,
        'cyber_101': cyber_101,
        'cyber_101_text':cyber_101_text,
        'flutter_name' : flutter_name,
        'flutter_text': flutter_text,



    }
    return render(request, 'index.html', context=context)

