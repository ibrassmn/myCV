from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now = True,
        verbose_name="Updated Date",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
    )
    class Meta:
        abstract =True

class GeneralSetting(AbstractModel):
    name =models.CharField(
        default='',
        max_length=254,
        blank=True,   #boş veriyi kaydetmeyi sağlar
        verbose_name="Name",
        help_text='The name of the general setting',
    )
    description =models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text='The description of the general setting',
    )
    parameter = models.CharField(
        default='',
        max_length=20000,
        blank=True,
        verbose_name="Parameter",
        help_text='',
        )


    def __str__(self):
        return f'Genereal Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,  # boş veriyi kaydetmeyi sağlar
        verbose_name="Name",
        help_text='The name of the general setting',
    )
    description =models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text='The description of the general setting',
    )
    file = models.FileField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )


    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)

class SkillLeft(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,  # boş veriyi kaydetmeyi sağlar
        verbose_name="Name",
        help_text='The name of the general setting',
    )
    percentage = models.IntegerField(
        default='50',
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Skill Left: {self.name}'

    class Meta:
        verbose_name = 'Skill Left'
        verbose_name_plural = 'Skills Left'
        ordering = ('order',)
class SkillRight(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,  # boş veriyi kaydetmeyi sağlar
        verbose_name="Name",
        help_text='The name of the general setting',
    )
    percentage = models.IntegerField(
        default='50',
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Skill Right: {self.name}'

    class Meta:
        verbose_name = 'Skill Right'
        verbose_name_plural = 'Skills Right'
        ordering = ('order',)

class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Company Name",
    )
    job_title = models.CharField(
        default='', max_length=254,blank=True,verbose_name="Job Title"
    )
    job_location = models.CharField(
        default='', max_length=254,blank=True,verbose_name="Job_Location"
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null = True,
        blank=True,
        verbose_name="End_Date"
    )
    job_summary = models.TextField(
        default='',
        max_length=20000,
        blank=True,
        verbose_name="Job Summary",
        help_text='',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)

class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="School Name",
    )
    major = models.CharField(
        default='', max_length=254,blank=True,verbose_name="Major"
    )
    department = models.CharField(
        default='', max_length=254,blank=True,verbose_name="Department"
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null = True,
        blank=True,
        verbose_name="End Date"
    )
    education_summary = models.TextField(
        default='',
        max_length=20000,
        blank=True,
        verbose_name="Education Summary",
        help_text='',
    )


    def __str__(self):
        return f'Education: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('-start_date',)

class My_Community(AbstractModel):
    community_tag = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Community Tag",
    )
    community_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Community Name",
    )
    community_place = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Community Place",
    )
    community_start_date = models.DateField(
        verbose_name='Community Start Date'
    )
    community_end_date = models.DateField(
        default=None,
        null = True,
        blank=True,
        verbose_name="Community End Date"
    )

    def __str__(self):
        return f'My Community: {self.community_name}'

    class Meta:
        verbose_name = 'My Community'
        verbose_name_plural = 'My Communities'
        ordering = ('community_name',)

class Certificate(AbstractModel):
    name =models.CharField(
        default='',
        max_length=254,
        blank=True,   #boş veriyi kaydetmeyi sağlar
        verbose_name="Name",
        help_text='The name of the general setting',
    )
    description =models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text='The description of the general setting',
    )
    parameter = models.CharField(
        default='',
        max_length=20000,
        blank=True,
        verbose_name="Parameter",
        help_text='',
        )

    def __str__(self):
        return f'Certificate: {self.name}'

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        ordering = ('name',)
