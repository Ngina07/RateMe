from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from .forms import UploadProjectForm,ReviewForm,UpdateProfile
from django.db.models import Avg
from .serializers import ProfileSerializer,ProjectSerializer
from rest_framework import viewsets




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


def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        projects = Project.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'projects': projects, 'message': message})
        
    return render(request, 'search.html')

def project(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    project = Project.objects.get(id = id)
    reviews = Review.objects.filter(project = project)
    design = reviews.aggregate(Avg('design'))['design__avg']
    usability = reviews.aggregate(Avg('usability'))['usability__avg']
    content = reviews.aggregate(Avg('content'))['content__avg']
    average = reviews.aggregate(Avg('average'))['average__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.average = (review.design + review.usability + review.content) / 3
            review.project = project
            review.user = user
            review.save()
        return redirect('project', id)
    else:
        form = ReviewForm()
    return render(request, 'project.html', {'project': project, 'reviews': reviews, 'form': form, 'design': design, 'usability': usability, 'content': content, 'average': average})


def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})

@login_required(login_url = '/accounts/login/')
def update_profile(request, id):
    if request.method == 'POST':
        profile = Profile.objects.get(id = id)
        form = UpdateProfile(request.POST or None, request.FILES or None, instance = profile)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.save()
            return redirect('profile', username = request.user)
    else:
        form = UpdateProfile()

    return render(request, 'update_profile.html', {'form': form})


class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.object.all()
    serializer_class = ProjectSerializer