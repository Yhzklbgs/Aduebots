# GATAU GW BUAT APAAN DAH LAH PAKE AJA
# GABUT CORONA
from Libs.linepy import *
from Libs.akad.ttypes import *
from time import sleep
from datetime import datetime, timedelta
import time
import livejson
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback, pafy



client = LINE("YOUR_TOKEN", appType='YOUR_APPNAME')
oepoll = OEPoll(client)
roleJson = livejson.File("role.json",True, True, 4)
settings = livejson.File("settings.json",True, True, 4)
staff = roleJson['staff']
owner = 'YOUR_MID'

def logError(text):
    client.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if op.param2 in staff:
                client.acceptGroupInvitation(op.param1)
                client.sendMessage(op.param1," 「 отмена 」\n отмена is STARTING♪\n'abort' to abort♪")
                client.sendMessage(op.param1," 「 отмена 」\n shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                group = client.getGroup(op.param1)
                if group.invitee is None:
                    client.sendMessage(op.param1, "Nothing Members Pending, I Leave See Ya >.<")
                    client.leaveGroup(op.param1)
                else:
                    group = client.getGroup(op.param1)
                    groupinvitingmembersmid = [contact.mid for contact in group.invitee]
                    for _mid in groupinvitingmembersmid:
                        client.cancelGroupInvitation(op.param1, [_mid])
                        time.sleep(0.8)
                    client.sendMessage(op.param1, "Type .bye if u done using bots")
            else:
                client.acceptGroupInvitation(op.param1)
                client.sendMessage(op.param1, 'GAUSAH MAKE BOT GW KONTOL IZIN DULU SAMA OWNER')
                client.leaveGroup(op.param1)     
        if op.type == 26:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            if msg.contentType == 0:
                if cmd == '.bye':
                    client.leaveGroup(to)
                if cmd == '.clearstaff':
                    roleJson['staff'] = []
                    print('success clear staff')
                elif cmd.startswith('staffadd ') and sender in owner:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                            try:
                                roleJson['staff'].append(target)
                                print('Success add staff')
                                client.sendMessage(to,"Success added staff")
                            except Exception as e:
                                print(e)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
thread2 = threading.Thread()
thread2.daemon = True
thread2.start()
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
    
