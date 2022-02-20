from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Metro(db.Model):
    __tablename__ = 'metro'
    id = db.Column(db.Integer, primary_key=True)
    date_day = db.Column(db.DateTime, nullable=False)
    get_on = db.Column(db.Integer, nullable=False)
    get_off = db.Column(db.Integer, nullable=False)

    def __init__(self, date_day, get_on , get_off):
        self.date_day = date_day
        self.get_on = get_on
        self.get_off = get_off


class Movie(db.Model):

    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key= True, nullable= False)
    date_day = db.Column(db.DateTime, nullable= False)
    korea_sales = db.Column(db.Integer, nullable= False)
    korea_audience_num = db.Column(db.Integer, nullable=False)
    foreign_audience_num = db.Column(db.Integer, nullable=False)
    foreign_sales = db.Column(db.Integer, nullable=False)
    total_sales = db.Column(db.Integer, nullable=False)
    total_audience = db.Column(db.Integer, nullable=False)

    def __init__(self, date_day, korea_sales, korea_audience_num, foreign_audience_num,foreign_sales,
                 total_sales, total_audience):
        self.date_day = date_day
        self.korea_sales = korea_sales
        self.korea_audience_num = korea_audience_num
        self.foreign_audience_num = foreign_audience_num
        self.foreign_sales = foreign_sales
        self.total_sales = total_sales
        self.total_audience = total_audience

class Consumption(db.Model):
    __tablename__ = 'consumption'
    ID = db.Column(db.Integer, primary_key = True)
    DATE_MON = db.Column(db.String(255), nullable = False)
    MARKET_NONFOOD_HOMEWARE_CULTURE = db.Column(db.Float(8), nullable = False)
    MARKET_NONFOOD_CLOTHING = db.Column(db.Float(8), nullable = False)
    MARKET_NONFOOD_DAILY = db.Column(db.Float(8), nullable = False)
    MARKET_NONFOOD_SPORT = db.Column(db.Float(8), nullable = False)
    MARKET_NONFOOD_CHANDLERY = db.Column(db.Float(8), nullable = False)
    MARKET_NONFOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    MARKET_FOOD = db.Column(db.Float(8), nullable = False)
    MARKET_TOTAL = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_CHANDLERY = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_WOMENSUITS = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_WOMENCASUAL = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_MENCLOTHING = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_KIDS_SPORT = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_HOMEWARE = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_LUXURY = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_NONFOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_FOOD = db.Column(db.Float(8), nullable = False)
    DEPARTMENT_TOTAL = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_NONFOOD_DAILY = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_NONFOOD_CHANDLERY = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_NONFOOD_CIGARETTE_ETC = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_NONFOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_FOOD_BEVERAGE_PROCESSED = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_FOOD_INSTANT_FRESH = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_FOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    CONVENIENCE_TOTAL = db.Column(db.Float(8), nullable = False)
    SSM_NONFOOD_DAILY = db.Column(db.Float(8), nullable = False)
    SSM_NONFOOD_CHANDLERY = db.Column(db.Float(8), nullable = False)
    SSM_NONFOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK = db.Column(db.Float(8), nullable = False)
    SSM_FOOD_FRESH = db.Column(db.Float(8), nullable = False)
    SSM_FOOD_PROCESSED = db.Column(db.Float(8), nullable = False)
    SSM_FOOD_SUBTOTAL = db.Column(db.Float(8), nullable = False)
    SSM_TOTAL = db.Column(db.Float(8), nullable = False)

