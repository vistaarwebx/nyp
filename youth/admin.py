from django.contrib import admin
from youth.models import*
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)
admin.site.register(Group)
admin.site.register(Groupadmin)
admin.site.register(Member)
admin.site.register(Facebook)
admin.site.register(Posts)
admin.site.register(Books)
admin.site.register(Gallery)
admin.site.register(Press)
admin.site.register(Test)
admin.site.register(VOLUNTEERS)
admin.site.register(JOBINTERNSHIP)


