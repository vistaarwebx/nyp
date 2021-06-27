from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Group(models.Model):
    CHOICES = (('activated', 'Activated'),('deactivated', 'Deactivated'))
    is_published = models.CharField(max_length=12, choices=CHOICES, default='deactivated')
    activatedate = models.DateField(null=True)
    name =  models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

class Groupadmin(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    grpName = models.CharField(max_length= 200)
    grpsurname = models.CharField(max_length=200,null=True)
    Mobile = models.IntegerField(null=True)
    Block = models.CharField(max_length=10,null=True)
    Email = models.EmailField(null=True)
    Address = models.CharField(max_length=10)
    Address2 = models.CharField(max_length=10,null=True)
    City = models.CharField(max_length=10,null=True)
    State = models.CharField(max_length=10,null=True)
    Country = models.CharField(max_length=10,null=True)
    age = models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.grpName + '--' + self.group.name

class Member(models.Model):
    group_admin = models.ForeignKey(Groupadmin, on_delete=models.CASCADE, null=True)
    memName = models.CharField(max_length=200)
    memAge = models.IntegerField(null=True)
    memMobile = models.IntegerField(null=True)
    memEmail = models.EmailField(null=True)
    memeducation = models.CharField(max_length=10,null=True)
    memoccupation = models.CharField(max_length=10,null=True)
    memposition = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.memName + '--' + self.group_admin.grpName

class Facebook(models.Model):
    image = models.FileField(null=True)


class Posts(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(null=True)
    para = models.CharField(max_length=10000)
    date = models.DateField(null=True)

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.FileField(null=True)
    para = models.CharField(max_length=10000)
    date = models.DateField(null=True)

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(null=True)

class Press(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(null=True)
    para = models.CharField(max_length=10000)
    date = models.DateField(null=True)

class Test(models.Model):
    Text = models.CharField(max_length=200,null=True)

class contact(models.Model):
    name = models.CharField(max_length=200,null=True)
    subject = models.CharField(max_length=900,null=True)    
    message = models.CharField(max_length=500,null=True)    
    Email = models.EmailField(null=True)    


class Videos(models.Model):
    video = EmbedVideoField()  

class VOLUNTEERS(models.Model):
    CHOICES = (('activated', 'Activated'),('deactivated', 'Deactivated'))
    is_published = models.CharField(max_length=12, choices=CHOICES, default='deactivated')
    activatedate = models.DateField(null=True)
    date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Mobile_no = models.IntegerField(null=True)
    adhar_no = models.IntegerField(null=True)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    education = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    any_organization = models.CharField(max_length=50)
    nyp_camp = models.CharField(max_length=50)
    about_you = models.CharField(max_length=500)
    image = models.FileField(null=True)



class JOBINTERNSHIP(models.Model):
    CHOICES = (('activated', 'Activated'),('deactivated', 'Deactivated'))
    is_published = models.CharField(max_length=12, choices=CHOICES, default='deactivated')
    activatedate = models.DateField(null=True)
    date = models.DateTimeField(auto_now=True)
    area_of_intrest = models.CharField(max_length=50)
    desired_duration = models.DateField(null=True)
    starting_month = models.DateField(null=True) 
    brief_detail = models.CharField(max_length=500)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Mobile_no = models.IntegerField(null=True)
    adhar_no = models.IntegerField(null=True)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True) 
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    about_you = models.CharField(max_length=500)
    resume = models.FileField(null=True)
    image = models.FileField(null=True)



