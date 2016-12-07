from django.shortcuts import render
from django.utils import timezone
from .models import Prod
from django.shortcuts import render, get_object_or_404
#from .forms import PostForm



def post_list(request):
    return render(request, 'prod/post_list.html', {})