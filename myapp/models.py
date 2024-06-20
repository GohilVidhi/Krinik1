from django.db import models

# Create your models here.



class League(models.Model):
    league_name=models.CharField(max_length=50,blank=True,null=True)
    short_league_name=models.CharField(max_length=50,blank=True,null=True)
    start_league_date=models.CharField(max_length=50,blank=True,null=True)
    end_league_date=models.CharField(max_length=50,blank=True,null=True)
    league_image=models.ImageField(upload_to="league_image_media")
    
    
    def __str__(self):
        return self.league_name



       
    

#------Team Models----------   
    
class Team(models.Model):
    league_name=models.ForeignKey(League,on_delete=models.CASCADE)  
    team_name=models.CharField(max_length=50,blank=True,null=True)      
    team_short_name=models.CharField(max_length=50,blank=True,null=True)      
    team_image=models.ImageField(upload_to="league_image_media")
    team_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.team_name    
