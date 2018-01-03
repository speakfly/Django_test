from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name  = models.CharField(max_length = 20,primary_key = True,verbose_name=u"部门")
    dep_tele  = models.CharField(max_length = 11,verbose_name=u"电话号码")
    def __str__(self):
        return self.dep_name
    class Meta:
        verbose_name = 'a.部门'
        verbose_name_plural = 'a.部门'

class Profession(models.Model):
    pro_name = models.CharField(max_length = 20,primary_key = True,verbose_name=u"职业")
    dep_name = models.ForeignKey('Department',verbose_name=u"部门")
    def __str__(self):
        return self.pro_name
    class Meta:
        verbose_name = 'b.职业'
        verbose_name_plural = 'b.职业'

class Enployee(models.Model):
    enp_id    = models.AutoField(primary_key=True,verbose_name=u"工号")
    enp_name  = models.CharField(max_length=10,verbose_name=u"姓名")
    enp_wage  = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"工资")
    enp_prof  = models.ForeignKey('Profession',verbose_name=u"职业")
    sta_date  = models.DateField(verbose_name=u"入职时间",auto_now=True)
    end_date  = models.DateField(verbose_name=u"离职时间")
    enp_statu = models.CharField(max_length=10,default="在职",verbose_name=u"状态")
    password  = models.CharField(max_length=10,default="123456",verbose_name=u"密码")
    def __str__(self):
        return str(self.enp_id)
    class Meta:
        verbose_name = 'c.员工'
        verbose_name_plural = 'c.员工'

class Promotion(models.Model):
    enp_id    = models.ForeignKey('Enployee',verbose_name=u"工号")
    to_pro    = models.ForeignKey('Profession',verbose_name=u"职业")
    def __str__(self):
        return str(self.enp_id)
    class Meta:
        verbose_name = 'e.升迁'
        verbose_name_plural = 'e.升迁'

class Train(models.Model):
    tra_name   = models.CharField(max_length=20,primary_key=True,verbose_name=u"培训")
    tra_plan   = models.TextField(verbose_name=u"计划")
    tra_statu  = models.BooleanField(default = False,verbose_name=u"状态")
    tra_result = models.TextField(verbose_name=u"成绩")
    def __str__(self):
        return self.tra_name
    class Meta:
        verbose_name = 'f.培训'
        verbose_name_plural = 'f.培训'

class Checking_in(models.Model):
    enp_id    = models.ForeignKey('Enployee',verbose_name=u"工号")
    che_date  = models.DateField(verbose_name=u"日期")
    che_grade = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u"成绩")
    che_mess  = models.TextField(blank=True,verbose_name=u"详情") 

    def __str__(self):
        return str(self.enp_id)
    class Meta:
        verbose_name = 'g.考勤'
        verbose_name_plural = 'g.考勤'

class Money(models.Model):
    enp_id    = models.ForeignKey('Enployee',verbose_name=u"工号")
    wage      = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"工资")
    tax       = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"税收")
    insu      = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"保险")
    bonus     = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"奖金")
    real_wage = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"实发工资")
    date      = models.DateField(verbose_name=u"日期")
    def __str__(self):
        return str(self.enp_id)
    class Meta:
        verbose_name = 'h.金钱'
        verbose_name_plural = 'h.金钱'


class Workshop(models.Model):
    date   = models.DateField(auto_now=True,verbose_name=u"日期")
    amount = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"数量")
    effect = models.DecimalField(max_digits=3,decimal_places=2,verbose_name=u"效率")
    consum = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"消耗")
    sales  = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"销售")
    money  = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"金额")
    num    = models.IntegerField(verbose_name=u"人数")
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name = 'i.车间'
        verbose_name_plural = 'i.车间'


class Sales(models.Model):
    date    = models.DateField(auto_now = True,verbose_name=u"日期")
    amount  = models.DecimalField(max_digits=6,decimal_places=2,verbose_name=u"数量")
    effect  = models.DecimalField(max_digits=3,decimal_places=2,verbose_name=u"效率")
    income  = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"收入")
    per_tax = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=u"每件税收")
    money   = models.DecimalField(max_digits=6,decimal_places=2,verbose_name=u"金额")
    num     = models.IntegerField(verbose_name=u"人数")
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name = 'j.销售'
        verbose_name_plural = 'j.销售'

class Logistics(models.Model):
    date   = models.DateField(auto_now=True,verbose_name=u"日期")
    money  = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=u"金额")
    num    = models.IntegerField(verbose_name=u"人数")
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name = 'k.后勤'
        verbose_name_plural = 'k.后勤'

