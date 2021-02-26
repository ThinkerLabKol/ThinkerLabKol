from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Lessons, MyModelAdmin)
admin.site.register(Reviews)
admin.site.register(Membership)
admin.site.register(CourseRegistration)