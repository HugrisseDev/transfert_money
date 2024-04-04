from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm


def dashboard(request):
    
    queryAllData = Transaction.objects.get(id=2)
    
    context = {'transact': queryAllData}
    
    
    return render(request, 'dashboard.html', context = context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('signin')  # Redirect to the sign-in page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the home page after successful sign-in
    return render(request, 'signin.html')


def home(request):
    
    return render(request, 'index.html')


def createTransaction(request):
    
    form = TransactionForm()
    context = {'form': form}
    
    return render(request, 'TransactionForm.html', context = context)