def __init__(self, DATE_MON, MARKET_NONFOOD_HOMEWARE_CULTURE, MARKET_NONFOOD_CLOTHING, MARKET_NONFOOD_DAILY, MARKET_NONFOOD_SPORT, MARKET_NONFOOD_CHANDLERY, MARKET_NONFOOD_SUBTOTAL,
                MARKET_FOOD, MARKET_TOTAL, DEPARTMENT_NONFOOD_CHANDLERY, DEPARTMENT_NONFOOD_WOMENSUITS, DEPARTMENT_NONFOOD_WOMENCASUAL, DEPARTMENT_NONFOOD_MENCLOTHING, DEPARTMENT_NONFOOD_KIDS_SPORT,
                DEPARTMENT_NONFOOD_HOMEWARE, DEPARTMENT_NONFOOD_LUXURY, DEPARTMENT_NONFOOD_SUBTOTAL, DEPARTMENT_FOOD, DEPARTMENT_TOTAL, CONVENIENCE_NONFOOD_DAILY, CONVENIENCE_NONFOOD_CHANDLERY,
                CONVENIENCE_NONFOOD_CIGARETTE_ETC,CONVENIENCE_NONFOOD_SUBTOTAL, CONVENIENCE_FOOD_BEVERAGE_PROCESSED, CONVENIENCE_FOOD_INSTANT_FRESH, CONVENIENCE_FOOD_SUBTOTAL, CONVENIENCE_TOTAL,
                SSM_NONFOOD_DAILY, SSM_NONFOOD_CHANDLERY, SSM_NONFOOD_SUBTOTAL, SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK, SSM_FOOD_FRESH, SSM_FOOD_PROCESSED, SSM_FOOD_SUBTOTAL, SSM_TOTAL):
        self.DATE_MON = DATE_MON
        self.MARKET_NONFOOD_HOMEWARE_CULTURE = MARKET_NONFOOD_HOMEWARE_CULTURE
        self.MARKET_NONFOOD_CLOTHING = MARKET_NONFOOD_CLOTHING
        self.MARKET_NONFOOD_DAILY = MARKET_NONFOOD_DAILY
        self.MARKET_NONFOOD_SPORT = MARKET_NONFOOD_SPORT
        self.MARKET_NONFOOD_CHANDLERY = MARKET_NONFOOD_CHANDLERY
        self.MARKET_NONFOOD_SUBTOTAL = MARKET_NONFOOD_SUBTOTAL
        self.MARKET_FOOD = MARKET_FOOD
        self.MARKET_TOTAL =MARKET_TOTAL
        self.DEPARTMENT_NONFOOD_CHANDLERY = DEPARTMENT_NONFOOD_CHANDLERY
        self.DEPARTMENT_NONFOOD_WOMENSUITS = DEPARTMENT_NONFOOD_WOMENSUITS
        self.DEPARTMENT_NONFOOD_WOMENCASUAL = DEPARTMENT_NONFOOD_WOMENCASUAL
        self.DEPARTMENT_NONFOOD_MENCLOTHING = DEPARTMENT_NONFOOD_MENCLOTHING
        self.DEPARTMENT_NONFOOD_KIDS_SPORT = DEPARTMENT_NONFOOD_KIDS_SPORT
        self.DEPARTMENT_NONFOOD_HOMEWARE = DEPARTMENT_NONFOOD_HOMEWARE
        self.DEPARTMENT_NONFOOD_LUXURY = DEPARTMENT_NONFOOD_LUXURY
        self.DEPARTMENT_NONFOOD_SUBTOTAL = DEPARTMENT_NONFOOD_SUBTOTAL
        self.DEPARTMENT_FOOD = DEPARTMENT_FOOD
        self.DEPARTMENT_TOTAL = DEPARTMENT_TOTAL
        self.CONVENIENCE_NONFOOD_DAILY = CONVENIENCE_NONFOOD_DAILY
        self.CONVENIENCE_NONFOOD_CHANDLERY = CONVENIENCE_NONFOOD_CHANDLERY
        self.CONVENIENCE_NONFOOD_CIGARETTE_ETC = CONVENIENCE_NONFOOD_CIGARETTE_ETC
        self.CONVENIENCE_NONFOOD_SUBTOTAL = CONVENIENCE_NONFOOD_SUBTOTAL
        self.CONVENIENCE_FOOD_BEVERAGE_PROCESSED = CONVENIENCE_FOOD_BEVERAGE_PROCESSED
        self.CONVENIENCE_FOOD_INSTANT_FRESH = CONVENIENCE_FOOD_INSTANT_FRESH
        self.CONVENIENCE_FOOD_SUBTOTAL = CONVENIENCE_FOOD_SUBTOTAL
        self.CONVENIENCE_TOTAL = CONVENIENCE_TOTAL
        self.SSM_NONFOOD_DAILY = SSM_NONFOOD_DAILY
        self.SSM_NONFOOD_CHANDLERY = SSM_NONFOOD_CHANDLERY
        self.SSM_NONFOOD_SUBTOTAL = SSM_NONFOOD_SUBTOTAL
        self.SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK = SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK
        self.SSM_FOOD_FRESH = SSM_FOOD_FRESH
        self.SSM_FOOD_PROCESSED = SSM_FOOD_PROCESSED
        self.SSM_FOOD_SUBTOTAL = SSM_FOOD_SUBTOTAL
        self.SSM_TOTAL = SSM_TOTAL

class Clothes(db.Model):
    __tablename__ = 'clothes'
    id = db.Column(db.Integer, primary_key= True)
    date_time = db.Column(db.DateTime, nullable = False)
    # categories = db.Column(db.String(20), nullable = False)
    total = db.Column(db.Integer, nullable = False)

    def __init__(self, date_time, total):

        self.date_time = date_time
        # self.categories = categories
        self.total = total

class Concert(db.Model):
    __tablename__ = 'concert'
    id = db.Column(db.Integer, primary_key=True)
    date_mon = db.Column(db.String(20), nullable=False)
    perform_num = db.Column(db.Integer, nullable=False)
    opening_num = db.Column(db.Integer, nullable=False)
    showing_num = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    book_num = db.Column(db.Integer, nullable=False)

    def __init__(self, date_mon, perform_num, opening_num, showing_num, sales, book_num):

        self.date_mon = date_mon
        self.perform_num = perform_num
        self.opening_num = opening_num
        self.showing_num = showing_num
        self.sales = sales
        self.book_num = book_num


