from django.db import models


# Create your models here.
class Commondity(models.Model):
    CommodityName = models.CharField('商品名称', max_length=100)
    CommodityCategory = models.CharField('商品类别', max_length=50, blank=True)
    CommodityPrice = models.DecimalField('商品价格', max_digits=11, decimal_places=2)
    CommondityImage = models.ImageField('商品图片', upload_to='static', default='static/upload/None/no-img.jpg')
    CommodityDateTime = models.DateTimeField('登记日期', auto_now_add=True)
    CommodityContent = models.TextField('商品说明', blank=True, null=True)
    CommondityContactMobile = models.CharField('联系电话', max_length=11, blank=True, null=True)

    def __str__(self):
        return self.CommodityName  # 一般系统默认使用<Commodity: Commodity object> 来表示对象, 通过这个函数可以告诉系统使用CommodityName字段来表示这个对象

    class Meta:
        verbose_name = '商品' #给模型起个更好听的名字，这儿相当于进行了汉化。
        verbose_name_plural = '所有商品'
        # 按时间下降排序
        ordering = ['-CommodityDateTime']
