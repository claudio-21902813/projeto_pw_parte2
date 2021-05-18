from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'website/base.html')

def info_page_view(request):
	return render(request, 'website/info.html')