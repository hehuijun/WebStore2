from django.contrib import admin
from commodity.models import Commondity






# Register your models here.
class AdminCommondity(admin.ModelAdmin):
    list_display = ('CommodityName','CommodityCategory','CommodityPrice','CommodityDateTime')#后台显示的列表内容
    search_fields = ('CommodityName', 'CommodityCategory',)#从哪些字段中搜索
    list_filter = ('CommodityCategory','CommodityDateTime',)#筛选器

admin.site.register(Commondity,AdminCommondity)

