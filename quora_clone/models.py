from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    question=models.TextField(blank=False,null=False)
    created_by=models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)


    def __str__(self):
        return self.question
    
    @property
    def answers(self):
        return self.answers_set.all()
    

class Answers(models.Model):
    answer_id=models.ForeignKey('quora_clone.Questions',on_delete=models.CASCADE)
    answers=models.TextField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name="Like",blank=True)
    answers_by=models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.answers
    
    
    


    