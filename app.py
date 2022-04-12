from bs4 import BeautifulSoup
import requests
import urllib
import json
import re
from flask import Flask, request
import json as simplejson
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
import xlsxwriter 
import itertools
from xlsxwriter.workbook import WorksheetMeta
from xlsxwriter.worksheet import Worksheet  


app = Flask(__name__)


def getSuit1(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile1%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 1.xlsx') 
    worksheet = workbook.add_worksheet("suit1")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray

def getSuit2(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile2%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 2.xlsx') 
    worksheet = workbook.add_worksheet("suit2")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray

def getSuit3(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile3%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 3.xlsx') 
    worksheet = workbook.add_worksheet("suit3")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray

def getSuit4(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile4%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 4.xlsx') 
    worksheet = workbook.add_worksheet("suit4")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray

def getSuit5(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile5%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 5.xlsx') 
    worksheet = workbook.add_worksheet("suit5")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray


def getSuit6(status, buildNo):
    source=requests.get(
            'http://firestar-master.gqe.wdprapps.disney.com:8080/job/wdw-photopass-reg/view/3.%20Stage/job/wdw-photopass-reg_MagicMobile6%20Functional%20Test%20Suite%20-%20Stage/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Suit 6.xlsx') 
    worksheet = workbook.add_worksheet("suit6")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (cells[0].a.text[3:9])
                    testArray.append(cells[0].a.text[3:9])
                    worksheet.write(row, col, str(cells[0].a.text[3:9]))
                    row+=1
    workbook.close()
    return testArray



def getAndroid(status, buildNo):
    source=requests.get(
            'http://yoda-master.gqe.wdprapps.disney.com:8080/job/MDX_Photopass/job/MDX_Photopass_Android_StandaloneExecution/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Jenkins Result Android.xlsx') 
    worksheet = workbook.add_worksheet("Android")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (str(cells[0].a.text).replace("PhotoPass_Android_StandaloneExecution.", "")[5:11])
                    testArray.append(str(cells[0].a.text).replace("PhotoPass_Android_StandaloneExecution.", "")[5:11])
                    worksheet.write(row, col, str(cells[0].a.text).replace("MDX_Photopass_Android_MagicMobile.", "")[5:11])
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (str(cells[0].a.text).replace("PhotoPass_Android_StandaloneExecution.", "")[5:11])
                    testArray.append(str(cells[0].a.text).replace("PhotoPass_Android_StandaloneExecution.", "")[5:11])
                    worksheet.write(row, col, str(cells[0].a.text).replace("PhotoPass_Android_StandaloneExecution.", "")[5:11])
                    row+=1
    workbook.close()   
    return testArray

def getIos(status, buildNo):
    source=requests.get(
            'http://yoda-master.gqe.wdprapps.disney.com:8080/job/MDX_Photopass/job/MDX_Photopass_IOS_MagicMobile/'+buildNo+'/').text

    soup=BeautifulSoup(source, 'lxml')
    testArray = []
    table = soup.find('table', id='results')
    print (table)
    rows = table.find_all('tr', recursive=False)
    print (rows)
    workbook = xlsxwriter.Workbook('Jenkins Result IOS.xlsx') 
    worksheet = workbook.add_worksheet("IOS")
    row = 0
    col = 0
    for i in range (1, len(rows), 1):
            cells = rows[i].find_all('td', recursive=False)
            if (status == 'pass'):
                if (cells[1].div.text == 'Passed'):
                    print (cells[1].div.text)
                    print (str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    testArray.append(str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    worksheet.write(row, col, str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    row+=1
            else:
                if (cells[1].div.text == 'Failed'):
                    print (cells[1].div.text)
                    print (str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    testArray.append(str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    worksheet.write(row, col, str(cells[0].a.text).replace("MDX_Photopass_IOS_MagicMobile.", "")[5:11])
                    row+=1
    workbook.close()   
    return testArray


@app.route("/ios/<string:status>/<string:build>", methods=['GET'])
def ios(status, build):
    data = getIos(status, build)
    return dumps({'testids': data})

@app.route("/android/<string:status>/<string:build>", methods=['GET'])
def android(status, build):
    data = getAndroid(status, build)
    return dumps({'testids': data})



@app.route("/suit1/<string:status>/<string:build>", methods=['GET'])
def suit1(status, build):
    data = getSuit1(status, build)
    return dumps({'testids': data})

@app.route("/suit2/<string:status>/<string:build>", methods=['GET'])
def suit2(status, build):
    data = getSuit2(status, build)
    return dumps({'testids': data})

@app.route("/suit3/<string:status>/<string:build>", methods=['GET'])
def suit3(status, build):
    data = getSuit3(status, build)
    return dumps({'testids': data})

@app.route("/suit6/<string:status>/<string:build>", methods=['GET'])
def suit6(status, build):
    data = getSuit6(status, build)
    return dumps({'testids': data})

@app.route("/suit4/<string:status>/<string:build>", methods=['GET'])
def suit4(status, build):
    data = getSuit4(status, build)
    return dumps({'testids': data})

@app.route("/suit5/<string:status>/<string:build>", methods=['GET'])
def suit5(status, build):
    data = getSuit5(status, build)
    return dumps({'testids': data})





if __name__ == '__main__':
    app.run()
