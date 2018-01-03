from django.contrib import admin
from .models import Department,Profession,Enployee,Promotion,Train,Checking_in,Money,Workshop,Sales,Logistics
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




class DepartmentAdmin(admin.ModelAdmin):
	list_display  = ('dep_name','dep_tele')
	search_fields = ('dep_name','dep_tele')
	actions = [export_to_csv]
admin.site.register(Department,DepartmentAdmin)

class ProfessionAdmin(admin.ModelAdmin):
	list_display  = ('pro_name','dep_name')
	search_fields = ('pro_name','dep_name__dep_name')
	actions = [export_to_csv]
admin.site.register(Profession,ProfessionAdmin)

class EnployeeAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','enp_name','enp_wage','enp_prof','sta_date','end_date')
	search_fields = ('enp_id','enp_name','enp_wage','sta_date','end_date','enp_prof__pro_name')
	actions = [export_to_csv]
admin.site.register(Enployee,EnployeeAdmin)


class PromotionAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','to_pro')
	search_fields = ('end_id__enp_id','to_pro')
	actions = [export_to_csv]
admin.site.register(Promotion,PromotionAdmin)

class TrainAdmin(admin.ModelAdmin):
	list_display  = ('tra_name','tra_plan','tra_statu','tra_result')
	search_fields = ('tra_name','tra_plan','tra_statu','tra_result')
	actions = [export_to_csv]
admin.site.register(Train,TrainAdmin)


class Checking_inAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','che_date','che_grade','che_mess')
	search_fields = ('end_id__enp_id','che_grade','che_mess')
	actions = [export_to_csv]
admin.site.register(Checking_in,Checking_inAdmin)



class MoneyAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','wage','tax','insu','bonus','real_wage','date')
	search_fields = ('end_id__enp_id','wage','tax','insu','bonus','real_wage','date')
	actions = [export_to_csv]
admin.site.register(Money,MoneyAdmin)



class WorkshopAdmin(admin.ModelAdmin):
	list_display  = ('date','amount','effect','consum','sales','money','num')
	search_fields = ('date','amount','effect','consum','sales','money','num')
	actions = [export_to_csv]
admin.site.register(Workshop,WorkshopAdmin)



class SalesAdmin(admin.ModelAdmin):
	list_display  = ('date','amount','effect','income','per_tax','money','num')
	search_fields = ('date','amount','effect','income','per_tax','money','num')
	actions = [export_to_csv]
admin.site.register(Sales,SalesAdmin)

class LogisticsAdmin(admin.ModelAdmin):
	list_display  = ('date','money','num')
	search_fields = ('date','money','num')
	actions = [export_to_csv]
admin.site.register(Logistics,LogisticsAdmin)