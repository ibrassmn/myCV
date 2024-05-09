from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
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
        max_length=254,
        blank=True,
        verbose_name="Parameter",
        help_text='',
        )
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

    def __str__(self):
        return f'Genereal Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)
