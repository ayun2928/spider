from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=20,verbose_name='电话号码')
    upwd = models.CharField(max_length=20,verbose_name='密码')
    uemail = models.EmailField(verbose_name='电子邮件')
    uname = models.CharField(max_length=20,verbose_name='用户名')
    isActive = models.BooleanField(default=True,verbose_name='是否激活')

    def __str__(self):
        return self.uphone

    def to_dict(self):
        dic = {
            "id" : self.id,
            "uphone":self.uphone,
            "upwd" : self.upwd,
            "uname" : self.uname,
            "uemail" : self.uemail,
            "isActive": self.isActive
        }
        return dic

# 创建商品类型的实体 - GoodsType
class GoodsType(models.Model):
    # 商品类型名称
    title = models.CharField(max_length=50,verbose_name='类型名称')
    # 商品类型图片
    picture = models.ImageField(upload_to='static/upload/goodstype',null=True,verbose_name='类型图片')
    # 商品类型描述
    desc=models.TextField(verbose_name='商品描述')

    def __str__(self):
        return self.title

    class Meta:
        db_table='GoodsType'
        verbose_name='商品类型'
        verbose_name_plural=verbose_name









