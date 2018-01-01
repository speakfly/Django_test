from django.shortcuts import render
from .models import Academy,Major,Grade,Apartment,Room,Student,Notice,Repair
from django.http import HttpResponseRedirect,HttpResponse
from django import forms
import sys,os
import xlrd
from django.contrib.admin.views.decorators import staff_member_required
class UserForm(forms.Form):
	stu_id = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20)

class RepairForm(forms.Form):
	rep_type = forms.CharField(max_length = 20)
	message  = forms.CharField(max_length = 50)

class PasswordForm(forms.Form):
	old_password  = forms.CharField(max_length = 20)
	new_password1 = forms.CharField(max_length = 20)
	new_password2 = forms.CharField(max_length = 20)

def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			stu_id = uf.cleaned_data['stu_id']
			password = uf.cleaned_data['password']
			users = Student.objects.filter(stu_id=stu_id,password=password)
			if users:
				request.session['stu_id'] = stu_id
				return HttpResponseRedirect('/index/')
	uf = UserForm()
	return render(request,'login.html',{'uf':'uf'})

def index(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if users:
		notices = Notice.objects.all().order_by('-cre_date')[:3]
		return render(request,'index.html',{'stu_id':stu_id,'notices':notices})
	else:
		return HttpResponseRedirect('/login/')

def logout(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	del request.session['stu_id']
	return HttpResponseRedirect("/login/")

def displayrepair(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	student = Student.objects.get(stu_id=stu_id)
	repairs = Repair.objects.filter(room_id=student.room_id)
	return render(request,"displayrepair.html",{'repairs':repairs})


def repair(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	if request.method == 'POST':
		uf = RepairForm(request.POST)
		if uf.is_valid():
			rep_type = uf.cleaned_data['rep_type']
			message = uf.cleaned_data['message']
			student = Student.objects.get(stu_id=stu_id)
			Repair.objects.create(rep_type = rep_type,message = message,room_id=student.room_id)
			return HttpResponseRedirect('/displayrepair/')
	return render(request,'repair.html')

def updatepassword(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
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
			users = Student.objects.filter(stu_id=stu_id,password=old_password)
			if len(users)==0:
				return HttpResponse(u"旧密码错误")
			Student.objects.filter(stu_id=stu_id).update(password=new_password2)
			return HttpResponseRedirect('/index/')
	return render(request,'updatepassword.html',{'stu_id':stu_id})

def displaynotice(request):
	nid = request.GET.get("noticeid","0")
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	id = int(nid)
	notice = Notice.objects.get(id=id)
	return render(request,"displaynotice.html",{'notice':notice})

def academy_exmaple_download(request):  
	file=open('app/download/academy_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="academy_example.xlsx"'  
	return response

def major_exmaple_download(request):  
	file=open('app/download/major_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="major_example.xlsx"'  
	return response

def grade_exmaple_download(request):  
	file=open('app/download/grade_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="grade_example.xlsx"'  
	return response


def apartment_exmaple_download(request):  
	file=open('app/download/apartment_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="apartment_example.xlsx"'  
	return response


def room_exmaple_download(request):  
	file=open('app/download/room_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="room_example.xlsx"'  
	return response

def student_exmaple_download(request):  
	file=open('app/download/student_example.xlsx','rb')  
	response =HttpResponse(file)  
	response['Content-Type']='application/octet-stream'  
	response['Content-Disposition']='attachment;filename="student_example.xlsx"'  
	return response

def academy_upload(request):  
	if request.method == "POST":
		academy_file =request.FILES.get("academy_file", None) 
		if not academy_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",academy_file.name),'wb+')  
		for chunk in academy_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",academy_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			aca_name = str(sheet.cell(rx,0).value)
			aca_tele = (str(sheet.cell(rx,1).value))[0:11]
			Academy.objects.create(aca_name=aca_name,aca_tele=aca_tele)
		os.remove(os.path.join(".",academy_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html") 



def major_upload(request):  
	if request.method == "POST":
		major_file =request.FILES.get("major_file", None) 
		if not major_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",major_file.name),'wb+')  
		for chunk in major_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",major_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			maj_name     = str(sheet.cell(rx,0).value)
			aca_name_str = str(sheet.cell(rx,1).value)
			aca_name     = Academy.objects.get(aca_name=aca_name_str)
			Major.objects.create(maj_name=maj_name,aca_name=aca_name)
		os.remove(os.path.join(".",major_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html") 

def grade_upload(request):  
	if request.method == "POST":
		grade_file =request.FILES.get("grade_file", None) 
		if not grade_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",grade_file.name),'wb+')  
		for chunk in grade_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",grade_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			gra_name     = str(sheet.cell(rx,0).value)
			maj_name_str = str(sheet.cell(rx,1).value)
			maj_name     = Major.objects.get(maj_name=maj_name_str)
			Grade.objects.create(gra_name=gra_name,maj_name=maj_name)
		os.remove(os.path.join(".",grade_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html") 

def apartment_upload(request):  
	if request.method == "POST":
		apartment_file =request.FILES.get("apartment_file", None) 
		if not apartment_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",apartment_file.name),'wb+')  
		for chunk in apartment_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",apartment_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			apa_name     = str(sheet.cell(rx,0).value)
			room_num     = int(sheet.cell(rx,1).value)
			bed_num      = int(sheet.cell(rx,2).value)
			Apartment.objects.create(apa_name=apa_name,room_num=room_num,bed_num=bed_num)
		os.remove(os.path.join(".",apartment_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html") 

def room_upload(request):  
	if request.method == "POST":
		room_file =request.FILES.get("room_file", None) 
		if not room_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",room_file.name),'wb+')  
		for chunk in room_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",room_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			room_id         = str(sheet.cell(rx,0).value)
			apa_name_str    = str(sheet.cell(rx,1).value)
			apa_name        = Apartment.objects.get(apa_name = apa_name_str)
			Room.objects.create(room_id=room_id,apa_name=apa_name,room_num=0)
		os.remove(os.path.join(".",room_file.name))

		return HttpResponse("upload over!")
	return render(request,"all.html") 


def student_upload(request):  
	if request.method == "POST":
		student_file =request.FILES.get("student_file", None) 
		if not student_file:  
			return HttpResponse("no files for upload!")  
		destination = open(os.path.join(".",student_file.name),'wb+')  
		for chunk in student_file.chunks():
			destination.write(chunk)  
		destination.close()


		excel_file = xlrd.open_workbook(os.path.join(".",student_file.name))
		sheet = excel_file.sheet_by_index(0)
		for rx in range(1, sheet.nrows):
			stu_id             = str(sheet.cell(rx,0).value)
			stu_name           = str(sheet.cell(rx,1).value)
			gra_name_str       = str(sheet.cell(rx,2).value)
			room_id_str        = str(sheet.cell(rx,3).value)
			gra_name           = Grade.objects.get(gra_name = gra_name_str)
			room_id            = Room.objects.get(room_id = room_id_str)
			Student.objects.create(stu_id=stu_id,stu_name=stu_name,gra_name=gra_name,room_id=room_id)
		os.remove(os.path.join(".",student_file.name))

		return HttpResponse("upload over!")
	return render(request,"all_upload.html")

def all_upload(request):
	return render(request,"all_upload.html")


def search_notice(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	search_title = request.GET.get("search_title","0")
	notices = Notice.objects.filter(title__contains=search_title)
	return render(request,"search_notice.html",{'notices':notices})


def test_suit_link(request):
	return render(request,"test_suit_link.html")

def personal_center(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	return render(request,"personal_center.html",{'users':users})

def read_more(request):
	stu_id = request.session.get("stu_id","anybody")
	users = Student.objects.filter(stu_id=stu_id)
	if len(users) == 0:
		return HttpResponseRedirect('/login/')
	notices = Notice.objects.all().order_by('-cre_date')
	return render(request,'read_more.html',{"notices":notices})

test_suit_link = staff_member_required(test_suit_link)
all_upload = staff_member_required(all_upload)
