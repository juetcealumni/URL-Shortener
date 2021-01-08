from django.shortcuts import render,HttpResponseRedirect
import secrets
import string
from .models import ShortUrl
# Create your views here.
def index(request):
    if request.method=='POST':
        url_length=6
        long_url=request.POST.get('longurl')
        shortened_url=''.join(secrets.choice(string.ascii_letters+string.digits)
                    for i in range(url_length))
        print(shortened_url)
        new_url=ShortUrl.objects.create(long_url=long_url,short_url=shortened_url)
        updated_url=new_url.short_url+str(new_url.id)
        sh_url=request.build_absolute_uri('/'+updated_url+'/')
        print(sh_url)
        ShortUrl.objects.filter(id=new_url.id).update(short_url=updated_url)
        return render(request,'index.html',{'short':sh_url})
    return render(request,'index.html')

def UrlRedirect(request,shorturl):
    longURL=ShortUrl.objects.get(short_url=shorturl)
    return HttpResponseRedirect(longURL.long_url)
    