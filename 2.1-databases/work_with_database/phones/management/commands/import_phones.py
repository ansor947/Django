import csv
from django.core.management.base import BaseCommand
from phones.models import Phone




class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
                Phone.objects(                
                id=phone[0],
                name=phone[1],
                price=phone[2],
                image=phone[3],
                release_date=phone[4],
                lte_exists=phone[5],
                slug=phone[6]).create()
                                
            # instance_phone = Phone.objects(
            #     id=phone[0],
            #     name=phone[1],
            #     price=phone[2],
            #     image=phone[3],
            #     release_date=phone[4],
            #     lte_exists=phone[5],
            #     slug=phone[6]
            #     ).save()
            

            
            
