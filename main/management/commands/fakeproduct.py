from unicodedata import category
from django.core.management.base import BaseCommand
from main.models import Product
import random

from faker import Faker
fake = Faker()
class Command(BaseCommand):
    def handle(self,*args,**options):
        for i in range(100):
            Product.objects.create(
                name_uz = fake.name(), 
                name_en = fake.name(), 
                category_id = random.randint(1,4),
                price = 1000 * random.randint(10,10000), 
                available = random.randint(0,40)

            )
