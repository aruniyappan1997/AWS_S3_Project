from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'profiles/users.html', {'users': users})

def upload_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        print(form)
    else:
        form = UserProfileForm()
    return render(request, 'profiles/upload.html', {'form': form})
