from django.shortcuts import render
from .models import Department,Profession,Enployee,Promotion,Train,Checking_in,Money,Workshop,Sales,Logistics
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
import sys,os
import xlrd
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def department_exmaple_download(request):  
	file=open('app/download/department_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="department_example.xlsx"'  
	return response

def profession_exmaple_download(request):  
	file=open('app/download/profession_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="profession_example.xlsx"'  
	return response

def enployee_exmaple_download(request):  
	file=open('app/download/enployee_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="enployee_example.xlsx"'  
	return response

def train_exmaple_download(request):  
	file=open('app/download/train_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="train_example.xlsx"'  
	return response

def checking_in_exmaple_download(request):  
	file=open('app/download/checking_in_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="checking_in_example.xlsx"'  
	return response

def money_exmaple_download(request):  
	file=open('app/download/money_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="money_example.xlsx"'  
	return response

def workshop_exmaple_download(request):  
	file=open('app/download/workshop_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="workshop_example.xlsx"'  
	return response

def sales_exmaple_download(request):  
	file=open('app/download/sales_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="sales_example.xlsx"'  
	return response

def logistics_exmaple_download(request):  
	file=open('app/download/logistics_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="logistics_example.xlsx"'  
	return response

def all_upload(request):
	return render(request,"all_upload.html")

def department_upload(request):  
	if request.method == "POST":
		department_file =request.FILES.get("department_file", None) 
		if not department_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",department_file.name),'wb+')  
		for chunk in department_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",department_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			dep_name = str(sheet.cell(rx,0).value)
			dep_tele = (str(sheet.cell(rx,1).value))[0:11]
			Department.objects.create(dep_name=dep_name,dep_tele=dep_tele)
		os.remove(os.path.join(".",department_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def profession_upload(request):  
	if request.method == "POST":
		profession_file =request.FILES.get("profession_file", None) 
		if not profession_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",profession_file.name),'wb+')  
		for chunk in profession_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",profession_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			pro_name     = str(sheet.cell(rx,0).value)
			dep_name_str = str(sheet.cell(rx,1).value)
			dep_name     = Department.objects.get(dep_name=dep_name_str)
			Profession.objects.create(pro_name=pro_name,dep_name=dep_name)
		os.remove(os.path.join(".",profession_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def enployee_upload(request):  
	if request.method == "POST":
		enployee_file =request.FILES.get("enployee_file", None) 
		if not enployee_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",enployee_file.name),'wb+')  
		for chunk in enployee_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",enployee_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			enp_name      = str(sheet.cell(rx,0).value)
			enp_wage      = float(sheet.cell(rx,1).value)
			enp_prof_str  = str(sheet.cell(rx,2).value)
			sta_date      = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,3).value, 0)
			end_date      = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,4).value, 0)
			enp_statu     = str(sheet.cell(rx,5).value)
			enp_prof      = Profession.objects.get(pro_name=enp_prof_str) 
			Enployee.objects.create(enp_name=enp_name,enp_wage=enp_wage,enp_prof=enp_prof,sta_date=sta_date,end_date=end_date,enp_statu=enp_statu)
		os.remove(os.path.join(".",enployee_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def checking_in_upload(request):  
	if request.method == "POST":
		checking_in_file =request.FILES.get("checking_in_file", None) 
		if not checking_in_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",checking_in_file.name),'wb+')  
		for chunk in checking_in_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",checking_in_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			enp_id_str    = str(sheet.cell(rx,0).value)
			che_date      = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,1).value,0)
			che_grade     = int(str(sheet.cell(rx,2).value))
			che_mess      = str(sheet.cell(rx,3).value)
			enp_id        = Enployee.objects.get(enp_id = enp_id_str)
			Checking_in.objects.create(enp_id=enp_id,che_date=che_date,che_grade=che_grade,che_mess=che_mess)
		os.remove(os.path.join(".",checking_in_file.name))
		return HttpResponse("upload over!")
	return render(request,"all_upload.html")


def money_upload(request):  
	if request.method == "POST":
		money_file =request.FILES.get("money_file", None) 
		if not money_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",money_file.name),'wb+')  
		for chunk in money_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",money_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			enp_id_str    = str(sheet.cell(rx,0).value)
			wage          = float(sheet.cell(rx,1).value)
			tax           = float(sheet.cell(rx,2).value)
			insu          = float(sheet.cell(rx,3).value)
			bonus         = float(sheet.cell(rx,4).value)
			real_wage     = float(sheet.cell(rx,5).value)
			date          = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,6).value,0)
			enp_id        = Enployee.objects.get(enp_id = enp_id_str)
			Money.objects.create(enp_id=enp_id,wage=wage,tax=tax,insu=insu,bonus=bonus,real_wage=real_wage,date=date)
		os.remove(os.path.join(".",money_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")


def workshop_upload(request):  
	if request.method == "POST":
		workshop_file =request.FILES.get("workshop_file", None) 
		if not workshop_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",workshop_file.name),'wb+')  
		for chunk in workshop_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",workshop_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			date   = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,0).value,0)
			amount = float(sheet.cell(rx,1).value)
			effect = float(sheet.cell(rx,2).value)
			consum = float(sheet.cell(rx,3).value)
			sales  = float(sheet.cell(rx,4).value)
			money  = float(sheet.cell(rx,5).value)
			num    = int(sheet.cell(rx,6).value)
			Workshop.objects.create(date=date,amount=amount,effect=effect,consum=consum,sales=sales,money=money,num=num)
		os.remove(os.path.join(".",workshop_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def sales_upload(request):  
	if request.method == "POST":
		sales_file =request.FILES.get("sales_file", None) 
		if not sales_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",sales_file.name),'wb+')  
		for chunk in sales_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",sales_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			date   = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,0).value,0)
			amount = float(sheet.cell(rx,1).value)
			effect = float(sheet.cell(rx,2).value)
			income = float(sheet.cell(rx,3).value)
			per_tax  = float(sheet.cell(rx,4).value)
			money  = float(sheet.cell(rx,5).value)
			num    = int(sheet.cell(rx,6).value)
			Sales.objects.create(date=date,amount=amount,effect=effect,income=income,per_tax=per_tax,money=money,num=num)
		os.remove(os.path.join(".",sales_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def logistics_upload(request):  
	if request.method == "POST":
		logistics_file =request.FILES.get("logistics_file", None) 
		if not logistics_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",logistics_file.name),'wb+')  
		for chunk in logistics_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",logistics_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			date   = xlrd.xldate.xldate_as_datetime(sheet.cell(rx,0).value,0)
			money  = float(sheet.cell(rx,1).value)
			num    = int(sheet.cell(rx,2).value)
			Logistics.objects.create(date=date,money=money,num=num)
		os.remove(os.path.join(".",logistics_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")








class UserForm(forms.Form):
	enp_id   = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)

class PasswordForm(forms.Form):
	old_password  = forms.CharField(max_length = 20)
	new_password1 = forms.CharField(max_length = 20)
	new_password2 = forms.CharField(max_length = 20)

def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			enp_id = uf.cleaned_data['enp_id']
			password = uf.cleaned_data['password']
			users = Enployee.objects.filter(enp_id=enp_id,password=password)
			if users:
				request.session['enp_id'] = enp_id
				return HttpResponseRedirect('/index/')
	uf = UserForm()
	return render(request,'login.html',{'uf':'uf'})

def index(request):
	enp_id = request.session.get("enp_id","anybody")
	users = Enployee.objects.filter(enp_id=enp_id)
	if users:
		money_list        = Money.objects.filter(enp_id=users[0]).order_by('-date')[:1]
		checking_in_list  = Checking_in.objects.filter(enp_id=users[0]).order_by('-che_date')[:1]
		return render(request,'index.html',{'money_list':money_list,'checking_in_list':checking_in_list})
	else:
		return HttpResponseRedirect('/login/')

def logout(request):
	enp_id = request.session.get("enp_id","anybody")
	users = Enployee.objects.filter(enp_id=enp_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	del request.session['enp_id']
	return HttpResponseRedirect("/login/")

def updatepassword(request):
	enp_id = request.session.get("enp_id","anybody")
	users = Enployee.objects.filter(enp_id=enp_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	if request.method == 'POST':
		uf = PasswordForm(request.POST)
		if uf.is_valid():
			old_password = uf.cleaned_data['old_password']
			new_password1 = uf.cleaned_data['new_password1']
			new_password2 = uf.cleaned_data['new_password2']
			if new_password1 != new_password2:
				return HttpResponse(u"两次密码不匹配")
			users = Enployee.objects.filter(enp_id=enp_id,password=old_password)
			if len(users)==0:
				return HttpResponse(u"旧密码错误")
			Enployee.objects.filter(enp_id=enp_id).update(password=new_password2)
			return HttpResponseRedirect('/index/')
	return render(request,'updatepassword.html')



logistics_upload = staff_member_required(logistics_upload)
sales_upload = staff_member_required(sales_upload)
workshop_upload = staff_member_required(workshop_upload)
money_upload = staff_member_required(money_upload)
checking_in_upload = staff_member_required(checking_in_upload)
enployee_upload = staff_member_required(enployee_upload)
profession_upload = staff_member_required(profession_upload)
department_upload = staff_member_required(department_upload)
all_upload = staff_member_required(all_upload)