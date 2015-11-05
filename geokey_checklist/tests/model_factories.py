import datetime
import factory

from geokey.categories.tests.model_factories import CategoryFactory
from geokey.categories.tests.model_factories import FieldFactory
from geokey.projects.tests.model_factories import ProjectF
from geokey.users.tests.model_factories import UserF

from ..models import Checklist
from ..models import ChecklistItem
from ..models import ChecklistSettings

class ChecklistFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Checklist

    name = factory.Sequence(lambda n: 'Checklist %d' %n)
    project = factory.SubFactory(ProjectF)
    category = factory.SubFactory(CategoryFactory)
    creator = factory.SubFactory(UserF)

    description = ""
    checklisttype = 'Blank'
    numberofpeople = 1
    numberofchildren = 1
    numberoftoddlers = 1
    numberofinfants = 1
    numberofpets = 1
    latitude =  47.6097
    longitude = -122.3331

class ChecklistItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ChecklistItem

    name = factory.Sequence(lambda n: 'ChecklistItem %d' %n)
    project = factory.SubFactory(ProjectF)
    category = factory.SubFactory(CategoryFactory)
    field = factory.SubFactory(FieldFactory)
    creator = factory.SubFactory(UserF)

    checklistitemdescription = ""
    checklistitemurl = ""
    checklistitemtype = 'Custom'
    quantityfactor = 1
    pertype = 'individual'
    quantity = 1
    quantityunit = ""
    expiryfactor = '365'
    expiry = datetime.date(2018, 01, 03)
    haveit = False

class ChecklistSettingsFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ChecklistSettings

    project = factory.SubFactory(ProjectF)

    reminderson = True
    frequencyonexpiration = 'twice'
    frequencybeforeexpiration = 180
