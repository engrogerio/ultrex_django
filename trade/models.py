from django.db import models
from django.db.models import CharField
from django.db.models import DecimalField
from django.db.models import IntegerField
from django.db.models import BooleanField
from django.db.models import DateTimeField
from api.utils import OptionApi
import cred_guten_env


class Trade(models.Model):
    
    CALL = 'call'
    PUT = 'put'
    ACTION_CHOICES = [
        (CALL, 'Call'),
        (PUT, 'Put'),
    ]
    
    BINARY = 'binary'
    DIGITAL = 'digital'
    TYPE_CHOICES = [
        (BINARY, 'Binary'),
        (DIGITAL, 'Digital')
    ]

    OPEN  = 'open'
    CLOSED = 'closed'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed')
    ]
    
    asset_CHOICES = OptionApi().get_asset_list()

    amount = DecimalField(max_digits=6, decimal_places=2)
    asset = CharField(max_length=20, choices=asset_CHOICES)
    action = CharField(max_length=10, choices=ACTION_CHOICES)
    type = CharField(max_length=8, choices = TYPE_CHOICES, default=DIGITAL)
    duration = IntegerField()
    martingale = BooleanField(default=False)
    martingale_factor = DecimalField(max_digits=2, decimal_places=1, default=0)
    start_datetime = DateTimeField()
    status = CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
    
    def __str__(self):
        return f'$ {self.amount} - {self.asset} - {self.start_datetime} - {self.duration} minutes'

    def deploy(self):
        api = OptionApi()
        result = api.commit_trade(self.type, self.asset, self.amount, self.action, self.duration)
        print (result)
        status = result['position-changed']['msg']['status']
        self.status = status
        self.status = self.CLOSED
        self.save()
        