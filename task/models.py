from django.db import models

class Task(models.Model):
    prior_choice=((1,"low"),(2,"2"),(3,"medium"),(4,"4"),(5,"high"))
    status_choice=((1,"ToDo"),(2,"Doing"),(3,"Done"))
    name=models.CharField(max_length=200,verbose_name="task name")
    desc=models.TextField(null=True,blank=True)
    priority=models.IntegerField(default=3,choices=prior_choice)
    status=models.IntegerField(choices=status_choice,default=1)
    due_date=models.DateTimeField(null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table="tasks"
    
    