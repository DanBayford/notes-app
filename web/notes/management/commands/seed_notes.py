from django.core.management.base import BaseCommand, CommandError
from users.models import CustomUser
from tags.models import TagModel
from notes.models import NoteModel
from notes.data import notes as _

# raise CommandError('Poll "%s" does not exist' % poll_id)

class Command(BaseCommand):
    help = "Resets the Notes app database"

    def add_arguments(self, parser):
      parser.add_argument(
          "--reset",               # flag name
          action="store_true", 
          help="Reset the current Notes database",
      )

    def handle(self, *args, **options):
        
        all_users = CustomUser.objects.exclude(email='dan@bayford.dev')
        all_notes = NoteModel.objects.all()
        all_tags = TagModel.objects.all()

        self.stdout.write(f"""
        Current database status:

        Users: {all_users.count()}
        Tags: {all_tags.count()}
        Notes: {all_notes.count()}
        """)
        
        # If no reset flag, early return
        if not options['reset']:
           return
        
        else:
           self.stdout.write("Resetting Notes database...")

           # Step 1: Delete all current data 
           all_users.delete()
           # delete.CASCADE should remove associated tags and notes, but just to confirm
           all_tags.delete()
           all_notes.delete()


           # Step 1: Create default user
           user = CustomUser.objects.create(email="dan@notes.com")
           user.set_password('P@ssword!')
           user.save()

           # Step 3: Create tags
           react_tag = TagModel.objects.create(name="React", user=user)
           django_tag = TagModel.objects.create(name="Django", user=user)
           protocols_tag = TagModel.objects.create(name="Protocols", user=user)
           database_tag = TagModel.objects.create(name="Database", user=user)
           docker_tag = TagModel.objects.create(name="Docker", user=user)
           security_tag = TagModel.objects.create(name="Security", user=user)
           python_tag = TagModel.objects.create(name="Python", user=user)
           javascript_tag = TagModel.objects.create(name="JavaScript", user=user)
           css_tag = TagModel.objects.create(name="CSS", user=user)
           

           # Step 4. Create notes
           note_1 = NoteModel.objects.create(title=_.note_1_title, author=user, content=_.note_1_content)
           note_1.tags.set([react_tag, javascript_tag])
           note_2 = NoteModel.objects.create(title=_.note_2_title, author=user, content=_.note_2_content)
           note_2.tags.set([react_tag, javascript_tag])
           note_3 = NoteModel.objects.create(title=_.note_3_title, author=user, content=_.note_3_content)
           note_3.tags.set([docker_tag])
           note_4 = NoteModel.objects.create(title=_.note_4_title, author=user, content=_.note_4_content)
           note_4.tags.set([python_tag])
           note_5 = NoteModel.objects.create(title=_.note_5_title, author=user, content=_.note_5_content)
           note_5.tags.set([protocols_tag, security_tag])
           note_6 = NoteModel.objects.create(title=_.note_6_title, author=user, content=_.note_6_content)
           note_6.tags.set([protocols_tag, security_tag])
           note_7 = NoteModel.objects.create(title=_.note_7_title, author=user, content=_.note_7_content)
           note_7.tags.set([javascript_tag])
           note_8 = NoteModel.objects.create(title=_.note_8_title, author=user, content=_.note_8_content)
           note_8.tags.set([security_tag])
           note_9 = NoteModel.objects.create(title=_.note_9_title, author=user, content=_.note_9_content)
           note_9.tags.set([security_tag])
           note_10 = NoteModel.objects.create(title=_.note_10_title, author=user, content=_.note_10_content)
           note_10.tags.set([security_tag])
           note_11 = NoteModel.objects.create(title=_.note_11_title, author=user, content=_.note_11_content)
           note_11.tags.set([react_tag, javascript_tag])
           note_12 = NoteModel.objects.create(title=_.note_12_title, author=user, content=_.note_12_content)
           note_12.tags.set([django_tag, python_tag])
           note_13 = NoteModel.objects.create(title=_.note_13_title, author=user, content=_.note_13_content)
           note_13.tags.set([security_tag])
           note_14 = NoteModel.objects.create(title=_.note_14_title, author=user, content=_.note_14_content)
           note_14.tags.set([django_tag, python_tag])
           note_15 = NoteModel.objects.create(title=_.note_15_title, author=user, content=_.note_15_content)
           note_15.tags.set([docker_tag])
           note_16 = NoteModel.objects.create(title=_.note_16_title, author=user, content=_.note_16_content)
           note_16.tags.set([css_tag])
           note_17 = NoteModel.objects.create(title=_.note_17_title, author=user, content=_.note_17_content)
           note_17.tags.set([database_tag])
           note_18 = NoteModel.objects.create(title=_.note_18_title, author=user, content=_.note_18_content)
           note_18.tags.set([javascript_tag])
           note_19 = NoteModel.objects.create(title=_.note_19_title, author=user, content=_.note_19_content)
           note_19.tags.set([react_tag, javascript_tag])
           note_20 = NoteModel.objects.create(title=_.note_20_title, author=user, content=_.note_20_content)
           note_20.tags.set([security_tag])
           note_21 = NoteModel.objects.create(title=_.note_21_title, author=user, content=_.note_21_content)
           note_21.tags.set([django_tag, python_tag])
           note_22 = NoteModel.objects.create(title=_.note_22_title, author=user, content=_.note_22_content)
           note_22.tags.set([javascript_tag])

           self.stdout.write(self.style.SUCCESS('Successfully reset database'))