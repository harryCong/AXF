from django.db import models

# Create your models here.
# 基类  模型类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# 轮播图 模型类
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

# 导航类 模型类
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

# 每日必买 模型类
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'

# 商品部分内容  模型类
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

# 商品主体内容

class Mainshow(models.Model):
    trackid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=100)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=100)
    productid1 = models.CharField(max_length=100)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=100)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=100)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table ='axf_mainshow'

# 闪购超市
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=100)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=100)
    typesort = models.CharField(max_length=100)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'axf_foodtypes'

class Goods(models.Model):
    productid = models.CharField(max_length=50)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=100)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=50)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=50)
    childcid = models.CharField(max_length=50)
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=50)
    storenums = models.CharField(max_length=50)
    productnum = models.CharField(max_length=50)

    class Meta:
        db_table = 'axf_goods'


# 用户 模型类
class User(models.Model):

    account = models.CharField(max_length=20, unique=True)

    password = models.CharField(max_length=256)

    name = models.CharField(max_length=100)

    tel = models.CharField(max_length=20)

    address = models.CharField(max_length=256)

    img = models.CharField(max_length=100)

    rank = models.IntegerField(default=1)

    token = models.CharField(max_length=100)

class Cart(models.Model):

    user = models.ForeignKey(User)

    goods = models.ForeignKey(Goods)

    goodnumber = models.IntegerField(default=1)

    isselect = models.BooleanField(default=True)