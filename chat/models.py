# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------ modelos oficiales -----------------------------------------------------------------

class usersManager(BaseUserManager):
    def create_superuser(self, email, username, name, password):
        usuario = self.create_user(email = email, username = username, name = name, password = password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

    def create_user(self, email, username, name, password ):
        if not email:
            raise ValueError('el usuario debe tener un correo electronico')

        usuario = self.model(email = self.normalize_email(email), username = username, name = name)
        usuario.set_password(password)
        usuario.save()
        return usuario


class users(AbstractBaseUser):

    email = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, default='', unique=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = usersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name' ]

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador

    class Meta:
        db_table = 'users'
        

class u_states(models.Model):
    user = models.ForeignKey('users', on_delete=models.CASCADE)
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'u_states'
        
        
class c_states(models.Model):
    state = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'c_states'


class chat_users(models.Model):
    user = models.ForeignKey('users', on_delete=models.CASCADE)
    chat = models.ForeignKey('chats', on_delete=models.CASCADE)

    class Meta:
        db_table = 'chat_users'


class chats(models.Model):
    state = models.ForeignKey('c_states', on_delete=models.CASCADE)

    class Meta:
        db_table = 'chats'


class messages(models.Model):
    chat = models.ForeignKey('chats', on_delete=models.CASCADE)
    user = models.ForeignKey('users', on_delete=models.CASCADE)
    text = models.CharField(max_length=4000, blank=True, null=True)
    date_msj = models.DateTimeField(blank=True, null=True)
    url_file = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'messages'


class u_friends(models.Model):
    user = models.ForeignKey('users', on_delete=models.CASCADE, related_name='+')
    user_added = models.ForeignKey('users', on_delete=models.CASCADE, related_name='+')

    class Meta:
        db_table = 'u_friends'
        unique_together = (('user', 'user_added'),)






