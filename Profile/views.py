from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User

from .models import *

def user_details(request, username):

    if username.lower() == "eoghy":
        profile = get_object_or_404(Profile, pk=2)
        context = {'profile':profile}
    elif username.lower() == "eoghan":
        profile = get_object_or_404(Profile, pk=1)
        context = {'profile':profile}
    
    return render(request, 'profile/user.html', context)