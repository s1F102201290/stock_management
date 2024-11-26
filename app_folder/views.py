from django.shortcuts import render

# Create your views here.
from django.views import View  
  
class SampleView(View):  
	def get(self, request, *args, **kwargs):  
		return render(request, 'app_folder/top_page.html')
top_page = SampleView.as_view()