from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Shirt
# from .models import Pant
# from .models import Jacket
# from .models import T_shirt
# from .models import Slides

def woman(request):
    return render(request, 'snippets/snip_woman.html')