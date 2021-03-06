from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    # 自定义性别选项规则
    GENDER_CHOICE = (
        ('male',u'男'),
        ('female',u'女')
    )
    #昵称
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='')
    #生日
    birthday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    #性别，只能男或女。默认男
    gender = models.CharField(
        max_length=6,
        verbose_name=u'性别',
        choices=GENDER_CHOICE,
        default='male'
    )
    #地址
    address = models.CharField(max_length=100,verbose_name=u'地址',default='')
    #电话
    mobile = models.CharField(max_length=11,null=True,blank=True)
    #头像，默认使用default.png
    image = models.ImageField(
        upload_to='image/%Y/%m',
        default='image/default.png',
        max_length=100
    )

    #meta信息，即后台栏目名
    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

#邮箱验证码model
class EmailRecord(models.Model):
    SEND_CHOICE = (
        ('register',u'注册'),
        ('forget',u'找回密码')
    )

    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type = models.CharField(max_length=10,choices=SEND_CHOICE)
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

#轮播图model

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(
        upload_to='banner/%Y/%m',
        verbose_name=u'轮播图',
        max_length=100
    )
    url = models.CharField(max_length=200,verbose_name=u'访问地址')
    index = models.IntegerField(default=100,verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name