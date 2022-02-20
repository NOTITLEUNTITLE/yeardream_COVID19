from flask import Flask, render_template, jsonify
from models import Clothes, Concert, PhaseNewCoronic, NaverComprehensiveData, Movie, Metro, Consumption, SeoulBus
from db_connect import db
import datetime


import json
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://seamus:elicerabbit@team4-db.clq1g0g3' \
                                        'exq8.ap-northeast-2.rds.amazonaws.com/csv_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False  #prevent sorting data by alphabet
db.init_app(app)
CORS(app)


@app.route('/clothes')
def clothes():
    rows = db.session.query(Clothes.id, Clothes.date_time, Clothes.total).all()


    #각 column 명을 뽑아내는 반복문
    for i in range(len(Clothes.__table__.columns.keys())):
        globals()['col{}'.format(i)] = Clothes.__table__.columns.keys()[i]


    data_list = []

    for row in rows:

        temp = ({col0:row[0],col1:row[1].strftime("%y%m%d"),col2:row[2]})


        data_list.append(temp)
    # print(type(data_list))


    return jsonify(data_list)



@app.route('/concert')
def concert():


    rows = db.session.query(Concert.id, Concert.date_mon, Concert.perform_num, Concert.opening_num, Concert.showing_num,
                            Concert.sales, Concert.book_num).all()

    for i in range(len(Concert.__table__.columns.keys())):
        globals()['col{}'.format(i)] = Concert.__table__.columns.keys()[i]
        # print(type(col0))


    concert_data = []
    for row in rows:
        # print(row[0])
        # row[1] = row[1].replace("-","")[2:]
        # dt = datetime.datetime.strptime(row[1], '%y%m')
        # print(dt)
        temp = ({col0:row[0],col1:row[1].replace("-","")[2:],col2:row[2],col3:row[3],col4:row[4],col5:row[5],col6:row[6]})

        # print(col1, row[1])
        # print(type(col1))
        print(row[1].replace("-","")[2:])
        # print(type(row[1]))
        concert_data.append(temp)

    return jsonify(concert_data)

@app.route('/phase_new_coronic')
def phase_new_coronic():



    rows = db.session.query(PhaseNewCoronic.id, PhaseNewCoronic.date_day, PhaseNewCoronic.phase,
                            PhaseNewCoronic.new_coronic).all()


    for i in range(len(PhaseNewCoronic.__table__.columns.keys())):
        globals()['col{}'.format(i)] = PhaseNewCoronic.__table__.columns.keys()[i]
        # print(type(col0))


    phase_new_coronic_data = []
    for row in rows:
        # print(row[0])
        temp = ({col0:row[0],col1:row[1].strftime("%y%m%d"),col2:row[2],col3:row[3]})

        phase_new_coronic_data.append(temp)

    return jsonify(phase_new_coronic_data)

#######################################


@app.route('/naver_data')
def naver_comporehensive():


    rows = db.session.query(NaverComprehensiveData.id, NaverComprehensiveData.date_day, NaverComprehensiveData.furniture,
                            NaverComprehensiveData.book, NaverComprehensiveData.home_appliance, NaverComprehensiveData.duty_free,
                            NaverComprehensiveData.living_health, NaverComprehensiveData.sport_leisure,NaverComprehensiveData.food,
                            NaverComprehensiveData.amenity, NaverComprehensiveData.childbirth, NaverComprehensiveData.fashion_clothes,
                            NaverComprehensiveData.fashion_accessories, NaverComprehensiveData.beauty).all()

    for i in range(len(NaverComprehensiveData.__table__.columns.keys())):
        globals()['col{}'.format(i)] = NaverComprehensiveData.__table__.columns.keys()[i]

    naver_comporehensive_data = []
    for row in rows:
        # print(row[0])
        temp = ({col0:row[0],col1:row[1].strftime("%y%m%d"),col2:row[2],col3:row[3],col4:row[4],col5:row[5],col5:row[5],col6:row[6],col7:row[7],
                 col8:row[8],col9:row[9],col10:row[10],col11:row[11],col12:row[12],col13:row[13]})

        naver_comporehensive_data.append(temp)

    return jsonify(naver_comporehensive_data)


#######################################

@app.route('/movie')
def movie():

    rows = db.session.query(Movie.id, Movie.date_day, Movie.korea_sales, Movie.korea_audience_num,
                            Movie.foreign_audience_num, Movie.foreign_sales, Movie.total_sales, Movie.total_audience).all()

    for i in range(len(Movie.__table__.columns.keys())):
        globals()['col{}'.format(i)] = Movie.__table__.columns.keys()[i]
        print(type(col0))

    movie_data = []
    for row in rows:
        # print(row[0])
        # row[1] = row[1].strftime("%y%m%d")
        temp = ({col0:row[0],col1:row[1].strftime("%y%m%d"),col2:row[2],col3:row[3],col4:row[4],col5:row[5],col6:row[6],col7:row[7]})

        movie_data.append(temp)
        # print(row[1].strftime("%y%m%d"))
        # print(type(row[1].strftime("%y%m%d")))

    return jsonify(movie_data)

