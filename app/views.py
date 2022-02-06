from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('id')[0]
        return render(request, 'app/index.html',{
            'profile_data':profile_data,
        })

class WorkView(View):
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.all()
        if work_data.exists():
            work_data = work_data.order_by('id')[0]
        work_data = Work.objects.order_by('id')
        return render(request, 'app/portfolio.html',{
            'work_data': work_data
        })

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('id')[0]
        return render(request, 'app/profile.html',{
            'profile_data':profile_data,
        })
