from django.db import models

#Create your models here.
class School(models.Model):
    school_id = models.CharField(max_length=25)
    school_name    = models.CharField(max_length=90)
    school_address = models.CharField(max_length=90)
    school_city    = models.CharField(max_length=50)
    school_state   = models.CharField(max_length=50)
    school_type    = models.CharField(max_length=40)
    
#Students instead of Student because the data displays information from a group of students    
class Students(models.Model):
    school_id = models.ForeignKey('School', on_delete=models.CASCADE)
    number_of_students = models.FloatField()
    work_and_study     = models.FloatField()
    average_age        = models.FloatField()
    grade_retention    = models.FloatField()
    ethnicity_hispanic = models.FloatField()
    ethnicity_gmayan   = models.FloatField()
    
class Education_options_hslevel(models.Model):
    school_id = models.ForeignKey('School', on_delete=models.CASCADE)
    _studying_accounting       = models.FloatField()
    _studying_secretary        = models.FloatField()
    _studying_teaching_edu     = models.FloatField()
    _studying_university_prep  = models.FloatField()
    
class Previous_Results(models.Model):
    school_id = models.ForeignKey('School', on_delete=models.CASCADE)
    Linguistics_2017  = models.FloatField()
    Linguistics_2018  = models.FloatField()
    Linguistics_2019  = models.FloatField()
    Mathematics_2017  = models.FloatField()
    Mathematics_2018  = models.FloatField()
    Mathematics_2019  = models.FloatField()
    
    

    
    
