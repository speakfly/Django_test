from django.db import models
class Academy(models.Model):
    aca_name = models.CharField(max_length = 20,primary_key = True)
    aca_tele  = models.CharField(max_length = 20)
    def __str__(self):
        return self.aca_name
    class Meta:
        verbose_name = '1.学院'
        verbose_name_plural = '1.学院'
class Major(models.Model):
    maj_name = models.CharField(max_length = 20,primary_key = True)
    aca_name = models.ForeignKey('Academy')
    def __str__(self):
        return self.maj_name
    class Meta:
        verbose_name = '2.专业'
        verbose_name_plural = '2.专业'
class Grade(models.Model):
    gra_name = models.CharField(max_length = 20,primary_key = True)
    maj_name = models.ForeignKey('Major')
    def __str__(self):
        return self.gra_name
    class Meta:
        verbose_name = '3.班级'
        verbose_name_plural = '3.班级'
class Apartment(models.Model):
    apa_name = models.CharField(max_length = 20,primary_key = True)
    room_num = models.IntegerField()
    bed_num  = models.IntegerField()
    def __str__(self):
        return self.apa_name
    class Meta:
        verbose_name = '4.宿舍'
        verbose_name_plural = '4.宿舍'

class Room(models.Model):
    room_id  = models.CharField(max_length=20,primary_key=True)
    room_num = models.IntegerField()
    apa_name = models.ForeignKey('Apartment')
    def __str__(self):
        return self.room_id
    class Meta:
        verbose_name = '5.房间'
        verbose_name_plural = '5.房间'

class Student(models.Model):
    stu_id    = models.CharField(max_length = 20,primary_key = True)
    stu_name  = models.CharField(max_length = 20)
    gra_name  = models.ForeignKey('Grade')
    room_id   = models.ForeignKey('Room')
    password  = models.CharField(max_length = 20,default = '123456')
    statu     = models.BooleanField(default = True)
    def __str__(self):
        return self.stu_id
    class Meta:
        verbose_name = '6.学生'
        verbose_name_plural = '6.学生'
class Notice(models.Model):
    title = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    message = models.TextField()
    cre_date   = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '7.公告'
        verbose_name_plural = '7.公告'
class Repair(models.Model):
    rep_type = models.CharField(max_length=4)
    message  = models.TextField()
    room_id  = models.ForeignKey('Room')
    statu    = models.BooleanField(default = False)
    cre_date = models.DateTimeField(auto_now=True)
    fin_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = '8.维修'
        verbose_name_plural = '8.维修'

