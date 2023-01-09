from django.db import models







# Create your models here.
class Campaign(models.Model):
    camp_id = models.AutoField(primary_key=True)
    camp_name=models.CharField(max_length=150, null=True, blank=True)
    camp_status=models.BooleanField()
    trigger_type=models.CharField(max_length=125,null=True, blank=True)
    trigger_value=models.JSONField(blank=True)
    sending_window_days=models.CharField(max_length=125,null=True, blank=True)
    sending_window_starttime=models.CharField(max_length=20,null=True, blank=True)
    sending_window_endtime=models.CharField(max_length=20,null=True, blank=True)
    sending_window_status=models.BooleanField()
    send_number_number=models.CharField(max_length=10,blank=True)
    double_optin_keyword=models.CharField(max_length=150,null=True)
    double_optin_message=models.CharField(max_length=250,null=True,blank=True)
    double_optin_status=models.BooleanField()
    limit_multiple_messasge=models.CharField(max_length=200,null=True,blank=True)
    limit_multiple_status=models.BooleanField()
    cancellation_on_reply=models.BooleanField()
    cancellation_status=models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return str(self.camp_name)
    
    
class campaign_action(models.Model):
    action_type=models.CharField(max_length=150,null=True,blank=True)
    action_value=models.JSONField(blank=True)
    oreder=models.IntegerField()
    camp_id=models.ForeignKey(Campaign,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    