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
