from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import User
# Create your models here.
#Btech is defined as a model and name is the only field in this model
department_values = (
        ('cse', 'Computer Science & Engineering'),
        ('ece', 'Electronics & Communication Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('dd', 'Design'),
        ('bsbe', 'Biosciences & Bioengineering'),
        ('cl', 'Chemical Engineering'),
        ('cst', 'Chemical Science & Technology'),
        ('eee', 'Electronics & Electrical Engineering'),
        ('ma', 'Mathematics & Computing'),
        ('ph', 'Engineering Physics'),
        ('rt', 'Rural Technology'),
        ('hss', 'Humanities & Social Sciences'),
        ('enc', 'Centre for Energy'),
        ('env', 'Centre for Environment'),
        ('nt', 'Centre for Nanotechnology'),
        ('lst', 'Centre for Linguistic Science & Technology')
    )
program_values = (
        ('btech', 'BTech'),
        ('mtech', 'MTech'),
        ('phd', 'PhD'),
        ('msc', 'MSc'),
        ('msr', 'MS-R'),
        ('ma', 'MA'),
        ('bdes', 'BDes'),
        ('mdes', 'MDes')
    )

venue_choices =(
    ('Lecture Hall 1','Lecture Hall 1'),
    ('Lecture Hall 2','Lecture Hall 2'),
    ('Lecture Hall 3','Lecture Hall 3'),
    ('Lecture Hall 4','Lecture Hall 4'),
    ('Conference Room','Conference Room'),
    ('CSE Seminar Room','CSE Seminar Room'),
    ('Core 2 Rooms','Core 2 Rooms'),
    ('Core 5 Rooms','Core 5 Rooms'),
    ('Mini Auditorium','Mini Auditorium'),
    ('Main Auditorium','Main Auditorium'),
    ('Department Library','Department Library'),
    ('None',"None")
)
# Create your models here.
class Btech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#Mtech is defined as a model and name is the only field in this model
class Mtech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#PhD is defined as a model and name is the only field in this model
class PhD(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#Event is defined as a model and name,event_id,fee,capacity etc. are the fields in this model
class Event(models.Model):

    # todo, extend and test by sunday

    name = models.CharField(max_length=300)
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event', blank=True)
    fee = models.PositiveIntegerField()
    capacity  = models.PositiveIntegerField()
    # target_audience = models.CharField(max_length=300)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=True)
    summary = models.TextField(blank=False, null=True)
    faq = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=300, help_text=' (Press Ctrl to select multiple)',blank=True)
    organisors = models.CharField(max_length=300)
    contact_info = models.CharField(max_length=300)
    venue = models.CharField(max_length=50, choices=venue_choices,default='CSE Seminar Room')
    # requester = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, default=None)
    invitees_btech = models.ManyToManyField(Btech, help_text=' (Press Ctrl to select multiple)', blank=True)
    invitees_mtech = models.ManyToManyField(Mtech, help_text=' (Press Ctrl to select multiple)', blank=True)
    invitees_phd = models.ManyToManyField(PhD, blank=True)
    # invitees_btech = models.ManyToManyField(Btech, help_text=' (Press Ctrl to select multiple)')
    comment_for_admin = models.CharField(max_length=300)
    approval = models.CharField(max_length=50, choices = (('Appr','Approved'),('Pend','Pending'),('Decl','Declined')), default='Pend')
    requestor = models.CharField(max_length=100, blank=True)
    curr_audience = models.IntegerField(blank=False, default=0)
    image_string = models.TextField(blank=True, default= "None")
    faq_question_1 = models.CharField(max_length=500,blank=True)
    faq_question_2 = models.CharField(max_length=500,blank=True)
    faq_question_3 = models.CharField(max_length=500,blank=True)
    faq_question_4 = models.CharField(max_length=500,blank=True)
    faq_question_5 = models.CharField(max_length=500,blank=True)


    faq_answer_1 = models.CharField(max_length=500,blank=True)
    faq_answer_2 = models.CharField(max_length=500,blank=True)
    faq_answer_3 = models.CharField(max_length=500,blank=True)
    faq_answer_4 = models.CharField(max_length=500,blank=True)
    faq_answer_5 = models.CharField(max_length=500,blank=True)



    def __str__(self):
         return self.name
#Poll is defined as a model and all the details which are required for polling are added as fields in the model
class Poll(models.Model):

    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,help_text='Unique poll id')
    response_coming = models.PositiveIntegerField()
    response_not_coming  = models.PositiveIntegerField()
    response_not_sure = models.PositiveIntegerField()
    user_id=models.CharField(max_length=300,default='')


    def __str__(self):
        return str(self.event_id)

#Profile is defined as a model and user, department of the user, program, roll number and phone number of the user are the fields in this model

class Profile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=100,blank=False,choices=department_values)
    program = models.CharField(max_length=100,blank=False,choices=program_values)
    roll_no = models.BigIntegerField(unique=True,blank=False)
    phone_no = models.BigIntegerField(blank=False)

    def __str__(self):
        return str(self.user)
#EventFeedback is defined as a model and content, submitter, rating and to which event are the fields in this model
class EventFeedback(models.Model):

    content = models.TextField(blank=False)
    submiter = models.CharField(max_length=100, blank=True)
    rating = models.FloatField()
    to_event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        name = str(self.submiter)+ "<=User|Event=> "+ str(self.to_event)
        return name
#AppFeedback is defined as a model and content is the only field in this model.
class AppFeedback(models.Model):

    content = models.TextField(blank=True)
    rating_ui = models.FloatField(blank=False, default=3.0)
    rating_ux = models.FloatField(blank=False, default=3.0)
    rating_overall = models.FloatField(blank=False, default=3.0)
    submitted_by= models.CharField(max_length=150,blank=False, default='Anonymous')


class Vote(models.Model):
    vote_id=models.UUIDField(primary_key=False, default=uuid.uuid4,help_text='Unique vote id')
    user_id=models.CharField(max_length=300,default='')
    user_vote=models.PositiveIntegerField()

    def __str__(self):
        return str(self.vote_id)
# {
#     "name": "null",
#     "fee": 12,
#     "capacity": 12,
#     "target_audience": "12",
#     "date": "2009-11-11",
#     "time": "12:00",
#     "venue": "L1",
#     "tags": "kl",
#     "invitees_btech": [4],
#     "invitees_mtech": [4],
#     "invitees_phd": [1],
#     "organisors": "jk",
#     "contact_info": "kl",
#     "summary": "kl",
#     "faq": "kl",
#     "comment_for_admin": "kl",
#     "curr_audience": null,
#     "approval": "Pend"
# }