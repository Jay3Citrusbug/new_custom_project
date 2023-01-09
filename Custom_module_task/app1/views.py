from django.shortcuts import render,redirect    
from django.http import HttpResponse
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


# @method_decorator(csrf_exempt, name='dispatch')
# class AddCampaign(View):

#     @csrf_protect
#     def get(self, request):
#         return HttpResponse("Inside AddCampaign get method")

#     @csrf_protect
#     def post(self, request):
#         print("Inside AddCampaign post method")
#         # print(request.POST)
#         name = request.POST['name']
#         trigger_type = request.POST['trigger_type']
#         trigger_val = request.POST['trigger_val']
#         status = request.POST['status']
#         sending_window_status = request.POST['sending_window_status']
#         days = request.POST['days']
#         start_time = request.POST['start_time']
#         end_time = request.POST['end_time']
#         double_optin_status = request.POST['double_optin_status']
#         double_optin_keyword = request.POST['double_optin_keyword']
#         double_optin_message = request.POST['double_optin_message']
#         limit_multiple_status = request.POST['limit_multiple_status']
#         limit_multiple_message = request.POST['limit_multiple_message']
#         cancellation_trigger_status = request.POST['cancellation_trigger_status']
#         on_reply = request.POST['on_reply']

#         if status == 'true':
#             status = True
#         else:
#             status = False

#         print("--------------------------------------------------")
#         print("name =", name)
#         print("trigger_type =", trigger_type)
#         print("trigger_val =", trigger_val)
#         print("status =", status)
#         print("sending_window_status =", sending_window_status)
#         print("days =", days)
#         print("start_time =", start_time)
#         print("end_time =", end_time)
#         print("double_optin_status =", double_optin_status)
#         print("double_optin_keyword =", double_optin_keyword)
#         print("double_optin_message =", double_optin_message)
#         print("limit_multiple_status =", limit_multiple_status)
#         print("limit_multiple_message =", limit_multiple_message)
#         print("cancellation_trigger_status =", cancellation_trigger_status)
#         print("on_reply =", on_reply)
#         print("on_reply =", type(status))
#         print("--------------------------------------------------")

#         return HttpResponse("Inside AddCampaign post method")


class AddCampaign(View):
    
    
    def get(self, request):
        return HttpResponse("Inside AddCampaign get method")

    def post(self, request):
        print("Inside AddCampaign post method")
        print(request.POST)
        campaign_name = request.POST.get('campaign_name')
        print(campaign_name,"campaign name ==========>>>>>")
        
        return HttpResponse("hello")