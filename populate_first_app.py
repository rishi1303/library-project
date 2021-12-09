import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rishi.settings')
import django
django.setup()
import random
from faker import Faker
from first_app.models import User
fakegen = Faker()
def populate(N=5):
    for entry in range(N):
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_email = fakegen.email()
        useg = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)

if __name__=='__main__':
    print("Populaitng script")
    populate(5)
    print("Populating complete")
