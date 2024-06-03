from faker import Faker
fake = Faker()
import random
from .models import Student
def add(n=10):
    for i in range(n):
        name = fake.name()
        email = fake.email()
        age = random.randint(20,30)
        phone = random.randint(6000000000,9999999999)

        Student.objects.create(name=name,email=email,age=age,phone = phone)