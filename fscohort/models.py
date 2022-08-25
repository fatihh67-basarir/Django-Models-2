from django.db import models


class Student(models.Model):
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    number = models.IntegerField('Numara')
    about = models.TextField('Hakkında', blank=True, null=True)
    avatar = models.ImageField('Resim', blank=True, null=True, upload_to='media/')

    def __str__(self):
        return f"{self.first_name} - {self.last_name} {self.number} "


     