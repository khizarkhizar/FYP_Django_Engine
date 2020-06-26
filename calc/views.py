import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from . import main

from django import forms
from django.views.generic import View
import json
import firebase_admin
from firebase_admin import credentials, firestore
import random
import serial


cred = credentials.Certificate(
    "calc/precautionary-of-fire-system-firebase-adminsdk-ikj23-7a83f45714.json")
a = firebase_admin.initialize_app(cred)
db = firestore.client()

tmaxRange = []
tminRange = []
gmaxRange = []
gminRange = []
fminRange = []
fmaxRange = []
port = []
alert1 = ""
no = 0


def home(request):
    # Opening JSON file
    with open('templates/sensors.json') as json_file:
        data = json.load(json_file)
    tmaxRange.clear()
    tminRange.clear()
    gmaxRange.clear()
    gminRange.clear()
    fminRange.clear()
    fmaxRange.clear()
    port.clear()
    a = []
    if request.GET:
        try:
            if request.GET['1'] == 'on':
                tmaxRange.append(request.GET["maxRange1"])
                tminRange.append(request.GET["minRange1"])
            if request.GET['2'] == 'on':
                gmaxRange.append(request.GET["maxRange2"])
                gminRange.append(request.GET["minRange2"])

            if request.GET['3'] == 'on':
                fmaxRange.append(request.GET["maxRange3"])
                fminRange.append(request.GET["minRange3"])
            if request.GET['port']:
                port.append(request.GET["port"])

        except Exception as e:
            a.append('<center >     <h1>    plz select the ' + str(e) +
                     ' sensor</h1> <button><a class="btn" href="/">Go Back</a></button></center>')
            return HttpResponse(a)

    return render(request, 'home.html', {'file': data['sensor']})


def Addsensor(request):
    if request.GET:
        print(request.GET["Naam"])
        print(request.GET["minRange"])
        print(request.GET["maxRange"])
    # read Data base

    # with open('templates\data.json', 'w') as outfile:
    #     json.dump(sensorData, outfile)

    return render(request, 'addSensor.html')


def get_data(request):
    data = {}
    if request.is_ajax():
        sensor_val = 0.3
        sensor_data = []
        now = datetime.datetime.now()
        ok_date = (str(now.strftime('%Y-%m-%d %H:%M:%S')))
        try:
            tData = random.random() * 150
            gData = random.random()*600
            fData = 0
            #sr = serial.Serial("COM9", int(port[0]))
            # st = list(str(sr.readline(), 'utf-8'))
            # sr.close()
            # sensor_val = str(''.join(st[:]))
            # tData, gData, fData = get_custom_class(no)
            # no=no+1
            defuzz, alert, aggregated = main.Fuzzy(
                tData, gData, fData, int(tminRange[0])*1, int(tmaxRange[0])*1, int(gminRange[0])*1, int(gmaxRange[0])*1)
            # print(tData, ',', gData, ',', defuzz, ',', alert)

            if (defuzz):
                sensor_data.append(str(defuzz)+','+ok_date+','+alert)
            else:
                sensor_data.append(str(defuzz)+','+ok_date+','+alert)
        except Exception as x:
            pass
        data['result'] = sensor_data

    else:
        data['result'] = 'fail'

    return JsonResponse(data)

# [START custom_class_def]


def check(request):
    # c1 = request.GET('temp')
    # print("cdd")
    # get_custom_class()
    return render(request, 'chart.html')


class FYP(object):
    def __init__(self, temparature_Sensor, gas_Sensor, flame_Sensor, Date):
        self.temparature_Sensor = temparature_Sensor
        self.gas_Sensor = gas_Sensor
        self.flame_Sensor = flame_Sensor
        self.Date = Date

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        val = FYP(source[u'temparature_Sensor'], source[u'gas_Sensor'],
                  source[u'flame_Sensor'], source[u'Date'])

        return val
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'temparature_Sensor': self.temparature_Sensor,
            u'gas_Sensor': self.gas_Sensor,
            u'flame_Sensor': self.flame_Sensor,
            u'Date': self.Date
        }

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return(
            u'FYP(temparature_Sensor={}, gas_Sensor={}, flame_Sensor={}, Date={})'
            .format(self.temparature_Sensor, self.gas_Sensor, self.flame_Sensor, self.Date))
# [END custom_class_def]


# Custom Add data

def add_example_data():
    db = firestore.client()
    now = datetime.datetime.now()
    ok_date = (str(now.strftime('%d/%m/%Y %H:%M:%S')))
    cities_ref = db.collection(u'Sensors_data').document()
    cities_ref.set(
        FYP(120, 200, 0, ok_date).to_dict())
    # [END add_example_data]


# Custom retrive data


def get_custom_class():

    db = firestore.client()
    # [START get_custom_class]
    users_ref = db.collection(u'Sensors_data')
    docs = users_ref.stream()
    sensorData = []
    for doc1 in docs:
        sensorData.append(doc1.id)
    doc_ref = db.collection(u'Sensors_data').document(sensorData[0])
    doc = doc_ref.get()
    val = FYP.from_dict(doc.to_dict())
    return val.temparature_Sensor, val.gas_Sensor, val.flame_Sensor


def History(request):

    # Opening JSON file
    with open('templates\data.json') as json_file:
        data = json.load(json_file)

        # Print the type of data variable
    print(float(data['data'][0]['id']))
    Date = '23/06/2020 20:45:34'

    # Query

    val = []
    no = 0
    d = 0
    if request.GET:
        Date = request.GET["datetimepicker"]
        new = list(Date)
        for k in range(0, 4):
            if no > 9:
                no = 0
                d = d+1
            new[14] = str(d)
            new[15] = str(no)
            Date = ''.join(new)
            no = no+1
            print(Date)
            for i in range(0, 60):

                if i < 10:
                    Date1 = Date+':0'+str(i)
                else:
                    Date1 = Date+':'+str(i)
                print(i)
                docs = (db.collection(u'Sensors_data').where(
                    u'Date', u'==', Date1).stream())

                for doc in docs:
                    val.append(FYP.from_dict(doc.to_dict()))
                    print(i)

    return render(request, 'history.html', {'name': val})

    # return render(request, 'history.html', {'name': data['data']})
