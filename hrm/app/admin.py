from django.contrib import admin
from .models import Department,Profession,Enployee,Retire,Promotion,Train,Checking_in,Money,Workshop,Sales,Logistics

class DepartmentAdmin(admin.ModelAdmin):
	list_display  = ('dep_name','dep_tele')
	search_fields = ('dep_name','dep_tele')
admin.site.register(Department,DepartmentAdmin)

class ProfessionAdmin(admin.ModelAdmin):
	list_display  = ('pro_name','dep_name')
	search_fields = ('pro_name',)
admin.site.register(Profession,ProfessionAdmin)

class EnployeeAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','enp_name','enp_wage','enp_depa','enp_prof','sta_date','end_date','enp_laor','enp_grade')
	search_fields = ('enp_id','enp_name','enp_wage','sta_date','end_date','enp_laor','enp_grade')
admin.site.register(Enployee,EnployeeAdmin)


class RetireAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','pension')
	search_fields = ('pension',)
admin.site.register(Retire,RetireAdmin)

class PromotionAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','to_pro')
	# search_fields = ('aca_name','aca_tele')
admin.site.register(Promotion,PromotionAdmin)

class TrainAdmin(admin.ModelAdmin):
	list_display  = ('tra_name','tra_plan','tra_statu','tra_result')
	search_fields = ('tra_name','tra_plan','tra_statu','tra_result')
admin.site.register(Train,TrainAdmin)


class Checking_inAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','che_date','che_statu')
	search_fields = ('che_date','che_statu')
admin.site.register(Checking_in,Checking_inAdmin)



class MoneyAdmin(admin.ModelAdmin):
	list_display  = ('enp_id','wage','tax','insu','bonus','real_wage','date')
	search_fields = ('wage','tax','insu','bonus','real_wage','date')
admin.site.register(Money,MoneyAdmin)



class WorkshopAdmin(admin.ModelAdmin):
	list_display  = ('date','amount','effect','consum','sales','money','num')
	search_fields = ('date','amount','effect','consum','sales','money','num')
admin.site.register(Workshop,WorkshopAdmin)



class SalesAdmin(admin.ModelAdmin):
	list_display  = ('date','amount','effect','income','per_tax','money','num')
	search_fields = ('date','amount','effect','income','per_tax','money','num')
admin.site.register(Sales,SalesAdmin)

class LogisticsAdmin(admin.ModelAdmin):
	list_display  = ('date','money','num')
	search_fields = ('date','money','num')
admin.site.register(Logistics,LogisticsAdmin)