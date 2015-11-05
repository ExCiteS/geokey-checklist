from datetime import datetime
from datetime import timedelta
from pytz import utc

from django.core import mail
from django.core.management.base import NoArgsCommand

from geokey.projects.models import Project
from geokey.users.models import User

from geokey_checklist.models import ChecklistSettings
from geokey_checklist.models import Checklist
from geokey_checklist.models import ChecklistItem

class Command(NoArgsCommand):

    def get_expired_items(self, project, user):
        """
        Returns all Checklists' expired items for a user
        """
        expired_items = []
        now = datetime.utcnow()
        checklistItems = ChecklistItem.objects.filter(creator=user, project=project, haveit=True) #need to add user so we only get the users's items, not EVERYONE's items

        for item in checklistItems:
            if item.expiry < utc.localize(now):
                expired_items.append(item)

        return expired_items

    def send_expired_reminder(self, user):
        """
        Creates an email to send to a user about the items
        from their Checklists that have expired. These emails
        will be sent at the specified frequency, as set in their
        ChecklistSettings. Should no items from any of the checklists
        be expired, no email will be sent.
        """
        projects = Project.objects.get_list(user)
        for project in projects:
            if project.name == "MyChecklist":

                expired_items = self.get_expired_items(project, user)
                now = datetime.utcnow()

                checklist_settings = ChecklistSettings.objects.get(project=project)
                frequencyonexpiration = checklist_settings.frequencyonexpiration
                #print "frequencyonexpiration: ", frequencyonexpiration
                lastremindercheck = checklist_settings.lastremindercheck
                #print "lastremindercheck: ", lastremindercheck
                next_reminder_date = None
                if lastremindercheck != None:
                    next_reminder_date = timedelta(days=int(frequencyonexpiration)) + lastremindercheck

                #print "next_reminder_date: ", next_reminder_date

                #if next_reminder_date == None:
                if True:

                    if len(expired_items) > 0:
                        messages = []
                        message_str = "Dear " + user.display_name + ",\nThe following items from your checklists have expired:\n"
                        for item in expired_items:
                            message_str += "-" + item.name + ":" + str(item.quantity) + " " + str(item.quantityunit) + " (expired - " + str(item.expiry.date()) + ")" + "\n"
                        message_str += "\nPlease update these items as soon as you can."

                        messages.append(
                            mail.EmailMessage(
                                "Expired Checklist Items",
                                message_str,
                                "challenging-risk@ucl.ac.uk",
                                [user.email]
                            )
                        )

                        if len(messages) > 0:
                            connection = mail.get_connection()
                            connection.open()
                            connection.send_messages(messages)
                            connection.close()

                    setattr(checklist_settings, "lastremindercheck", datetime.now())
                    checklist_settings.save()
                    #print "no last reminder, reminder sent and lastremindercheck updated"

                elif next_reminder_date < utc.localize(now):

                    if len(expired_items) > 0:
                        messages = []
                        message_str = "Dear " + user.display_name + ",\nThe following items from your checklists have expired:\n"
                        for item in expired_items:
                            message_str += "-" + item.name + ":" + str(item.quantity) + " " + str(item.quantityunit) + " (expired - " + str(item.expiry.date()) + ")" + "\n"
                        message_str += "\nPlease update these items as soon as you can."

                        messages.append(
                            mail.EmailMessage(
                                "Expired Checklist Items",
                                message_str,
                                "challenging-risk@ucl.ac.uk",
                                [user.email]
                            )
                        )

                        if len(messages) > 0:
                            connection = mail.get_connection()
                            connection.open()
                            connection.send_messages(messages)
                            connection.close()

                    setattr(checklist_settings, "lastremindercheck", datetime.now())
                    checklist_settings.save()
                    #print "past date of setting for last reminder, reminder sent and lastremindercheck updated"

    def handle(self, *args, **options):
        """
        Executes the code below when the command is run.
        """
        #Note: the idea is for this to be called as a chron job and to loop through all users to send the emails at once

        for user in User.objects.exclude(display_name='AnonymousUser'):
            self.send_expired_reminder(user)
