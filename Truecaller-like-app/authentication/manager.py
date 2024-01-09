from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
   def create_user(self, name, password, **extra_fields):
      if not name:
         raise ValueError("name is required")
      extra_fields['email']=self.normalize_email(extra_fields['email'])
      user= self.model(name=name,**extra_fields)
      user.set_password(password)
      user.save(using=self.db)
      return user
   
   def create_superuser(self, name, password, **extra_fields):
      extra_fields.setdefault('is_staff',True)
      extra_fields.setdefault('is_superuser',True)
      extra_fields.setdefault('is_active',True)
      return self.create_user(name,password,**extra_fields)
   
  
      
      
