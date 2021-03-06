# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checking_in',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('che_date', models.DateField(verbose_name='日期')),
                ('che_grade', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='成绩')),
                ('che_mess', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'g.考勤',
                'verbose_name_plural': 'g.考勤',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='部门')),
                ('dep_tele', models.CharField(max_length=11, verbose_name='电话号码')),
            ],
            options={
                'verbose_name': 'a.部门',
                'verbose_name_plural': 'a.部门',
            },
        ),
        migrations.CreateModel(
            name='Enployee',
            fields=[
                ('enp_id', models.AutoField(primary_key=True, serialize=False, verbose_name='工号')),
                ('enp_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('enp_wage', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='工资')),
                ('sta_date', models.DateField(auto_now=True, verbose_name='入职时间')),
                ('end_date', models.DateField(verbose_name='离职时间')),
                ('enp_statu', models.CharField(default='在职', max_length=10, verbose_name='状态')),
                ('password', models.CharField(default='123456', max_length=10, verbose_name='密码')),
            ],
            options={
                'verbose_name': 'c.员工',
                'verbose_name_plural': 'c.员工',
            },
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='金额')),
                ('num', models.IntegerField(verbose_name='人数')),
            ],
            options={
                'verbose_name': 'k.后勤',
                'verbose_name_plural': 'k.后勤',
            },
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='工资')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='税收')),
                ('insu', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='保险')),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='奖金')),
                ('real_wage', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='实发工资')),
                ('date', models.DateField(verbose_name='日期')),
                ('enp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Enployee', verbose_name='工号')),
            ],
            options={
                'verbose_name': 'h.金钱',
                'verbose_name_plural': 'h.金钱',
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('pro_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='职业')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Department', verbose_name='部门')),
            ],
            options={
                'verbose_name': 'b.职业',
                'verbose_name_plural': 'b.职业',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Enployee', verbose_name='工号')),
                ('to_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profession', verbose_name='职业')),
            ],
            options={
                'verbose_name': 'e.升迁',
                'verbose_name_plural': 'e.升迁',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='数量')),
                ('effect', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='效率')),
                ('income', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='收入')),
                ('per_tax', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='每件税收')),
                ('money', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='金额')),
                ('num', models.IntegerField(verbose_name='人数')),
            ],
            options={
                'verbose_name': 'j.销售',
                'verbose_name_plural': 'j.销售',
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('tra_name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='培训')),
                ('tra_plan', models.TextField(verbose_name='计划')),
                ('tra_statu', models.BooleanField(default=False, verbose_name='状态')),
                ('tra_result', models.TextField(verbose_name='成绩')),
            ],
            options={
                'verbose_name': 'f.培训',
                'verbose_name_plural': 'f.培训',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='日期')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='数量')),
                ('effect', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='效率')),
                ('consum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='消耗')),
                ('sales', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='销售')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='金额')),
                ('num', models.IntegerField(verbose_name='人数')),
            ],
            options={
                'verbose_name': 'i.车间',
                'verbose_name_plural': 'i.车间',
            },
        ),
        migrations.AddField(
            model_name='enployee',
            name='enp_prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profession', verbose_name='职业'),
        ),
        migrations.AddField(
            model_name='checking_in',
            name='enp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Enployee', verbose_name='工号'),
        ),
    ]
