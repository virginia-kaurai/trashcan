from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


class CustomAccountManager(BaseUserManager):

    def create_user(
        self,
        email,
        
        first_name,
        last_name,
        password=None,
        **other_fields
    ):

        
        if not email:
            raise ValueError(
                "You must provide an email address"
            )

        
        email = self.normalize_email(email)

       
        user = self.model(
            email=email,
            
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )

        
        user.set_password(password)

     
        user.save(using=self._db)

        return user


    def create_superuser(
        self,
        email,
       
        first_name,
        last_name,
        password=None,
        **other_fields
    ):

        
        other_fields.setdefault(
            "is_staff",
            True
        )

        other_fields.setdefault(
            "is_superuser",
            True
        )

        other_fields.setdefault(
            "is_active",
            True
        )

        # Create the superuser using create_user()
        return self.create_user(
            email=email,
            
            first_name=first_name,
            last_name=last_name,
            password=password,
            **other_fields
        )  



class User(AbstractBaseUser,PermissionsMixin):
    
   

    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=True
    )

   
    objects = CustomAccountManager()


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)

     ROLE_CHOICES= (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('principal', 'Principal'),
     )
     role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True)