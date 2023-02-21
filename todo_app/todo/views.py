from django.shortcuts import render,redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.models import User
# from .forms import RegisterForm,LoginForm

# Create your views here.
#
# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     fields = '__all__'
#     success_url = reverse_lazy('task')
#     redirect_authenticated_user = True
#
#     def get_success_url(self):
#         return self.success_url

def Home(request):
    return render(request,'home.html')


class TaskList(ListView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'taskdetail.html'

#
#
# def login_fun(request):
#     login = Login.objects.all()
#     context={}
#     form = LoginForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('/task-list')
#     context['form'] = form
#     return render(request,"login2.html",context)
#
#
#
# def register_fun(request):
#     register = Register.objects.all()
#     context={}
#     form = RegisterForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('/login/')
#     context['form'] = form
#     return render(request,"register.html",context)
#


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"You created an account!")

        return redirect('login')

    return render(request,'register.html')


class CustomLogin(LoginView):
    template_name='login2.html'
    fields ='_all_'
    success_url = reverse_lazy('task')
    redirected_authenticated_user=True

    def get_success_url(self):
        return self.success_url