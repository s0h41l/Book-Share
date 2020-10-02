from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Friend(models.Model):
    id = models.AutoField(primary_key=True)
    user_one_id = models.CharField(max_length=80)
    user_two_id = models.CharField(max_length=80)


class LookUp(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    createdAt = models.DateTimeField(auto_now=True)
    updateAt = models.DateTimeField()

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    status = models.ForeignKey(LookUp, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    photo = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)
    updateAt = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + "("+self.author+")"


class BookShare(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrower_id')
    lender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lender_id')
    status = models.ForeignKey(LookUp, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.phone


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
