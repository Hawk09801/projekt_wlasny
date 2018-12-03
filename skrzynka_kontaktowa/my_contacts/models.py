from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField(null=True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)


class Address(models.Model):
    city = models.CharField(max_length=64, null=True)
    street = models.CharField(max_length=64, null=True)
    house_number = models.SmallIntegerField(null=True)
    apartment_number = models.SmallIntegerField(null=True)


class Telephon(models.Model):
    TYPE_NUMBER = (
        (1, "numer domowy"),
        (2, "numer służbowy"),
        (3, "numer komórkowy"),
        (4, "inny")
    )
    number = models.IntegerField(null=True)
    type_number = models.IntegerField(choices=TYPE_NUMBER, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Mail(models.Model):
    MAIL_TYPE = (
        (1, "mail prywatny"),
        (2, "mail służbowy"),
        (3, "inny")
    )
    mail = models.EmailField(max_length=64, null=True)
    mail_type = models.IntegerField(choices=MAIL_TYPE, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.TextField(null=True)
    person = models.ManyToManyField(Person, null=True)
