from django.contrib import admin
from .models import Academy,Major,Grade,Apartment,Room,Student,Notice,Repair
import csv
import datetime
from django.http import HttpResponse
import codecs

def export_to_csv(modeladmin, request, queryset):
	opts=modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	response.write(codecs.BOM_UTF8)
	# response=HttpResponse(content_type='text/csv')
	# response['Content-Disposition']='attachment;filename={}.csv'.format(opts.verbose_name)
	writer=csv.writer(response)
	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# writer.writerow([field.verbose_name.encode('utf-8') for field in fields])
	writer.writerow([field.verbose_name for field in fields])
	# writer.writerow([field.verbose_name.encode('gb2312') for field in fields])
	for obj in queryset:
		data_row=[]
		for field in fields:
			value=getattr(obj,field.name)
			if isinstance(value,datetime.datetime):
				value=value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_description = '导出CSV'




class AcademyAdmin(admin.ModelAdmin):
	list_display  = ('aca_name','aca_tele')
	search_fields = ('aca_name','aca_tele')
	actions = [export_to_csv]
class MajorAdmin(admin.ModelAdmin):
	list_display  = ('maj_name','aca_name')
	search_fields = ('maj_name',)
	actions = [export_to_csv]
class GradeAdmin(admin.ModelAdmin):
	list_display  = ('gra_name','maj_name')
	search_fields = ('gra_name',)
	actions = [export_to_csv]
class ApartmentAdmin(admin.ModelAdmin):
	list_display  = ('apa_name','room_num','bed_num')
	search_fields = ('apa_name','room_num','bed_num')
	actions = [export_to_csv]
class RoomAdmin(admin.ModelAdmin):
	list_display  = ('room_id','room_num','apa_name')
	search_fields = ('room_id','room_num')
	actions = [export_to_csv]
class StudentAdmin(admin.ModelAdmin):
	list_display  = ('stu_id','stu_name','room_id','statu','gra_name')
	search_fields = ('stu_id','stu_name','gra_name__gra_name')
	actions = [export_to_csv]
class NoticeAdmin(admin.ModelAdmin):
	list_display  = ('title','author','cre_date')
	search_fields = ('title','author','cre_date')
	actions = [export_to_csv]
class RepairAdmin(admin.ModelAdmin):
	list_display  = ('id','rep_type','room_id','cre_date','fin_date','statu')
	search_fields = ('id','rep_type','room_id','cre_date','fin_date','statu')
	list_editable = ('statu',)
	actions = [export_to_csv]






admin.site.register(Academy,AcademyAdmin)
admin.site.register(Major,MajorAdmin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Apartment,ApartmentAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Notice,NoticeAdmin)
admin.site.register(Repair,RepairAdmin)

