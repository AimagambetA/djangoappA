from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from app.forms import UserRegistrationForm,UserLoginForm
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def covid(request):
    return render(request, 'app/covid.html')

def index2(request):
    return render(request, 'app/index2.html')

def register(request):
    context={}
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.save()
            subject="THANKS FOR REGISTRATION"
            message='HEY '+user.Uname + ' ,you are now successfully register with us and your password is secure'
            to=user.email
            send_mail(
                subject,
                message,
                '200103301@stu.sdu.edu.kz',
                [to],
            )
            return redirect('login')
        context['register_form']=form
    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, "app/register.html",context)

def home_view(request):
    return render(request,"app/dashboard.html")
def login_view(request):
    context={}
    if request.POST:
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request, email=email,password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:
            context['login_form']=form
    else:
        form=UserLoginForm()
        context["login_form"]=form
    return render(request,"app/login.html",context)

def logout_view(request):
    logout(request)
    return redirect('login')

def show_post(request,post_id):
    post=get_object_or_404(Comment,pk=post_id)
    context={'post':post}
    return render(request,'app/post.html',context=context)

def send_message(request):
    send_mail("Test my DJANGO app for sending mail","Some text here","200103301@stu.sdu.edu.kz",["200103301@stu.sdu.edu.kz"],fail_silently=False)
   
    # email = EmailMessage(
    #     'Hello',
    #     'Some text here',
    #     '200103301@stu.sdu.edu.kz',
    #     '200103301@stu.sdu.edu.kz',
    #     headers={'Message-ID': 'foo'},
    # )
    # email.attach_file('C:/Django/djangoapp/app/images/1210.jpg')
    # email.send(fail_silently=False)


    return render(request,'app/successfull.html')