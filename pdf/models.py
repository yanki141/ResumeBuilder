from django.db import models

# Create your models here.
# After creating this, do makemigrations to create table in the framework
# to create in db we need to migrate
# To see the table, create superuser: syanki/Syanki@141
# Can't see this table in Admin interface, include this class in admin.py
# after registering this model, we can create any Profile from admin interface as well like form filling.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=100)
    ambition = models.TextField(max_length=100)
    work_ex = models.TextField(max_length=100)

    def __str__(self):
        return f'Resume of {self.name} having email: {self.email}'