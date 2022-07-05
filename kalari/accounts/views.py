from django.shortcuts import render
from django.shortcuts import redirect,render
from .forms import signupForm,AuthForm,CommonForm,signupForm,mykalariForm,usersForm
from django.contrib.auth import login,authenticate,logout

def home(request):
    return render(request,'account/home.html')

def signup_mykalari(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = mykalariForm()
         context['form2'] = signupForm()
         return render(request,'account/mykalri_reg.html',context)
    elif request.method == 'POST':
         form1=mykalariForm(request.POST)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'mykalari'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1
             context['form2']   = form2
             return render(request,'account/mykalri_reg.html',context)
def signup_users(request):
    if request.method == 'GET':
         context = {}
         context['form1'] = usersForm()
         context['form2'] = signupForm()
         return render(request,'account/users_reg.html',context)
    elif request.method == 'POST':
         form1=usersForm(request.POST)
         form2= signupForm(request.POST)
         if form1.is_valid() and form2.is_valid():
             user =form2.save(commit=False)
             user.set_password(form2.cleaned_data['password'])
             user.user_type = 'users'
             user.save()
             company = form1.save(commit=False)
             company.user = user
             company.save()
             return redirect('account_login')
         else:
             context = {}
             context['form1'] = form1
             context['form2']   = form2
             return render(request,'account/company_reg.html',context)


# Create your views here.
def login_view(request):
    if request.method =='GET':
        context = {}
        context['form'] = AuthForm()
        return render(request, 'account/signin.html', context)
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('/admin/')
            elif user.user_type =='mykalari':
                return redirect('mykalary_home')
            elif user.user_type =='users':
                return redirect('users_home')


        else:
            context = {}
            context['form'] = AuthForm()
            context['error'] = 'Invalid Credentials'
            return render(request, 'account/signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('account_login')


# Create your views here.
