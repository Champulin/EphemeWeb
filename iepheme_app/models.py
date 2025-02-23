from django.db import models
from django.urls import reverse
# Create your models here.
class Video(models.Model):
    # Fields
    title = models.CharField(max_length=200, help_text='Titre du video', verbose_name='Titre')
    author = models.CharField(max_length=200, help_text='Autheur du video', verbose_name='Auteur')
    description = models.TextField(max_length=2000, help_text='Description pour le video', verbose_name='Description')
    video_url = models.CharField(max_length=200, help_text='Url du video ', verbose_name='Video URL')
    thumbnail_url = models.CharField(max_length=200, help_text='Url du thumbnail (gif)', verbose_name='Thumbnail URL')
    date = models.DateField()
    tags = models.CharField(max_length=200, help_text='Tags du video (séparés par des virgules)')
    source_name = models.ForeignKey('Source', on_delete=models.CASCADE,null=True, help_text='Youtube ou Vimeo',verbose_name='Source')
    category_name = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, help_text='choisi la catégorie du video', verbose_name='Catégorie')
    # Metadata
    class Meta:
        ordering = ['title','-date']
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    #Methods
    def __str__(self):
        return f'{self.title} '


class Category(models.Model):
    # Fields
    name = models.CharField(max_length=200,db_index=True, help_text='Nom de la catégorie', verbose_name='Nom du Catégorie')
    slug = models.SlugField(unique=True)
    #add a field called alphabetic_order
    alphabetic_order = models.CharField(max_length=200,default='a-' ,help_text='ordre dans lequel les videos vont apparaitre "a-1"', verbose_name='Ordre alphabétique')
    class Meta:
        ordering = ['alphabetic_order']
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    # Methods
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('iepheme_app:category', kwargs={'slug': self.slug})

class Source(models.Model):
    #Fields
    name = models.CharField(max_length=200,db_index=True, help_text='Youtube ou Vimeo', verbose_name='Nom du site')
    def __str__(self):
        return f'{self.name}'