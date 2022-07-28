from turtle import title

from djongo import models
from djongo.models.fields import ObjectId
# Create your models here.
class jobs(models.Model):
    CATEGORY_CHOISE=(
        ('Marketing',"Marketing"),
        ('Customer Service',"Customer Service"),
        ('Human Resource',"Human Resource"),
        ('Project Management',"Project Management"),
        ('Business Development',"Business Development"),
        ('Sales And Communication',"Sales And Communication"),
        ('Design & Creative',"Design & Creative"),
        ('Information Technology',"Information Technology"),
    )

    JOBTYPE_CHOISE=(
        ("Full Time","Full Time"),
        ("Part Time","Part Time"),
        ("Temporary","Temporary"),
        ("Contract","Contract"),

    )
    _id=models.fields.ObjectIdField()
    title=models.CharField(max_length=255)
    companyname=models.CharField(max_length=255)
    category=models.CharField(max_length=25,choices=CATEGORY_CHOISE)
    type=models.CharField(max_length=10,choices=JOBTYPE_CHOISE)
    location=models.CharField(max_length=255)
    minSalary=models.IntegerField()
    maxSalary=models.IntegerField()
    description=models.TextField()
    responsibilities=models.TextField()
    qulifications=models.TextField()
    companydetail=models.TextField()
    noOfvacancy=models.IntegerField()
    url=models.URLField()
    postby=models.GenericObjectIdField()
    date=models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS=['title','companyname','category','type','location','description','responsibilities','qulifications','url']
    class Meta:
        db_table='jobPost'