class PhaseNewCoronic(db.Model):

    __tablename__ = 'phase_new_coronic'

    id = db.Column(db.Integer, primary_key=True)
    date_day = db.Column(db.DateTime, nullable=False)
    phase = db.Column(db.Integer, nullable=False)
    new_coronic = db.Column(db.Integer, nullable=False)

    def __init__(self, date_day, phase, new_coronic):

        self.date_day = date_day
        self.phase = phase
        self.new_coronic = new_coronic

class NaverComprehensiveData(db.Model):

    __tablename__ = 'naver_comprehensive_data'

    id = db.Column(db.Integer, primary_key= True)
    date_day = db.Column(db.DateTime, nullable=False)
    furniture = db.Column(db.Float, nullable= False)
    book = db.Column(db.Float, nullable=False)
    home_appliance = db.Column(db.Float, nullable=False)
    duty_free = db.Column(db.Float, nullable=False)
    living_health = db.Column(db.Float, nullable=False)
    sport_leisure = db.Column(db.Float, nullable=False)
    food = db.Column(db.Float, nullable=False)
    amenity = db.Column(db.Float, nullable=False)
    childbirth = db.Column(db.Float, nullable=False)
    fashion_clothes = db.Column(db.Float, nullable=False)
    fashion_accessories = db.Column(db.Float, nullable=False)
    beauty = db.Column(db.Float, nullable=False)


    def __init__(self,date_day, furniture, book, home_appliance, duty_free, living_health, sport_leisure,
                 food, amenity, childbirth, fashion_clothes, fashion_accessories, beauty):

        self.date_day = date_day
        self.furniture = furniture
        self.book = book
        self.home_appliance = home_appliance
        self.duty_free = duty_free
        self.living_health = living_health
        self.sport_leisure = sport_leisure
        self.food = food
        self.amenity = amenity
        self.childbirth = childbirth
        self.fashion_clothes = fashion_clothes
        self.fashion_accessories = fashion_accessories
        self.beauty = beauty

class SeoulBus(db.Model):
    __tablename__ = 'seoulbus'
    id = db.Column(db.Integer, primary_key=True)
    date_day = db.Column(db.DateTime, nullable=False)
    get_on = db.Column(db.Integer, nullable=False)
    get_off = db.Column(db.Integer, nullable=False)

    def __init__(self, date_day, get_on , get_off):
        self.date_day = date_day
        self.get_on = get_on
        self.get_off = get_off

class MetroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_day', 'get_on', 'get_off')

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_day', 'korea_sales', 'korea_audience_num', 'foreign_audience_num','foreign_sales',
                 'total_sales', 'total_audience')

class ConsumptionSchema(ma.Schema):
    class Meta:
        fields = ('ID', 'DATE', 'MARKET_NONFOOD_HOMEWARE_CULTURE', 'MARKET_NONFOOD_CLOTHING', 'MARKET_NONFOOD_DAILY', 'MARKET_NONFOOD_SPORT', 'MARKET_NONFOOD_CHANDLERY', 'MARKET_NONFOOD_SUBTOTAL',
                'MARKET_FOOD', 'MARKET_TOTAL', 'DEPARTMENT_NONFOOD_CHANDLERY', 'DEPARTMENT_NONFOOD_WOMENSUITS', 'DEPARTMENT_NONFOOD_WOMENCASUAL', 'DEPARTMENT_NONFOOD_MENCLOTHING', 'DEPARTMENT_NONFOOD_KIDS_SPORT',
                'DEPARTMENT_NONFOOD_HOMEWARE', 'DEPARTMENT_NONFOOD_LUXURY', 'DEPARTMENT_NONFOOD_SUBTOTAL', 'DEPARTMENT_FOOD', 'DEPARTMENT_TOTAL', 'CONVENIENCE_NONFOOD_DAILY', 'CONVENIENCE_NONFOOD_CHANDLERY',
                'CONVENIENCE_NONFOOD_CIGARETTE_ETC','CONVENIENCE_NONFOOD_SUBTOTAL', 'CONVENIENCE_FOOD_BEVERAGE_PROCESSED', 'CONVENIENCE_FOOD_INSTANT_FRESH', 'CONVENIENCE_FOOD_SUBTOTAL', 'CONVENIENCE_TOTAL',
                'SSM_NONFOOD_DAILY', 'SSM_NONFOOD_CHANDLERY', 'SSM_NONFOOD_SUBTOTAL', 'SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK', 'SSM_FOOD_FRESH', 'SSM_FOOD_PROCESSED', 'SSM_FOOD_SUBTOTAL', 'SSM_TOTAL')

class ClothesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_time', 'total')

class ConcertSchema(ma.Schema):
    class Meta:
        fields = ('id','date_mon', 'perform_num', 'opening_num','showing_num','sales','book_num')

class PhaseNewCoronicSchema(ma.Schema):
    class Meta:
        fields = ('id','date_day', 'phase','new_coronic')

class NaverComprehensiveDataSchema(ma.Schema):
    class Meta:
        fields = ('id','date_day', 'furniture', 'book', 'home_appliance', 'duty_free', 'living_health', 'sport_leisure',
                 'food', 'amenity', 'childbirth', 'fashion_clothes', 'fashion_accessories', 'beauty')

