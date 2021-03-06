import json
import datetime
import math

from braces.views import LoginRequiredMixin

from django.contrib import messages
from django.contrib.gis.geos import GEOSGeometry, Point
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from rest_framework.views import APIView

from geokey.core.decorators import handle_exceptions_for_ajax
from geokey.projects.models import Project
from geokey.categories.models import Category, Field
from geokey.contributions.models import Location, Observation

from .base import (
    TYPE,
    ITEM_TYPE,
    EXPIRY_FACTOR,
    PER_TYPE,
    FREQUENCY_EXPIRED_REMINDER,
    DEFAULT_ITEMS
)
from .models import Checklist, ChecklistItem, ChecklistSettings


error_description_checklist = 'You must be creator of the Checklist.'
error_description_item = 'You must be creator of the Checklist Item.'


class ChecklistObjectMixin(object):

    def get_context_data(self, project_id, checklist_id, **kwargs):
        try:
            checklist = Category.objects.get_single(
                self.request.user,
                project_id,
                checklist_id
            )

            if checklist.creator != self.request.user:
                return {
                    'error': 'Permission denied.',
                    'error_description': error_description_checklist
                }
            else:
                return super(ChecklistObjectMixin, self).get_context_data(
                    checklist=checklist,
                    **kwargs
                )
        except Checklist.DoesNotExist:
            return {
                'error_description': 'Checklist not found.',
                'error': 'Not found.'
            }


class ChecklistItemObjectMixin(object):

    def get_context_data(self, checklist_item_id, **kwargs):
        try:
            checklist_item = ChecklistItem.objects.get(pk=checklist_item_id)

            if checklist_item.creator != self.request.user:
                return {
                    'error': 'Permission denied.',
                    'error_description': error_description_item
                }
            else:
                return super(ChecklistItemObjectMixin, self).get_context_data(
                    checklist_item=checklist_item,
                    **kwargs
                )
        except ChecklistItem.DoesNotExist:
            return {
                'error_description': 'Checklist Item not found.',
                'error': 'Not found.'
            }


class IndexPage(LoginRequiredMixin, TemplateView, ChecklistItemObjectMixin):

    template_name = 'checklist_index.html'

    def get_context_data(self, *args, **kwargs):
        projects = Project.objects.filter(
            creator=self.request.user,
            name="MyChecklist"
        )
        project = None
        # checklist_settings = None
        if projects:
            project = projects[0]
            # checklist_settings = ChecklistSettings.objects.get(project=project)

        categories = None
        if project:
            categories = Category.objects.get_list(
                self.request.user,
                project.id
            )

        return super(IndexPage, self).get_context_data(
            project=project,
            categories=categories,
            # checklist_settings=checklist_settings,
            itemTypeChoices=ITEM_TYPE,
            *args,
            **kwargs
        )


class ChecklistChecklistSettings(LoginRequiredMixin, TemplateView):

    template_name = 'checklist_settings.html'

    def get_context_data(self, project_id, *args, **kwargs):
        project = Project.objects.get_single(self.request.user, project_id)
        try:
            checklist_settings = ChecklistSettings.objects.get(project=project)
        except:
            checklist_settings = None

        # reminderBeforeExpirationChoices = REMINDER_BEFORE_EXPIRATION

        return super(ChecklistChecklistSettings, self).get_context_data(
            project=project,
            checklist_settings=checklist_settings,
            frequencyExpiredReminderChoices=FREQUENCY_EXPIRED_REMINDER,
            # reminderBeforeExpirationChoices=reminderBeforeExpirationChoices,
            *args,
            **kwargs
        )

    def post(self, request, project_id):
        project = Project.objects.get_single(self.request.user, project_id)
        try:
            checklist_settings = ChecklistSettings.objects.get(project=project)
        except:
            checklist_settings = None

        if checklist_settings is not None:
            reminderson_radio = self.request.POST.get('checklistRemindersOn')
            reminderson = True
            if reminderson_radio == "No":
                reminderson = False
            # frequencybeforeexpiration = self.request.POST.get('checklistReminderBeforeExpiration')
            frequencyonexpiration = self.request.POST.get(
                'checklistReminderAfterExpiration'
            )

            setattr(checklist_settings, "reminderson", reminderson)
            #s etattr(checklist_settings, "frequencybeforeexpiration", frequencybeforeexpiration)
            setattr(checklist_settings, "frequencyonexpiration", frequencyonexpiration)
            checklist_settings.save()

            successful_message = "Settings have been saved."
            messages.success(self.request, successful_message)
            return redirect('geokey_checklist:index')

        else:
            error_message = "There was an error in attempting to save your settings. Please contact the system administrator for further assistance."
            messages.error(self.request, error_message)
            return redirect('geokey_checklist:index')

