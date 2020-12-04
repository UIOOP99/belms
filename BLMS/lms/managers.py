from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not user_id:
            raise ValueError('The given user id must be set')
        #email = self.normalize_email(email)
        user = self.model(user_id=user_id, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, user_id, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id , **extra_fields)

    def create_superuser(self,user_id, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(user_id, **extra_fields)