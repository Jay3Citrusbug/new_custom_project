from django.shortcuts import render,redirect    
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Campaign, campaign_action


class Campaign(View):
    def get(self, request):
        return render(request, "client/campaigns.html")


class CampaignCreate(View):
    def get(self, request):
        return render(request, 'client/campaign_creation.html')



class AddCampaign(View):
    
    
    def get(self, request):
        return HttpResponse("Inside AddCampaign get method")

    def post(self, request):
        print("Inside AddCampaign post method")
        print(request.POST,"post data is")
        print(request.POST.getlist('sending_window_days[]'),"post data is=========>>>>")
        campaign_name = request.POST.get('campaign_name')
        camp_status=request.POST.get('camp_status')
      
        trigger_type=request.POST.get('trigger_type')
        trigger_val=request.POST.get('trigger_val')
        
        sending_window_days = request.POST.getlist("sending_window_days[]")
      
        sending_window_starttime=request.POST.get('sending_window_starttime')
        sending_window_endtime=request.POST.get('sending_window_endtime')
        sending_window_status=request.POST.get('sending_window_status')
        send_number_number=request.POST.get('send_number_number')
        double_optin_keyword=request.POST.get('double_optin_keyword')
        double_optin_message=request.POST.get('double_optin_message')
        double_optin_status=request.POST.get('double_optin_status')
        limit_multiple_status=request.POST.get('limit_multiple_status')
        limit_multiple_messasge=request.POST.get('limit_multiple_messasge')
        cancellation_status=request.POST.get('cancellation_status')
        cancellation_on_reply=request.POST.get('cancellation_on_reply')
        
        
        
        print("name=",campaign_name)
        print("days is it=",sending_window_days)
        print("trigger val=",trigger_val)
        print('type of tigger',trigger_type)
        
        
        
        
    
        return JsonResponse({'data':campaign_name,'status':True,'msg':'updated','url':'http://127.0.0.1:8000/campaign-creation/'})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    