class ChecklistIndexUpdateItems(LoginRequiredMixin, APIView, ChecklistItemObjectMixin):

    @handle_exceptions_for_ajax
    def get(self, request, project_id, checklist_id):
        category = Category.objects.get_single(self.request.user, project_id, checklist_id)

        checklistItems = ChecklistItem.objects.filter(creator=self.request.user, category=category)
        checklistItems_dict = {}
        for checklistItem in checklistItems:
            checklistItem_dict={}
            cid_key = -1
            attrs = vars(checklistItem)
            for key in attrs:
                if(key != "_state"):
                    val = attrs[key]
                    if(key == "id"):
                        cid_key = attrs[key]
                    if(key == "expiry"):
                        if(type(val) == datetime.datetime):
                            val = str(val.date())
                    checklistItem_dict[key] = val

            checklistItems_dict[cid_key] = checklistItem_dict

        return HttpResponse(json.dumps(checklistItems_dict))

class ChecklistAddItem(TemplateView):
    template_name = 'checklist_add_item.html'

    def get_context_data(self, project_id, checklist_id, *args, **kwargs):
        category = Category.objects.get_single(self.request.user, project_id, checklist_id)
        expiryFactorChoices = EXPIRY_FACTOR
        itemTypeChoices = ITEM_TYPE
        perTypeChoices = PER_TYPE

        return super(ChecklistAddItem, self).get_context_data(
            category=category,
            expiryFactorChoices=expiryFactorChoices,
            itemTypeChoices=itemTypeChoices,
            perTypeChoices=perTypeChoices,
            *args,
            **kwargs
        )

    def post(self, request, project_id, checklist_id):
        project = Project.objects.get_single(self.request.user, project_id)
        category = Category.objects.get_single(self.request.user, project_id, checklist_id)
        checklist = Checklist.objects.get(project=project,category=category)
        numberofpeople = checklist.numberofpeople
        numberofchildren = checklist.numberofchildren
        numberoftoddlers = checklist.numberoftoddlers
        numberofinfants = checklist.numberofinfants
        numberofpets = checklist.numberofpets

        name = self.request.POST.get('checklistItemName')
        project = Project.objects.get_single(self.request.user, project_id)
        category = Category.objects.get_single(
            self.request.user,
            project_id,
            checklist_id
        )
        creator = self.request.user

        checklistitemtype = self.request.POST.get('checklistItemType')

        checklistitemdescription = self.request.POST.get('checklistItemDescription')
        checklistitemurl = self.request.POST.get('checklistItemURL')
        quantityfactor_str = self.request.POST.get('checklistItemQuantityFactor')
        quantityfactor = int(quantityfactor_str)

        pertype = self.request.POST.get('checklistItemPerType')

        quantityunit = self.request.POST.get('checklistItemQuantityUnit')
        expiryfactor = self.request.POST.get('checklistItemExpiry')
        expiry = None
        haveit = False

        totalnumber = 1
        quantity = 0

        if checklistitemtype == "Essential" or checklistitemtype == "Useful" or checklistitemtype == "Personal":
            totalnumber_float = float(numberofpeople) + (float(numberofchildren) * 0.5) + (float(numberoftoddlers) * 0.3) + (float(numberofinfants) * 0.1) + (float(numberofpets) * 0.1)
            totalnumber = int(math.ceil(totalnumber_float))
        elif checklistitemtype == "Children":
            totalnumber = numberofchildren
        elif checklistitemtype == "Toddlers":
            totalnumber = numberoftoddlers
        elif checklistitemtype == "Infants":
            totalnumber = numberofinfants
        elif checklistitemtype == "Pets":
            totalnumber = numberofpets
        else:
            totalnumber = 1 #for 'Custom' or 'Fixit'

        if pertype == "location":
            quantity = quantityfactor # this is for an item per household (e.g. first aid kit)
        else:
            quantity = totalnumber * quantityfactor # this is for an item per member of household (e.g. water)

        field = Field.create(name, name, "", False, category, 'TextField')

        checklist_item = ChecklistItem.objects.create(
            name=name,
            project=project,
            category=category,
            field=field,
            creator=creator,
            #checklisttype=checklisttype,
            checklistitemdescription=checklistitemdescription,
            checklistitemurl=checklistitemurl,
            checklistitemtype=checklistitemtype,
            quantityfactor=quantityfactor,
            pertype=pertype,
            quantity=quantity,
            quantityunit=quantityunit,
            expiryfactor=expiryfactor,
            expiry=expiry,
            haveit=haveit
        )
        successful_message = checklist_item.name + " has been added."
        messages.success(self.request, successful_message)
        return redirect('geokey_checklist:index', checklist_id=category.id)

