from django.db import models

# Create your models here.

class Batches(models.Model):
    batchid = models.PositiveIntegerField(db_column='batchId', max_length=7 ,primary_key=True) 
    coursename = models.CharField(db_column='courseName', max_length=15, blank=True, null=True)  
    joinyear = models.IntegerField(db_column='joinYear', max_length=4,blank=True, null=True) 
    endyear = models.IntegerField(db_column='endYear', max_length=4,blank=True, null=True)

    class Meta:
        db_table = 'batches'

    def __str__(self):
        return f'{self.batchid}'

class OfficialAlumni(models.Model):
    regno = models.PositiveIntegerField(db_column='regNo', primary_key=True)  
    studentname = models.CharField(db_column='studentName', max_length=40)  
    mobile = models.CharField(max_length=15, blank=True, null=True)
    instmail = models.EmailField(db_column='instMail', max_length=23, blank=True, null=True) 
    personalmail = models.EmailField(db_column='personalMail', max_length=255, blank=True, null=True) 
    batchid = models.ForeignKey(Batches, models.PROTECT, db_column='batchId')  
    is_registered = models.BooleanField(default= False)
    
    class Meta:
        managed = True
        db_table = 'official_alumni'
# add column registerd boolean type in db 