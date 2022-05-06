from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.mail import send_mail
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, Uname, phone, age , country , company_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not Uname:
            raise ValueError("Username id required")
        if not phone:
            raise ValueError("please write phone number")
        if not age:
            raise ValueError("please write your age")
        if not country:
            raise ValueError("country is required")
        if not company_name:
            raise ValueError("country is required")

        
        user=self.model(
            email=self.normalize_email(email),
            Uname=Uname,
            phone=phone,
            age=age,
            country=country,
            company_name=company_name
        )
        user.set_password(password)
        user.save(using=self._db)
        subject='Thx'
        message='Hey <<Some Text>>'
        to=user.email
        send_mail(
            subject,
            message,
            '200103301@stu.sdu.edu.kz',
            [to],
        )
        return user
    
    def create_superuser(self , email , Uname , phone , age , country ,company_name ,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            Uname=Uname,
            phone=phone,
            age=age,
            country=country,
            password=password,
            company_name=company_name
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email address",max_length=60,unique=True)
    Uname=models.CharField(verbose_name="Username",max_length=200,unique=True)
    phone=models.CharField(max_length=20,verbose_name="phone")
    age=models.CharField(max_length=10,verbose_name="age")
    country=models.CharField(max_length=20,verbose_name="country")
    company_name=models.CharField(max_length=30,verbose_name="company_name")
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=['Uname','phone','age','country','company_name']

    objects=MyUserManager()

    def __str__(self):
        return self.Uname
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True



class Comment(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Коммент"
        verbose_name_plural="Комментарии"
        ordering=['title']

class Posts(models.Model):
    title=models.CharField(max_length=150)
    is_published=models.BooleanField(default=True)
    
    def get_number(self):
        return 7
    def get_title(self):
        return "Alikhan"
