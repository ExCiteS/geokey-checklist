from django.utils import timezone
from django.test import TestCase

from ..models import Checklist
from ..models import ChecklistItem
from .model_factories import ChecklistFactory
from .model_factories import ChecklistItemFactory


class ChecklistTest(TestCase):

    def test_update(self):
        checklist = ChecklistFactory(description="test", checklisttype='Home', numberofpeople=2, numberofchildren=2, numberoftoddlers=2, numberofinfants=2, numberofpets=2, latitude=0, longitude=0)
        self.assertEqual(checklist.description, "test")
        self.assertEqual(checklist.checklisttype, "Home")
        self.assertEqual(checklist.numberofpeople, 2)
        self.assertEqual(checklist.numberofchildren, 2)
        self.assertEqual(checklist.numberoftoddlers, 2)
        self.assertEqual(checklist.numberofinfants, 2)
        self.assertEqual(checklist.numberofpets, 2)
        self.assertEqual(checklist.latitude, 0)
        self.assertEqual(checklist.longitude, 0)

class ChecklistItemTest(TestCase):
    def test_update(self):
        checklistitem = ChecklistItemFactory(haveit=True)
        self.assertTrue(checklistitem.haveit)

        checklistitem = ChecklistItemFactory(haveit=False)
        self.assertFalse(checklistitem.haveit)
