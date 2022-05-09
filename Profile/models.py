from django.db import models
from django.contrib.auth.models import User

class Links(models.Model):
    Link_Author = models.ManyToManyField(User)
    Link_Name = models.CharField('Link Name', max_length=255)
    Link_HTTP = models.URLField('URL', max_length=255)
    Link_Icon = models.CharField('Icon Image', max_length=255, help_text='<strong>Font Awesome Code</strong><br/>')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['Link_Name']
        
    def get_authors(self):
        return ", ".join([a.username.capitalize() for a in self.Link_Author.all()])

    def __str__(self):
        label = self.Link_Name +  ' - ' + ", ".join([a.username.capitalize() for a in self.Link_Author.all()])
        link = str(label)
        return link

class Profile(models.Model):
    User_Full_Name = models.CharField('Name', max_length=255, null=True, blank=True, default='first last')
    User_Image = models.ImageField('Profile Image', upload_to='images/', blank=True)
    User_Title = models.CharField('Header', max_length=255)
    User_Summary = models.CharField('Summary', max_length=255)
    User_Phone = models.CharField('Phone Number', max_length=255, null=True, blank=True)
    User_Email = models.CharField('Email', max_length=255, null=True, blank=True)
    User_Links = models.ManyToManyField(Links)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        label = self.User_Full_Name
        user = str(label)
        return user