@app.route('/metro')
def metro():

    rows = db.session.query(Metro.id, Metro.date_day, Metro.get_on,
                            Metro.get_off).all()

    for i in range(len(Metro.__table__.columns.keys())):
        globals()['col{}'.format(i)] = Metro.__table__.columns.keys()[i]

    metro_date = []
    for row in rows:
        # print(row[0])
        temp = ({col0:row[0],col1:row[1].strftime("%y%m%d"),col2:row[2],col3:row[3]})

        metro_date.append(temp)

    return jsonify(metro_date)

#######################################

@app.route('/consumption')
def consumption():
    rows = db.session.query(Consumption.ID, Consumption.DATE_MON, Consumption.MARKET_NONFOOD_HOMEWARE_CULTURE ,Consumption.MARKET_NONFOOD_CLOTHING, Consumption.MARKET_NONFOOD_DAILY,
                            Consumption.MARKET_NONFOOD_SPORT, Consumption.MARKET_NONFOOD_CHANDLERY, Consumption.MARKET_NONFOOD_SUBTOTAL,
                            Consumption.MARKET_FOOD, Consumption.MARKET_TOTAL, Consumption.DEPARTMENT_NONFOOD_CHANDLERY,Consumption.DEPARTMENT_NONFOOD_WOMENSUITS, Consumption.DEPARTMENT_NONFOOD_WOMENCASUAL,
                            Consumption.DEPARTMENT_NONFOOD_MENCLOTHING, Consumption.DEPARTMENT_NONFOOD_KIDS_SPORT, Consumption.DEPARTMENT_NONFOOD_HOMEWARE, Consumption.DEPARTMENT_NONFOOD_LUXURY,
                            Consumption.DEPARTMENT_NONFOOD_SUBTOTAL, Consumption.DEPARTMENT_FOOD, Consumption.DEPARTMENT_TOTAL, Consumption.CONVENIENCE_NONFOOD_DAILY, Consumption.CONVENIENCE_NONFOOD_CHANDLERY,
                            Consumption.CONVENIENCE_NONFOOD_CIGARETTE_ETC, Consumption.CONVENIENCE_NONFOOD_SUBTOTAL, Consumption.CONVENIENCE_FOOD_BEVERAGE_PROCESSED, Consumption.CONVENIENCE_FOOD_INSTANT_FRESH,
                            Consumption.CONVENIENCE_FOOD_SUBTOTAL, Consumption.CONVENIENCE_TOTAL, Consumption.SSM_NONFOOD_DAILY, Consumption.SSM_NONFOOD_CHANDLERY, Consumption.SSM_NONFOOD_SUBTOTAL,
                            Consumption.SSM_FOOD_AGRICULTURAL_MARINE_LIVESTOCK, Consumption.SSM_FOOD_FRESH, Consumption.SSM_FOOD_PROCESSED, Consumption.SSM_FOOD_SUBTOTAL, Consumption.SSM_TOTAL).all()

    for i in range(len(Consumption.__table__.columns.keys())):
        globals()['col{}'.format(i)] = Consumption.__table__.columns.keys()[i]

    Consumption_data = []
    for row in rows:
        # print(row[0])
        temp = (
        {col0: row[0], col1: row[1].strftime("%y%m%d"), col2: row[2], col3: row[3], col4: row[4], col5: row[5], col5: row[5], col6: row[6], col7: row[7], col8: row[8], col9: row[9], col10: row[10],
         col11: row[11], col12: row[12], col13: row[13], col14: row[14], col15: row[15], col16: row[16], col17: row[17], col18: row[18], col19: row[19], col20: row[20], col21: row[21],
         col22: row[22], col23: row[23], col24 : row[24], col25: row[25], col26: row[26], col27: row[27], col28: row[28], col29: row[29], col30: row[30], col31: row[31], col32: row[32],
         col33: row[33], col34: row[34], col35: row[35]})

        Consumption_data.append(temp)

    return jsonify(Consumption_data)

@app.route('/seoulbus')
def seoulbus():


    rows = db.session.query(SeoulBus.id, SeoulBus.date_day, SeoulBus.get_on,
                            SeoulBus.get_off).all()

    for i in range(len(SeoulBus.__table__.columns.keys())):
        globals()['col{}'.format(i)] = SeoulBus.__table__.columns.keys()[i]

    SeoulBus_date = []
    for row in rows:
        # print(row[0])
        temp = ({col0: row[0], col1: row[1].strftime("%y%m%d"), col2: row[2], col3: row[3]})

        SeoulBus_date.append(temp)

    return jsonify(SeoulBus_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)

                                                                                                                                                                                                                                                                                                            223,0-1       B
