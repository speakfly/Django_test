from django.db import models
class Academy(models.Model):
    aca_name = models.CharField(verbose_name=u"学院名称",max_length = 20,primary_key = True)
    aca_tele  = models.CharField(verbose_name=u"学院电话",max_length = 20)
    def __str__(self):
        return self.aca_name
    class Meta:
        verbose_name = '1.学院'
        verbose_name_plural = '1.学院'
class Major(models.Model):
    maj_name = models.CharField(verbose_name=u"专业名称",max_length = 20,primary_key = True)
    aca_name = models.ForeignKey('Academy',verbose_name=u"学院")
    def __str__(self):
        return self.maj_name
    class Meta:
        verbose_name = '2.专业'
        verbose_name_plural = '2.专业'
class Grade(models.Model):
    gra_name = models.CharField(verbose_name=u"班级名称",max_length = 20,primary_key = True)
    maj_name = models.ForeignKey('Major',verbose_name=u"专业")
    def __str__(self):
        return self.gra_name
    class Meta:
        verbose_name = '3.班级'
        verbose_name_plural = '3.班级'
class Apartment(models.Model):
    apa_name = models.CharField(verbose_name=u"公寓",max_length = 20,primary_key = True)
    room_num = models.IntegerField(verbose_name=u"房间数",)
    bed_num  = models.IntegerField(verbose_name=u"床位数",)
    def __str__(self):
        return self.apa_name
    class Meta:
        verbose_name = '4.宿舍'
        verbose_name_plural = '4.宿舍'

class Room(models.Model):
    room_id  = models.CharField(verbose_name=u"公寓_宿舍号",max_length=20,primary_key=True)
    room_num = models.IntegerField(verbose_name=u"已有多少人",)
    apa_name = models.ForeignKey('Apartment',verbose_name=u"公寓")
    def __str__(self):
        return self.room_id
    class Meta:
        verbose_name = '5.房间'
        verbose_name_plural = '5.房间'

class Student(models.Model):
    stu_id    = models.CharField(verbose_name=u"学号",max_length = 20,primary_key = True)
    stu_name  = models.CharField(verbose_name=u"姓名",max_length = 20)
    gra_name  = models.ForeignKey('Grade',verbose_name=u"班级")
    room_id   = models.ForeignKey('Room',verbose_name=u"公寓_宿舍号")
    password  = models.CharField(verbose_name=u"密码",max_length = 20,default = '123456')
    statu     = models.BooleanField(verbose_name=u"状态",default = True)
    def __str__(self):
        return self.stu_id
    class Meta:
        verbose_name = '6.学生'
        verbose_name_plural = '6.学生'
class Notice(models.Model):
    title = models.CharField(verbose_name=u"题目",max_length = 20)
    author = models.CharField(verbose_name=u"作者",max_length = 20)
    message = models.TextField(verbose_name=u"信息",)
    cre_date   = models.DateTimeField(verbose_name=u"发布日期",auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '7.公告'
        verbose_name_plural = '7.公告'
class Repair(models.Model):
    rep_type = models.CharField(verbose_name=u"维修类型",max_length=4)
    message  = models.TextField(verbose_name=u"维修信息",)
    room_id  = models.ForeignKey('Room',verbose_name=u"公寓_宿舍号")
    statu    = models.BooleanField(verbose_name=u"状态",default = False)
    cre_date = models.DateTimeField(verbose_name=u"保修时间",auto_now=True)
    fin_date = models.DateTimeField(verbose_name=u"维修时间",auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '8.维修'
        verbose_name_plural = '8.维修'