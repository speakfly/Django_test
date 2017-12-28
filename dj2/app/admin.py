from django.contrib import admin
from .models import Academy,Major,Grade,Apartment,Room,Student,Notice,Repair


class AcademyAdmin(admin.ModelAdmin):
	list_display  = ('aca_name','aca_tele')
	search_fields = ('aca_name','aca_tele')
	suit_form_tabs = (('major', 'Major'), ('grade', 'Grade'),
		)
class MajorAdmin(admin.ModelAdmin):
	list_display  = ('maj_name','aca_name')
	search_fields = ('maj_name',)
class GradeAdmin(admin.ModelAdmin):
	list_display  = ('gra_name','maj_name')
	search_fields = ('gra_name',)
class ApartmentAdmin(admin.ModelAdmin):
	list_display  = ('apa_name','room_num','bed_num')
	search_fields = ('apa_name','room_num','bed_num')
class RoomAdmin(admin.ModelAdmin):
	list_display  = ('room_id','room_num','apa_name')
	search_fields = ('room_id','room_num')
class StudentAdmin(admin.ModelAdmin):
	list_display  = ('stu_id','stu_name','room_id','statu')
	search_fields = ('stu_id','stu_name')
class NoticeAdmin(admin.ModelAdmin):
	list_display  = ('title','author','cre_date')
	search_fields = ('title','author','cre_date')
class RepairAdmin(admin.ModelAdmin):
	list_display  = ('id','rep_type','room_id','cre_date','fin_date','statu')
	search_fields = ('id','rep_type','room_id','cre_date','fin_date','statu')
	list_editable = ('statu',)


admin.site.register(Academy,AcademyAdmin)
admin.site.register(Major,MajorAdmin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Apartment,ApartmentAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Repair,RepairAdmin)

