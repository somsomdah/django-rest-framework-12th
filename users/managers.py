from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self,code,name,password,**extra_fields):
        user=self.model(code=code,name=name,**extra_fields)
        user.set_password(password) # 지정 암호를 암호화 해서 password 필드에 저장
        user.save()
        return user

    def create_superuser(self,code,name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(code,name, password, **extra_fields)