class ChecklistDeleteItem(LoginRequiredMixin, ChecklistItemObjectMixin, TemplateView):
    template_name = 'base.html'

    def get(self, request, checklist_item_id, project_id, checklist_id):
        context = self.get_context_data(checklist_item_id)
        checklist_item = context.pop('checklist_item', None)
        successful_message = checklist_item.name + " has been deleted."

        field = checklist_item.field

        if checklist_item is not None:
            field.delete()
            checklist_item.delete()

            messages.success(self.request, successful_message)
            return redirect('geokey_checklist:index', checklist_id=checklist_id)

        return self.render_to_response(context)

class ChecklistEditItemVal(LoginRequiredMixin, ChecklistItemObjectMixin, TemplateView):
    template_name = 'base.html'

    def get(self, request, project_id, checklist_id, checklist_item_id, checklist_item_field_key, checklist_item_field_val):
        checklist_item = ChecklistItem.objects.get(project_id=project_id, category_id=checklist_id, pk=checklist_item_id)

        checklist_item_update_dict = {}

        if checklist_item_field_key == "haveit":
            if checklist_item_field_val == "True":
                expiryfactor = checklist_item.expiryfactor
                expiry = datetime.timedelta(days=int(expiryfactor)) + datetime.datetime.now()
                checklist_item_update_dict = {
                    checklist_item_field_key: checklist_item_field_val,
                    "expiry": expiry
                }
            else:
                checklist_item_update_dict = {
                    checklist_item_field_key: checklist_item_field_val,
                    "expiry": None
                }
        else:
            checklist_item_update_dict = {
                checklist_item_field_key: checklist_item_field_val
            }


        checklist_item.update(checklist_item_update_dict)

        return redirect('geokey_checklist:index', checklist_id=checklist_id)

