from django.utils import timezone
from django.test import TestCase

from ..models import Checklist, ChecklistItem
from .model_factories import ChecklistFactory, ChecklistItemFactory


# class ChecklistTest(TestCase):

#     def test_update(self):
        #checklist = ChecklistFactory(description="test", checklisttype='Home', numberofpeople=2, numberofchildren=2, numberoftoddlers=2, numberofinfants=2, numberofpets=2, latitude=0, longitude=0)
        # checklist = ChecklistFactory()
        # checklist.update({"description": "newtest"})
        #checklist.update({"numberofinfants": 3})
        #...
        # reference = Checklist.objects.get(pk=checklist.id)
        # self.assertEqual(reference.description, "newtest")
        #self.assertEqual(reference.numberofinfants, 3)

        #self.assertEqual(checklist.checklisttype, "Home")
        #self.assertEqual(checklist.numberofpeople, 2)
        #self.assertEqual(checklist.numberofchildren, 2)
        #self.assertEqual(checklist.numberoftoddlers, 2)
        #self.assertEqual(checklist.numberofinfants, 2)
        #self.assertEqual(checklist.numberofpets, 2)
        #self.assertEqual(checklist.latitude, 0)
        #self.assertEqual(checklist.longitude, 0)

# class ChecklistItemTest(TestCase):
#     def test_update(self):
#         checklistitem = ChecklistItemFactory(haveit=False)
#         reference = ChecklistItems.objects.get(pk=checklistitem.id)
#         self.assertFalse(reference.haveit)
#         checklistitem.update({"haveitem": True})
#         self.assertTrue(reference.haveit)

        #checklistitem = ChecklistItemFactory(haveit=False)
        #self.assertFalse(checklistitem.haveit)
