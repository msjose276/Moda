from django.shortcuts import render

# Create your views here.


def kids(request):
    return render(request, 'snippets/snip_kids.html')