class ChecklistEditItem(LoginRequiredMixin, ChecklistItemObjectMixin, TemplateView):
    template_name = 'checklist_edit_item.html'

    def get_context_data(self, project_id, checklist_id, *args, **kwargs):
        category = Category.objects.get_single(self.request.user, project_id, checklist_id)
        expiryFactorChoices = EXPIRY_FACTOR
        itemTypeChoices = ITEM_TYPE
        perTypeChoices = PER_TYPE

        return super(ChecklistEditItem, self).get_context_data(
            category=category,
            expiryFactorChoices=expiryFactorChoices,
            itemTypeChoices=itemTypeChoices,
            perTypeChoices=perTypeChoices,
            *args,
            **kwargs
        )

    def post(self, request, project_id, checklist_id, checklist_item_id):
        project = Project.objects.get_single(self.request.user, project_id)
        category = Category.objects.get_single(self.request.user, project_id, checklist_id)
        checklist = Checklist.objects.get(project=project,category=category)
        numberofpeople = checklist.numberofpeople
        numberofchildren = checklist.numberofchildren
        numberoftoddlers = checklist.numberoftoddlers
        numberofinfants = checklist.numberofinfants
        numberofpets = checklist.numberofpets

        name = self.request.POST.get('checklistItemName')
        checklistitemdescription = self.request.POST.get('checklistItemDescription')
        checklistitemurl = self.request.POST.get('checklistItemURL')
        checklistitemtype = self.request.POST.get('checklistItemType')
        quantityfactor_str = self.request.POST.get('checklistItemQuantityFactor')
        quantityfactor = int(quantityfactor_str)

        pertype = self.request.POST.get('checklistItemPerType')

        quantityunit = self.request.POST.get('checklistItemQuantityUnit')
        expiryfactor = self.request.POST.get('checklistItemExpiry')
        expiry = None

        checklist_item = ChecklistItem.objects.get(pk=checklist_item_id)
        if checklist_item.haveit == True:
            expiry = datetime.timedelta(days=int(expiryfactor)) + datetime.datetime.now();

        totalnumber = 1
        quantity = 0

        if checklistitemtype == "Essential" or checklistitemtype == "Useful" or checklistitemtype == "Personal":
            totalnumber_float = float(numberofpeople) + (float(numberofchildren) * 0.5) + (float(numberoftoddlers) * 0.3) + (float(numberofinfants) * 0.1) + (float(numberofpets) * 0.1)
            totalnumber = int(math.ceil(totalnumber_float))
        elif checklistitemtype == "Children":
            totalnumber = numberofchildren
        elif checklistitemtype == "Toddlers":
            totalnumber = numberoftoddlers
        elif checklistitemtype == "Infants":
            totalnumber = numberofinfants
        elif checklistitemtype == "Pets":
            totalnumber = numberofpets
        else:
            totalnumber = 1 #for 'Custom' or 'Fixit'

        if pertype == "location":
            quantity = quantityfactor # this is for an item per household (e.g. first aid kit)
        else:
            quantity = totalnumber * quantityfactor # this is for an item per member of household (e.g. water)

        field = checklist_item.field
        setattr(field, "name", name)
        setattr(field, "key", name)
        field.save()

        checklist_item_update_dict = {
            "name": name,
            "checklistitemdescription": checklistitemdescription,
            "checklistitemurl": checklistitemurl,
            "checklistitemtype": checklistitemtype,
            "quantityfactor": quantityfactor,
            "pertype": pertype,
            "quantity": quantity,
            "quantityunit": quantityunit,
            "expiryfactor": expiryfactor,
            "expiry":expiry
        }
        checklist_item.update(checklist_item_update_dict)

        successful_message = checklist_item.name + " has been updated."
        messages.success(self.request, successful_message)
        return redirect('geokey_checklist:index', checklist_id=checklist_id)

