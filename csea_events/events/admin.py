from django.contrib import admin
from events.models import Event, Btech, Mtech, PhD, AppFeedback, Profile, EventFeedback
# Register your models here.

class EventAdmin(admin.ModelAdmin):  
  list_display = ('approval','name','date','time')
  ordering = ('approval',) # The negative sign indicate descendent order

admin.site.register(EventFeedback)

admin.site.register(Event, EventAdmin)

admin.site.register(Btech)

admin.site.register(Mtech)

admin.site.register(PhD)

admin.site.register(AppFeedback)

admin.site.register(Profile)