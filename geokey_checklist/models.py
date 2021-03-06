from django.conf import settings
from django.db import models

from .base import TYPE
from .base import ITEM_TYPE
from .base import EXPIRY_FACTOR
from .base import PER_TYPE
from .base import FREQUENCY_EXPIRED_REMINDER
from .base import REMINDER_BEFORE_EXPIRATION

class Checklist(models.Model):
    """
    Stores a single checklist.
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey('projects.Project')
    category = models.ForeignKey('categories.Category')
    description = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    checklisttype = models.CharField(choices=TYPE, default=TYPE.Blank, max_length=100)
    numberofpeople = models.IntegerField()
    numberofchildren = models.IntegerField()
    numberoftoddlers = models.IntegerField()
    numberofinfants = models.IntegerField()
    numberofpets = models.IntegerField()
    latitude =  models.FloatField()
    longitude = models.FloatField()

    def update(self, newdata):
        for key in newdata:
            val = newdata[key]
            setattr(self,key,val)
            self.save()

class ChecklistSettings(models.Model):
    """
    Stores settings for the checklist extension for the user.
    """
    project = models.ForeignKey('projects.Project')
    reminderson = models.BooleanField(default=True)
    frequencyonexpiration = models.CharField(choices=FREQUENCY_EXPIRED_REMINDER, default=FREQUENCY_EXPIRED_REMINDER.one_month, max_length=100)
    #frequencybeforeexpiration = models.CharField(choices=REMINDER_BEFORE_EXPIRATION, default=REMINDER_BEFORE_EXPIRATION.six_months, max_length=100)
    lastremindercheck = models.DateTimeField(null=True)

class ChecklistItem(models.Model):

    """
    Stores a single checklist item.
    """
    name = models.CharField(max_length=100)
    project = models.ForeignKey('projects.Project')
    category = models.ForeignKey('categories.Category')
    field = models.ForeignKey('categories.Field')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    checklistitemdescription = models.CharField(max_length=100, null=True)
    checklistitemurl = models.CharField(max_length=255, null=True)
    checklistitemtype = models.CharField(choices=ITEM_TYPE, default=ITEM_TYPE.Custom, max_length=100)
    quantityfactor = models.IntegerField()
    pertype = models.CharField(choices=PER_TYPE, default=PER_TYPE.individual, max_length=100)
    quantity = models.IntegerField()
    quantityunit = models.CharField(max_length=100, null=True)
    expiryfactor = models.IntegerField(null=True)
    expiry = models.DateTimeField(null=True)
    haveit = models.BooleanField(default=False)

    def update(self, newdata):
        for key in newdata:
            val = newdata[key]

            if key == "haveit":
                if type(val) <> 'bool':
                    if val == "True":
                        val = True
                    else:
                        val = False

            setattr(self,key,val)
            self.save()