class ChecklistAddChecklist(TemplateView):
    template_name = 'checklist_add_checklist.html'

    def get_context_data(self, project_id, *args, **kwargs):
        typeChoices = TYPE

        return super(ChecklistAddChecklist, self).get_context_data(
            project_id=project_id,
            typeChoices=typeChoices,
            *args,
            **kwargs
        )

    def post(self, request, project_id):
        name = self.request.POST.get('checklistName')
        description = self.request.POST.get('checklistDescription')
        creator = self.request.user
        project = None
        checklist_settings = None

        #not the most robust method; need to rework...
        if int(project_id) == 999999:
            project = Project.create("MyChecklist", "", True, False, 'auth', creator) #can be true, auth, or false
            checklist_settings = ChecklistSettings.objects.create(
                project=project,
                reminderson=True,
                frequencyonexpiration='twice',
                #frequencybeforeexpiration='one_week'
            )
        else:
            project = Project.objects.get_single(self.request.user, project_id)
            checklist_settings = ChecklistSettings.objects.get(project=project)

        default_status = 'active' #can be 'active' or 'pending'

        category = Category.objects.create(
            project=project,
            creator=creator,
            name=name,
            description=description,
            default_status=default_status
        )

        latitude = self.request.POST.get('checklistLat')
        longitude = self.request.POST.get('checklistLng')
        geom_point = Point((float(longitude), float(latitude)))
        geometry = GEOSGeometry(geom_point)
        created_at = datetime.datetime.now()
        location_status = 'active' #can be 'active' or 'pending'

        location = Location.objects.create(
            name=name,
            description=description,
            geometry=geometry,
            created_at=created_at,
            creator=creator,
            private_for_project=project,
            status=location_status
        )

        data = {} #e.g. {'text': 'Text', 'number': 12}
        observation_status = 'active' #can be 'active' or 'pending'

        observation = Observation.create(
            properties=data,
            creator=creator,
            location=location,
            project=project,
            category=category,
            status=observation_status
        )

        checklisttype = self.request.POST.get('checklistType')
        numberofpeople = self.request.POST.get('checklistNumPeople')
        numberofchildren = self.request.POST.get('checklistNumChildren')
        numberoftoddlers = self.request.POST.get('checklistNumToddlers')
        numberofinfants = self.request.POST.get('checklistNumInfants')
        numberofpets = self.request.POST.get('checklistNumPets')

        checklist = Checklist.objects.create(
            name=name,
            description=description,
            project=project,
            category=category,
            creator=creator,
            checklisttype=checklisttype,
            numberofpeople=numberofpeople,
            numberofchildren=numberofchildren,
            numberoftoddlers=numberoftoddlers,
            numberofinfants=numberofinfants,
            numberofpets=numberofpets,
            latitude=latitude,
            longitude=longitude
        )

        default_items = DEFAULT_ITEMS

        for item_dict in default_items:

            dict_checklisttype = ""
            dict_name = ""
            dict_checklistitemdescription = ""
            dict_checklistitemurl = ""
            dict_checklistitemtype = ""
            dict_quantityfactor = ""
            dict_pertype = ""
            dict_quantityunit = ""
            dict_expiryfactor = ""

            for key in item_dict:
                if key == "checklisttype":
                    dict_checklisttype = item_dict[key]
                elif key == "name":
                    dict_name = item_dict[key]
                elif key == "checklistitemdescription":
                    dict_checklistitemdescription = item_dict[key]
                elif key == "checklistitemurl":
                    dict_checklistitemurl = item_dict[key]
                elif key == "checklistitemtype":
                    dict_checklistitemtype = item_dict[key]
                elif key == "quantityfactor":
                    dict_quantityfactor = item_dict[key]
                elif key == "pertype":
                    dict_pertype = item_dict[key]
                elif key == "quantityunit":
                    dict_quantityunit = item_dict[key]
                elif key == "expiryfactor":
                    dict_expiryfactor = item_dict[key]

            #create the default items from the given values
            if dict_checklisttype == checklisttype:
                totalnumber = 1
                quantity = 0

                if dict_checklistitemtype == "Essential" or dict_checklistitemtype == "Useful" or dict_checklistitemtype == "Personal":
                    totalnumber_float = float(numberofpeople) + (float(numberofchildren) * 0.5) + (float(numberoftoddlers) * 0.3) + (float(numberofinfants) * 0.1) + (float(numberofpets) * 0.1)
                    totalnumber = int(math.ceil(totalnumber_float))
                elif dict_checklistitemtype == "Children":
                    totalnumber = int(numberofchildren)
                elif dict_checklistitemtype == "Toddlers":
                    totalnumber = int(numberoftoddlers)
                elif dict_checklistitemtype == "Infants":
                    totalnumber = int(numberofinfants)
                elif dict_checklistitemtype == "Pets":
                    totalnumber = int(numberofpets)
                else:
                    totalnumber = 1  # for 'Custom' or 'Fixit'

                if dict_pertype == "location":
                    quantity = int(dict_quantityfactor)  # this is for an item per household (e.g. first aid kit)
                else:
                    quantity = totalnumber * int(dict_quantityfactor)  # this is for an item per member of household (e.g. water)

                if quantity > 0:
                    field = Field.create(dict_name, dict_name, "", False, category, 'TextField')

                    checklist_item = ChecklistItem.objects.create(
                        name=dict_name,
                        project=project,
                        category=category,
                        field=field,
                        creator=creator,
                        # checklisttype=checklisttype,
                        checklistitemdescription=dict_checklistitemdescription,
                        checklistitemurl=dict_checklistitemurl,
                        checklistitemtype=dict_checklistitemtype,
                        quantityfactor=dict_quantityfactor,
                        pertype=dict_pertype,
                        quantity=quantity,
                        quantityunit=dict_quantityunit,
                        expiryfactor=dict_expiryfactor,
                        expiry=None,
                        haveit=False
                    )

        successful_message = checklist.name + " has been added."
        messages.success(self.request, successful_message)
        return redirect('geokey_checklist:index', checklist_id=category.id)


