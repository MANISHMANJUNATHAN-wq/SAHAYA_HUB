from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import HelpRequest
from .forms import HelpRequestForm

def home(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HelpRequestForm()

    requests_list = HelpRequest.objects.all().order_by('-created_at')
    total_count = requests_list.count()
    pending_count = requests_list.filter(status='PENDING').count()
    resolved_count = requests_list.filter(status='RESOLVED').count()

    context = {
        'form': form,
        'requests': requests_list,
        'total_count': total_count,
        'pending_count': pending_count,
        'resolved_count': resolved_count,
    }
    return render(request, 'hub/index.html', context)

# Only logged-in volunteers can accept or resolve tasks
@login_required(login_url='login')
def update_status(request, pk):
    item = get_object_or_404(HelpRequest, pk=pk)
    if item.status == 'PENDING':
        item.status = 'IN_PROGRESS'
    elif item.status == 'IN_PROGRESS':
        item.status = 'RESOLVED'
    item.save()
    return redirect('home')

def volunteer_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'hub/login.html', {'form': form})

def volunteer_signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request, 'hub/signup.html', {'form': form})

def volunteer_logout(request):
    logout(request)
    return redirect('home')