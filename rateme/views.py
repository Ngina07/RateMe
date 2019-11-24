from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from .forms import UploadProjectForm,ReviewForm,UpdateProfile
from django.db.models import Avg




def welcome(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Profile.objects.filter(user = request.user).exists():
            Profile.objects.create(user = user)   
    projects = Project.objects.order_by('-pub_date')

    return render(request,"welcome.html",{"projects":projects})


@login_required(login_url='/accounts/login/')
def upload_project(request):
    if request.method == 'POST':
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
        return redirect('welcome')
    else:
        form = UploadProjectForm()

    return render(request, 'upload.html', {'form': form})