class ChecklistEditChecklist(LoginRequiredMixin, TemplateView): #add ChecklistObjectMixin back later...
    template_name = 'checklist_edit_checklist.html'

    def get_context_data(self, project_id, checklist_id, *args, **kwargs):
        category = Category.objects.get_single(
            self.request.user,
            project_id,
            checklist_id
        )
        project = Project.objects.get_single(self.request.user, project_id)
        checklist = Checklist.objects.get(project=project, category=category)

        return super(ChecklistEditChecklist, self).get_context_data(
            category=category,
            checklist=checklist,
            project_id=project_id,
            checklist_id=checklist_id,
            *args,
            **kwargs
        )

    def post(self, request, project_id, checklist_id):
        name = self.request.POST.get('checklistName')
        description = self.request.POST.get('checklistDescription')

        category = Category.objects.get_single(
            self.request.user,
            project_id,
            checklist_id
        )
        project = Project.objects.get_single(self.request.user, project_id)
        checklist = Checklist.objects.get(
            project=project,
            category=category
        )

        observation = Observation.objects.get(
            project=project,
            category=category
        )
        location = observation.location

        numberofpeople = self.request.POST.get('checklistNumPeople')
        numberofchildren = self.request.POST.get('checklistNumChildren')
        numberoftoddlers = self.request.POST.get('checklistNumToddlers')
        numberofinfants = self.request.POST.get('checklistNumInfants')
        numberofpets = self.request.POST.get('checklistNumPets')

        latitude = self.request.POST.get('checklistLat')
        longitude = self.request.POST.get('checklistLng')
        geom_point = Point((float(longitude), float(latitude)))
        geometry = GEOSGeometry(geom_point)

        setattr(category, "name", name)
        setattr(category, "description", description)
        category.save()

        setattr(checklist, "name", name)
        setattr(checklist, "description", description)

        setattr(checklist, "numberofpeople", numberofpeople)
        setattr(checklist, "numberofchildren", numberofchildren)
        setattr(checklist, "numberoftoddlers", numberoftoddlers)
        setattr(checklist, "numberofinfants", numberofinfants)
        setattr(checklist, "numberofpets", numberofpets)

        setattr(checklist, "latitude", latitude)
        setattr(checklist, "longitude", longitude)
        checklist.save()

        setattr(location, "name", name)
        setattr(location, "description", description)
        setattr(location, "geometry", geometry)
        location.save()

        # now loop through every checklist item in this checklist and update the quantity based on the new number of people, etc.
        checklist_items = ChecklistItem.objects.filter(
            project=project,
            category=category
        )

        for checklistItem in checklist_items:

            checklistitemtype = checklistItem.checklistitemtype
            quantityfactor = checklistItem.quantityfactor

            totalnumber = 1
            quantity = 0

            if checklistitemtype == "Essential" or checklistitemtype == "Useful" or checklistitemtype == "Personal":
                totalnumber_float = float(numberofpeople) + (float(numberofchildren) * 0.5) + (float(numberoftoddlers) * 0.3) + (float(numberofinfants) * 0.1) + (float(numberofpets) * 0.1)
                totalnumber = int(math.ceil(totalnumber_float))
            elif checklistitemtype == "Children":
                totalnumber = int(numberofchildren)
            elif checklistitemtype == "Toddlers":
                totalnumber = int(numberoftoddlers)
            elif checklistitemtype == "Infants":
                totalnumber = int(numberofinfants)
            elif checklistitemtype == "Pets":
                totalnumber = int(numberofpets)
            else:
                totalnumber = 1  # for 'Custom' or 'Fixit'

            if quantityfactor == 0:
                quantity = 1  # item per household (e.g. first aid kit)
            else:
                quantity = totalnumber * quantityfactor  # item per member

            setattr(checklistItem, "quantity", quantity)
            checklistItem.save()

        successful_message = checklist.name + " has been updated."
        messages.success(self.request, successful_message)
        return redirect('geokey_checklist:index', checklist_id=checklist_id)


class ChecklistDeleteChecklist(LoginRequiredMixin, ChecklistObjectMixin,
                               TemplateView):

    template_name = 'base.html'

    def get(self, request, project_id, checklist_id):
        context = self.get_context_data(project_id, checklist_id)
        category = context.pop('checklist', None)

        project = Project.objects.get_single(self.request.user, project_id)
        checklist = Checklist.objects.get(project=project, category=category)

        successful_message = checklist.name + " has been deleted."

        if category is not None:
            category.delete()

            if checklist is not None:
                checklist.delete()

            messages.success(self.request, successful_message)
            return redirect('geokey_checklist:index')

        return self.render_to_response(context)
