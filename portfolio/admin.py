from django.contrib import admin
from .models import * 
admin.site.register(Contact)
admin.site.register(Blogs)
# admin.site.register(Internship)

class InternshipAdmin(admin.ModelAdmin):
    list_display=( 'fullname','usn','email', 'college_name','offer_status','start_date','proj_report','timeStamp')
    
    search_fields=('fullname','usn','email')
    list_filter=['college_name','proj_report','offer_status']
# Register your models here.


   
   
admin.site.register(Internship,InternshipAdmin)