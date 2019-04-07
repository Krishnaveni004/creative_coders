from django.db import models
from django.utils import timezone

class form_1(models.Model):
    name=models.CharField(max_length=100,default='name')
    email=models.CharField(max_length=100,default='email')
    password=models.CharField(max_length=100,default='password')
# Create your models here.
class Test_Form(models.Model):
    name = models.CharField(max_length = 100, default = 'name');
    parent_contact = models.CharField(max_length = 100, default = 'parent_contact');
    email = models.EmailField(max_length = 100, default = 'email');
    contact = models.CharField(max_length = 100, default = 'phone');
    add = models.CharField(max_length = 100, default = 'address');
    internship = models.CharField(max_length = 100, default = 'internship');
    college = models.CharField(max_length = 100, default = 'college');
    cty_w = models.CharField(max_length = 100, default = 'city_for_internship');
    cty_l = models.CharField(max_length = 100, default = 'current_city');
    cent =models.CharField(max_length = 100, default = 'center');








class ContactForm(models.Model):
    name = models.CharField(max_length = 100, default = 'name');
    email = models.EmailField(max_length = 100, default = 'email');
    msg = models.TextField(max_length = 200, default = 'message');

class patient_table(models.Model):

    pid = models.CharField(max_length = 6, default = 'pid');
    did = models.CharField(max_length = 100, default = 'did');
    diseasename = models.CharField(max_length = 200, default = 'fever');
    date = models.DateTimeField(max_length = 100);
    linkreport = models.CharField(max_length = 200);
    uid = models.CharField(max_length=13, default='uid');
    pname = models.CharField(max_length=200, default='pname');
    dname = models.CharField(max_length=200, default='dname');
    hname = models.CharField(max_length=200, default='hname');


class Newsletter(models.Model):
    email = models.EmailField(max_length = 100, default = 'email');


class DataVirtualizationForm(models.Model):
    name = models.CharField(max_length = 100, default = 'name');
    parent_contact = models.CharField(max_length = 100, default = 'parent_contact');
    email = models.EmailField(max_length = 100, default = 'email');
    contact = models.CharField(max_length = 100, default = 'phone');
    add = models.CharField(max_length = 100, default = 'address');
    college = models.CharField(max_length = 100, default = 'college');
    cty_l = models.CharField(max_length = 100, default = 'current_city');
    cent =models.CharField(max_length = 100, default = 'center');
    review = models.CharField(max_length = 100, default = 'review');
    review_message = models.CharField(max_length = 500, default = 'review message')
    timestamp = models.DateTimeField(default = timezone.now)









# class Company(models.Model):
#     company_name = models.CharField(max_length = 80);
#     company_criteria = models.IntegerField(default = 0);
#     course = models.ForeignKey('CourseDesc', on_delete = models.CASCADE, default = 'course');
#     # skills_required = models.ForeignKey('Course', on_delete = models.CASCADE, default = 0);


# for future...
# class courses(models.Model):
#     course_title = models.CharField(max_length = 50);
