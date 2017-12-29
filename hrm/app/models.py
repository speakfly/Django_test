from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name  = models.CharField(max_length = 20,primary_key = True)
    dep_tele  = models.CharField(max_length = 11)
    def __str__(self):
        return self.dep_name
    class Meta:
        verbose_name = 'a.部门'
        verbose_name_plural = 'a.部门'

class Profession(models.Model):
    pro_name = models.CharField(max_length = 20,primary_key = True)
    dep_name = models.ForeignKey('Department')
    def __str__(self):
        return self.pro_name
    class Meta:
        verbose_name = 'b.职业'
        verbose_name_plural = 'b.职业'


class Enployee(models.Model):
    enp_id    = models.CharField(max_length=10,primary_key=True)
    enp_name  = models.CharField(max_length=10)
    enp_wage  = models.DecimalField(max_digits=6,decimal_places=2)
    enp_depa  = models.ForeignKey('Department')
    enp_prof  = models.ForeignKey('Profession')
    sta_date  = models.DateField()
    end_date  = models.DateField()
    enp_laor  = models.IntegerField()
    enp_grade = models.IntegerField()

    def __str__(self):
        return self.enp_id
    class Meta:
        verbose_name = 'c.员工'
        verbose_name_plural = 'c.员工'

class Retire(models.Model):
    enp_id    = models.ForeignKey('Enployee')
    pension   = models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return self.str(enp_id)
    class Meta:
        verbose_name = 'd.退休'
        verbose_name_plural = 'd.退休'

class Promotion(models.Model):
    enp_id    = models.ForeignKey('Enployee')
    to_pro  = models.ForeignKey('Profession')
    def __str__(self):
        return self.str(enp_id)
    class Meta:
        verbose_name = 'e.升迁'
        verbose_name_plural = 'e.升迁'

class Train(models.Model):
    tra_name   = models.CharField(max_length=20,primary_key=True)
    tra_plan   = models.TextField()
    tra_statu  = models.BooleanField(default = False)
    tra_result = models.TextField()
    def __str__(self):
        return self.tra_name
    class Meta:
        verbose_name = 'f.培训'
        verbose_name_plural = 'f.培训'

class Checking_in(models.Model):
    enp_id    = models.ForeignKey('Enployee')
    che_date  = models.DateField()
    che_statu = models.BooleanField(default=True)
    def __str__(self):
        return self.str(enp_id)
    class Meta:
        verbose_name = 'g.考勤'
        verbose_name_plural = 'g.考勤'

class Money(models.Model):
    enp_id    = models.ForeignKey('Enployee')
    wage      = models.DecimalField(max_digits=6,decimal_places=2)
    tax       = models.DecimalField(max_digits=6,decimal_places=2)
    insu      = models.DecimalField(max_digits=6,decimal_places=2)
    bonus     = models.DecimalField(max_digits=6,decimal_places=2)
    real_wage = models.DecimalField(max_digits=6,decimal_places=2)
    date      = models.DateField()
    def __str__(self):
        return self.str(enp_id)
    class Meta:
        verbose_name = 'h.金钱'
        verbose_name_plural = 'h.金钱'


class Workshop(models.Model):
    date   = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    effect = models.DecimalField(max_digits=3,decimal_places=2)
    consum = models.DecimalField(max_digits=10,decimal_places=2)
    sales  = models.DecimalField(max_digits=10,decimal_places=2)
    money  = models.DecimalField(max_digits=10,decimal_places=2)
    num    = models.IntegerField()
    def __str__(self):
        return self.str(self.date)
    class Meta:
        verbose_name = 'i.车间'
        verbose_name_plural = 'i.车间'


class Sales(models.Model):
    date    = models.DateField()
    amount  = models.DecimalField(max_digits=6,decimal_places=2)
    effect  = models.DecimalField(max_digits=3,decimal_places=2)
    income  = models.DecimalField(max_digits=10,decimal_places=2)
    per_tax = models.DecimalField(max_digits=5,decimal_places=2)
    money   = models.DecimalField(max_digits=6,decimal_places=2)
    num     = models.IntegerField()
    def __str__(self):
        return self.str(self.date)
    class Meta:
        verbose_name = 'j.销售'
        verbose_name_plural = 'j.销售'

class Logistics(models.Model):
    date   = models.DateField()
    money  = models.DecimalField(max_digits=10,decimal_places=2)
    num    = models.IntegerField()
    def __str__(self):
        return self.str(self.date)
    class Meta:
        verbose_name = 'k.后勤'
        verbose_name_plural = 'k.后勤'