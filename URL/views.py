from django.shortcuts import render
import pyshorteners
# Create your views here.

def ShortURL(request):
    if request.method == 'POST':
        url = request.POST.get('shortURL')
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(url)
        return render(request,'index.html',context={'short_url':short_url})
    return render(request,'index.html')
    