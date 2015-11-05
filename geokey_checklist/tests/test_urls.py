from django.test import TestCase
from django.core.urlresolvers import reverse, resolve

from ..views import (
    IndexPage,
    ChecklistIndexUpdateItems,
    ChecklistAddItem,
    ChecklistDeleteItem,
    ChecklistEditItem,
    ChecklistEditItemVal,
    ChecklistAddChecklist,
    ChecklistDeleteChecklist,
    ChecklistEditChecklist,
    ChecklistChecklistSettings
)


class UrlTest(TestCase):

    def test_index_page(self):
        self.assertEqual(reverse('geokey_checklist:index'), '/admin/checklist/')

        resolved = resolve('/admin/checklist/')
        self.assertEqual(resolved.func.func_name, IndexPage.__name__)

        self.assertEqual(
            reverse('geokey_checklist:index', kwargs={'checklist_id': 1}),
            '/admin/checklist/1/'
        )

        resolved = resolve('/admin/checklist/1/')
        self.assertEqual(resolved.func.func_name, IndexPage.__name__)
        self.assertEqual(resolved.kwargs['checklist_id'], '1')

    def test_checklist_settings(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_settings', kwargs={'project_id': 1}),
            '/admin/checklist/settings/1/'
        )

        resolved = resolve('/admin/checklist/settings/1/')
        self.assertEqual(resolved.func.func_name, ChecklistChecklistSettings.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')

    def test_index_update_items(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_index_update_items', kwargs={'project_id': 1, 'checklist_id': 2}),
            '/admin/checklist/1/2/items/'
        )

        resolved = resolve('/admin/checklist/1/2/items/')
        self.assertEqual(resolved.func.func_name, ChecklistIndexUpdateItems.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')

    def test_add_item(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_add_item', kwargs={'project_id': 1, 'checklist_id': 2}),
            '/admin/checklist/1/2/add-item/'
        )

        resolved = resolve('/admin/checklist/1/2/add-item/')
        self.assertEqual(resolved.func.func_name, ChecklistAddItem.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')

    def test_edit_item(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_edit_item', kwargs={'project_id': 1, 'checklist_id': 2, 'checklist_item_id': 3}),
            '/admin/checklist/1/2/edit-item/3/'
        )

        resolved = resolve('/admin/checklist/1/2/edit-item/3/')
        self.assertEqual(resolved.func.func_name, ChecklistEditItem.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')
        self.assertEqual(resolved.kwargs['checklist_item_id'], '3')

    def test_edit_item_val(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_edit_item_val', kwargs={'project_id': 1, 'checklist_id': 2, 'checklist_item_id': 3, 'checklist_item_field_key': 'haveit', 'checklist_item_field_val': 'True'}),
            '/ajax/admin/checklist/1/2/edit-item-val/3/haveit/True/'
        )

        resolved = resolve('/ajax/admin/checklist/1/2/edit-item-val/3/haveit/True/')
        self.assertEqual(resolved.func.func_name, ChecklistEditItemVal.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')
        self.assertEqual(resolved.kwargs['checklist_item_id'], '3')
        self.assertEqual(resolved.kwargs['checklist_item_field_key'], 'haveit')
        self.assertEqual(resolved.kwargs['checklist_item_field_val'], 'True')

    def test_delete_item(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_delete_item', kwargs={'project_id': 1, 'checklist_id': 2, 'checklist_item_id': 3}),
            '/admin/checklist/1/2/delete-item/3/'
        )

        resolved = resolve('/admin/checklist/1/2/delete-item/3/')
        self.assertEqual(resolved.func.func_name, ChecklistDeleteItem.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')
        self.assertEqual(resolved.kwargs['checklist_item_id'], '3')

    def test_add_checklist(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_add_checklist', kwargs={'project_id': 1}),
            '/admin/checklist/add-checklist/1/'
        )

        resolved = resolve('/admin/checklist/add-checklist/1/')
        self.assertEqual(resolved.func.func_name, ChecklistAddChecklist.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')

    def test_edit_checklist(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_edit_checklist', kwargs={'project_id': 1, 'checklist_id': 2}),
            '/admin/checklist/1/edit-checklist/2/'
        )

        resolved = resolve('/admin/checklist/1/edit-checklist/2/')
        self.assertEqual(resolved.func.func_name, ChecklistEditChecklist.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')

    def test_delete_checklist(self):
        self.assertEqual(
            reverse('geokey_checklist:checklist_delete_checklist', kwargs={'project_id': 1, 'checklist_id': 2}),
            '/admin/checklist/1/delete-checklist/2/'
        )

        resolved = resolve('/admin/checklist/1/delete-checklist/2/')
        self.assertEqual(resolved.func.func_name, ChecklistDeleteChecklist.__name__)
        self.assertEqual(resolved.kwargs['project_id'], '1')
        self.assertEqual(resolved.kwargs['checklist_id'], '2')
