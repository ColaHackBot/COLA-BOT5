from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
#======================================================================================
botStart = time.time()
#======================================================================================

maxgie = LINE('')
maxgie.log("Auth Token : " + str(maxgie.authToken))
maxgie.log("Timeline Token : " + str(maxgie.tl.channelAccessToken))

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
maxgieMID = maxgie.profile.mid
maxgieProfile = maxgie.getProfile()
maxgieSettings = maxgie.getSettings()
#==============================================================================#
maxgiePoll = OEPoll(maxgie)
maxgieMID = maxgie.getProfile().mid
admin = [maxgieMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}

#==============================================================================#
did = {"join": True,}
kcn = {"autojoin": False,"Members":5,}
sets = {
    "l":True, 
      "c":True, 
      "cm":"Auto Like By.HACK_BOT\nline://ti/p/~HACK_BOT",  
    "winvite": False,
    "wblacklist": False,
    "tagsticker": False,
    "Sticker": False,
    "autoJoin": False,
    "autoCancel": False,
    "autoJoinTicket": False,
   "changePictureProfile": False, 
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "วิธีตั้งแทค \n- ตั้งแทค ข้อความที่ต้องการ",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "ยินดีต้อนรับเข้ากลุ่มนะครับ 😃",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
    "b": "บัญชีนี้ถูกป้องกันด้วย Self Bot By. HACK_BOT ระบบได้บล็อคบัญชีคุณอัตโนมัติ >_<",
    "c":"Auto Like By. HACK_BOT",
    "m": "สวัสดีครับ ผมมุดลิ้งมานะครับ >_<",
}
apalo = {
    "winvite": False,
    "wblacklist": False,
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#333333","t": "#6600CC"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = maxgieMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = maxgie.getProfile() 
backup = maxgie.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = maxgieProfile.displayName
settings["myProfile"]["statusMessage"] = maxgieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = maxgieProfile.pictureStatus
cont = maxgie.getContact(maxgieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = maxgie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = maxgieProfile.statusMessage
ProfileMe["pictureStatus"] = maxgieProfile.pictureStatus
coverId = maxgie.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        maxgie.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = maxgie.getContact(mid)
    if contact.videoProfile == None:
        maxgie.cloneContactProfile(mid)
    else:
        profile = maxgie.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxgie.getProfileDetail(mid)['result']['objectId']
    maxgie.updateProfileCoverById(coverId)
def backupProfile():
    profile = maxgie.getContact(maxgieMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = maxgie.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = maxgie.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        maxgie.updateProfileAttribute(8, profile.pictureStatus)
        maxgie.updateProfile(profile)
    else:
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    maxgie.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        maxgie.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = maxgie.getGroup(msg.to).name
    sd = maxgie.waktunjir()
    maxgie.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = maxgie.getContact(to)
        profile = maxgie.profile
        profileName = maxgie.profile
        profileStatus = maxgie.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        maxgie.updateProfile(profileName)
        maxgie.updateProfile(profileStatus)
        profile.pictureStatus = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if maxgie.getProfileCoverId(to) is not None:
            maxgie.updateProfileCoverById(maxgie.getProfileCoverId(to))
        maxgie.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return maxgie.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        maxgie.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(maxgie.getContact(maxgieMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus)
        ticket = "https://line.me/ti/p/~topzalove123"
        maxgie.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def ggggg(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d วัน\n───────────\n%02d ชั่วโมง\n───────────\n%02d นาที\n───────────\n' %(days ,hours, mins)
    
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    maxgie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(maxgie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxgie.getContact("ua053fcd4c52917706ae60c811e39d3ea").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxgie.genOBSParams({'oid': maxgieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxgie.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxgie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxgie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    maxgie.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
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
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = maxgie.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        maxgie.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("\n ข้อความจากคุณ นนท์ \n")
    print("\n BoT-Lnw-NoN-Thailand \n")
    print ("\n รับ  ลิงก์ เพื่อล็อคอินใหม่ด้วยครับ \n")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
#    with open("stickerz.json","r") as fp:
#        stickerz = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': maxgie.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + maxgie.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            maxgie.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
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
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def duc1(to, duc1):
    data={
"type": "flex",
"altText": duc1,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#000000"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": duc1,
"color":"#00FF00",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#=====================================================================

async def maxgieBot(op):
    try:
        if settings["restartPoint"] != None:
            maxgie.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
             # if op.param2 in admin:
                 # return
              maxgie.findAndAddContactsByMid(op.param1)
              maxgie.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              #if op.param2 in admin:
                 # return
              maxgie.sendMessage(op.param1,tagadd["b"])
          #    msgSticker = sets["messageSticker"]["listSticker"]["block"]
          #    if msgSticker != None:
          #        sid = msgSticker["STKID"]
          #        spkg = msgSticker["STKPKGID"]
          #        sver = msgSticker["STKVER"]
          #        sendSticker(op.param1, sver, spkg, sid)
                    #maxgie.sendMessage(op.param1,tagaad["b"])
              maxgie.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
         if kcn["autojoin"] == True:
             G = maxgie.getCompactGroup(op.param1)
             if len(G.members) <= kcn["Members"]:
                 maxgie.acceptGroupInvitation(op.param1)
                 maxgie.leaveGroup(op.param1)               	
             else:
                 maxgie.acceptGroupInvitation(op.param1)
                 
        if op.type == 13:
            if maxgieMID in op.param3:
                if did["join"] == True:
                    friend = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(friend)
                    for ids in kontak:
                      The = ids.mid
                      if op.param2 not in The:
                          try:
                             maxgie.acceptGroupInvitation(op.param1)
                             ginfo = maxgie.getGroup(op.param1)
                          except:
                             maxgie.acceptGroupInvitation(op.param1)
                             ginfo = maxgie.getGroup(op.param1)
                             maxgie.sendMessage(op.param1,"BYE BYE~~")
                             maxgie.leaveGroup(op.param1)
        if op.type == 13:
            if maxgieMID in op.param3:
                G = maxgie.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            maxgie.acceptGroupInvitation(op.param1)
                        else:
                            maxgie.leaveGroup(op.param1)
                    else:
                        maxgie.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        maxgie.acceptGroupInvitation(op.param1)
                        maxgie.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxgie.acceptGroupInvitation(op.param1, matched_list)
                    maxgie.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00FFFF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนออกกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~HACK_BOT"
                     #      
                     #   "
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "〖 สวัสดีสมาชิกใหม่ 〗\n"
            s += "\n• ชื่อกลุ่ม : {}".format(gname)
            s += "\n• ชื่อคนเข้ากลุ่ม : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00FFFF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~HACK_BOT"
                           #"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            cover = maxgie.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#000000'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#00FFFF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#00FFFF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
#=====================================================================
       # if op.type == 26:
         #   print ("[ 26 ] RECEIVE MESSAGE")
         #   msg = op.message
         #   text = str(msg.text)
         #   msg_id = msg.id
         #   receiver = msg.to
         #   sender = msg._from
         #   cmd = command(text)
         #   setKey = settings["keyCommand"].title()
         #   if settings["setKey"] == False: setKey = ""
         #   isValid = True
         #   if isValid != False:
               # if msg.toType == 0 and sender != maxgieMID: to = sender
               # else: to = receiver
               # if msg.toType == 0 and settings["replays"] and sender != maxgieMID:
                   # contact = maxgie.getContact(sender)
                    #if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                     #   msgSticker = sets["messageSticker"]["listSticker"]["replay"]
                     #   if msgSticker != None:
                     #       sid = msgSticker["STKID"]
                     #       spkg = msgSticker["STKPKGID"]
                     #       sver = msgSticker["STKVER"]
                     #       sendSticker(to, sver, spkg, sid)
                     #   if "@!" in settings["reply"]:
                     #       msg_ = settings["reply"].split("@!")
                     #       sendMention(to, sender, "「 แทคส่วนตัว 」\n" + msg_[0], msg_[1])
                     #   maxgie.sendMessage(to, "「 แทคส่วนตัว 」\n", settings["reply"])
                     
        if op.type == 24:
            if settings["autoLeave"] == True:
                maxgie.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if apalo["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = maxgie.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 maxgie.sendMessage(msg.to,"-> " + _name + " ทำการเชิญสำเร็จ")
                                 break
                             elif invite in apalo["blacklist"]:
                                 maxgie.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 maxgie.sendMessage(msg.to,"ใช้คำสั่ง!,ล้างดำ,ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     maxgie.findAndAddContactsByMid(target)
                                     maxgie.inviteIntoGroup(msg.to,[target])
                                     maxgie.sendMessage(msg.to,"เชิญ :" + _name + "เรียบร้อย")
                                     apalo["winvite"] = False
                                     break
                                 except:
                                     try:
                                         maxgie.findAndAddContactsByMid(invite)
                                         maxgie.inviteIntoGroup(op.param1,[invite])
                                         apalo["winvite"] = False
                                     except:
                                         maxgie.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         apalo["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [maxgieMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg._from not in maxgieMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        maxgie.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        maxgie.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          maxgie.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "🌟เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว🌟")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "🌟เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว🌟")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          maxgie.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
        if op.type in [25,26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        try:
                            if sets["l"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                duc1(to,"🌟ไลค์ให้แล้วนะครับ🌟")
                                if purl[1] not in wait['postId']:
                                    maxgie.likePost(purl[0], purl[1], random.choice([1001]))
                                if sets["c"] == True:
                                    maxgie.createComment(purl[0], purl[1], sets["cm"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if sets["l"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    duc1(to,"🌟ไลค์ให้แล้วนะครับ🌟")
                                    if purl[1] not in wait['postId']:
                                        maxgie.likePost(msg._from, purl[1], random.choice([1001]))
                                    if sets["c"] == True:
                                        maxgie.createComment(msg._from, purl[1], sets["cm"])
                                        wait['postId'].append(purl[1])
                                    else:pass
              
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] ข้อความ ที่เราส่ง")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "ประกาศ":
                    sa="วิธีใช้ ประกาศกลุ่ม >\\<"
                    sa+="\n- ประกาศ ข้อความ/ไอดีไลน์"
                    sa+="\nตัวอย่าง >\\<"
                    sa+="\n- ประกาศ มอนิ่ง/HACK_BOT"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~HACK_BOT"}}
                    sendTemplate(to,data)
                if text. lower() == "คำสั่งแอด":
                    sa="ชุดคำสั่งแอดมิน/ผู้สร้าง\n"
                    sa+="\n - Sp = เช็คความเร็วบอท \n"
                    sa+="\n - ทัก @ = เตะสมาชิก \n"
                    sa+="\n - ขายของ = สั่งบอทขายของ \n"
                    sa+="\n - เทส = เช็คบอท \n"
                    sa+="\n - ออน = ดูเวลาทำงานบอท \n"
                    sa+="\n - ยกเชิญ = สั่งบอทยกค้างเชิญ \n"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~HACK_BOT"}}
                    sendTemplate(to,data)
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~HACK_BOT"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "วิธีใช้ stag >\\<"
                    sa += "\n- stag [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~HACK_BOT"}}
                    sendTemplate(to,data)
                if text.lower() == "สะกด":
                    sa = "วิธีใช้ สะกด >\\<"
                    sa += "\n- สะกดกิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกด รักทอป @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~HACK_BOT"}}
                    sendTemplate(to,data)
                if text.lower() == "สติกเกอร์":
                    sa="🇹🇭 ชุดคำ สั่งส่ง สติกเกอร์ ของ นนท์ 🇹🇭"
                    sa+="\n- บึ้ม"
                    sa+="\n- นักฆ่า"
                    sa+="\n- เค้าสั่น"
                    sa+="\n- เค้างง"
                    sa+="\n- เค้าดีใจ"
                    sa+="\n- เค้าเขิล"
                    sa+="\n- เค้าอาย"
                    sa+="\n- เค้าเชื่อ"
                    sa+="\n- เค้าโอเค"
                    sa+="\n- เค้าไม่เถียง"
                    sa+="\n- เค้าวิ่ง"
                    sa+="\n- เค้าเครียด"
                    sa+="\n- เค้าหิว"
                    sa+="\n- เค้าพร้อม"
                    sa+="\n- เค้าชอบ"
                    sa+="\n- เค้าอาบน้ำ"
                    sa+="\n- เค้าจะเอา"
                    sa+="\n- จัดไป"
                    sa+="\n- โยกๆ"
                    sa+="\n- ว้าว"
                    sa+="\n- ขอบคุณ"
                    sa+="\n- เห้อ"
                    sa+="\n- เบื่อ"
                    sa+="\n- โอเค"
                    sa+="\n- กัปตัน"
                    sa+="\n- วานด้า"
                    sa+="\n- แนท"
                    sa+="\n- ฟรุ้งฟริง"
                    sa+="\n- ยิง"
                    sa+="\n- บาย"
                    sa+="\n- หึหึ"
                    sa+="\n- เย่"
                    sa+="\n- เบิดเดย์"
                    sa+="\n- ชอบ"
                    sa+="\n- น่ารัก"
                    sa+="\n- รักนะ"
                    sa+="\n- เหรอ"
                    sa+="\n- ร้อน"
                    sa+="\n- จุฟๆ"
                    sa+="\n- สวัสดี"
                    sa+="\n- โหล"
                    sa+="\n- ฝันดี"
                    sa+="\n- เผ่น"
                    sa+="\n- เพลียย"
                    sa+="\n- เร็ว"
                    sa+="\n- ล้อเล่นๆ"
                    sa+="\n- พิม่อน"
                    sa+="\n- เหอะๆ"
                    sa+="\n- ยิง2"
                    sa+="\n- มานี่"
                    sa+="\n- อ้อนๆ"
                    sa+="\n- สติช"
                    sa+="\n- สติช2"
                    sa+="\n- สติช3"
                    sa+="\n- ทีมบิน"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~thenon2016"}}
                    sendTemplate(to,data)
                if text.lower() == "เช็ค" or text.lower() == "set":
                    sas = "☆ Settings ☆"
                    if settings["autoAdd"] == True: sa = "\n• ออโต้แอด ( เปิด )"
                    else:sa = "\n• ออโต้แอด ( ปิด )"
                    if settings["autoblock"] == True: sa += "\n• ออโต้บล็อค ( เปิด )"
                    else:sa += "\n• ออโต้บล็อค ( ปิด )"
                    if settings["autoCancel"]["on"] == True: sa +="\n• ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n• ปฏิเสธกลุ่มเชิญ ( ปิด )"
                    if tagadd["tags"] == True: sa += "\n• ตอบกลับคนแทค ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค ( ปิด )"
                    if tagadd["tagss"] == True: sa += "\n• ตอบกลับคนแทค2 ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค2 ( ปิด )"
                    if sets["tagsticker"] == True: sa += "\n• แทคสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• แทคสติ๊กเกอร์ ( ปิด )"
                    if settings["autolike"] == True: sa += "\n• ออโต้ไลค์ ( เปิด )"
                    else:sa += "\n• ออโต้ไลค์ ( ปิด )"
                    if settings["com"] == True: sa += "\n• คอมเม้นโพส ( เปิด )"
                    else:sa += "\n• คอมเม้นโพส ( ปิด )"
                    if settings["Welcome"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม ( ปิด )"
                    if settings["Wc"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( ปิด )"
                    if settings["wcsti2"] == True: sa += "\n• ติ๊กคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนเข้ากลุ่ม ( ปิด )"
                    if settings["Leave"] == True: sa += "\n• คนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• คนออกกลุ่ม ( ปิด )"
                    if settings["lv"] == True: sa += "\n• ติ๊กคนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนออกกลุ่ม ( ปิด )"
                    if settings["unsendMessage"] == True: sa += "\n• ตรวจจับยกเลิก ( เปิด )"
                    else:sa += "\n• ตรวจจับยกเลิก ( ปิด )"
                    if settings["Sticker"] == True: sa += "\n• เชคติ๊กใหญ่ ( เปิด )"
                    else:sa += "\n• เชคติ๊กใหญ่ ( ปิด )"
                    if sets["Sticker"] == True: sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( ปิด )"
                    
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#00FFFF",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#00FFFF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'clearban' or text.lower() == "ล้างดำ":
                      apalo["Talkblacklist"] = []
                      duc1(to, "🌟สำเร็จ🌟")
                
                elif text.lower() == "คทดำ":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟ไม่มีคท.คนติดดำ🌟")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif text.lower() == "เตะดำ":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in maxgie.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            duc1(to, "🌟ไม่มีหมาดำ🌟")
                        else:
                            for mids in matched_list:
                                try:
                                    maxgie.kickoutFromGroup(to, [mids])
                                except:pass
                
                elif "Kick " in msg.text:
                    Ri0 = text.replace("kick ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                except:
                                    pass                              
                              
                elif "ล้อเล่น " in msg.text:
                    Ri0 = text.replace("ล้อเล่น ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(to,[target])
                                except:
                                    pass
                                         
                elif "ทัก " in msg.text:
                        vkick0 = msg.text.replace("ทัก ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = maxgie.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    maxgie.kickoutFromGroup(msg.to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    #maxgie.inviteIntoGroup(msg.to,[target])
                                    #maxgie.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass            
                elif msg.text.lower().startswith("สีme "):
                            text_ = removeCmd("สีme", text)
                            try:
                                temp["t"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("สีอักษร "):
                            text_ = removeCmd("สีอักษร", text)
                            try:
                                temp["te"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสี me\nพิม'ตั้งสีme #333333'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสี tag\nพิม'ตั้งสีแทค #333333'"
                            maxgie.sendImageWithURL(to,c)
                            maxgie.sendImageWithURL(to,p)
                            maxgie.sendMessage(to,m)
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                maxgie.sendMessage(to,"「 ตั้งบล็อคอัตโนมัติ 」\nคือ : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟สำเร็จแล้ววว🌟")
                elif text.lower().startswith("ตั้งค้างเชิญ "):
                            text_ = removeCmd("ตั้งค้างเชิญ", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                maxgie.sendMessage(to,"「 ตั้งยกค้างเชิญ 」\nจำนวน : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟สำเร็จแล้ววว🌟")
                if text.lower() == "ดำ":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟ส่งคทลงมา...🌟")
                if text.lower() == "ขาว":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟ส่งคทลงมา...🌟")
                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งแทคแชท "):
                      text_ = removeCmd("ตั้งแทคแชท", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                      text_ = removeCmd("ตั้งต้อนรับ", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                maxgie.sendMessage(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("ตั้งแอด "):
                      text_ = removeCmd("ตั้งแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ตั้งแอด 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          settings["commet"] = text_
                          sa = "「 ตั้งคอมเม้น 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "HACK_BOT", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower() == "ทัก":
                  if msg.toType == 0:
                     sendMention(to, to, "──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──\n", "\n──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──")
                  elif msg.toType == 2:
                     group = maxgie.getGroup(to)
                     contact = [mem.mid for mem in group.members]
                     mentionMembers(to, contact)       
                if text.lower() == "เชค":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    maxgie.generateReplyMessage(msg.id)
                    duc1.sendMessags(id, to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b)+"\n\nข้อความแทคแชท :\n"+str(Re))
                if text.lower() == "/คำสั่ง" or text.lower() == "/help":
                    sas = "😀 Help Message 😀\n"
                    sa = "• คท\n"
                    sa += "• ไอดีเรา\n"
                    sa += "• ชื่อเรา\n"
                    sa += "• ตัสเรา\n"
                    sa += "• รูปเรา\n"
                    sa += "• รูปวีดีโอเรา\n"
                    sa += "• ปกเรา\n"
                    sa += "──────────────\n"
                    sa += "• ข้อมูล\n"
                    sa += "• ออน\n"
                    sa += "• รีบอท\n"
                    sa += "• แทค\n"
                    sa += "• ยกเชิญ\n"
                    sa += "• /ลบรัน\n"
                    sa += "• ก็อป @user\n"
                    sa += "• กลับร่าง\n"
                    sa += "──────────────\n"
                    sa += "• สะกดกิต [พิม'สะกดกิต'เพื่อดูวิธี]\n"
                    sa += "• ตั้งapi [พิมเพื่อดูวิธี]\n"
                    sa += "• ล้างapi [คำที่จะลบ]\n"
                    sa += "• เชคapi\n"
                    sa += "• stag [พิม'stag'เพื่อดูวิธี]\n"
                    sa += "• แปรงคท [MID]\n"
                    sa += "• ยูทูป [ข้อความ]\n"
                    sa += "• image [text(ภาษาอังกฤษ)]\n"
                    sa += "• รูป [ข้อความ(ภาษาไทย)]\n"
                    sa += "• เพลสโต [ชื่อแอพ]\n"
                    sa += "• ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                    sa += "• ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                    sa += "• ยก [ใส่จำนวนที่จะยกเลิก]\n"
                    sa += "──────────────\n"
                    sa += "• ดำ ส่งคท.\n"
                    sa += "• ขาว ส่งคท.\n"
                    sa += "• ดำ @user\n"
                    sa += "• ล้าง @user\n"
                    sa += "• เชคดำ\n"
                    sa += "• คทดำ\n"
                    sa += "• ล้างดำ\n"
                    sa += "──────────────\n"
                    sa += "• ตั้งต้อนรับ [ข้อความ]\n"
                    sa += "• ตั้งคนออก [ข้อความ]\n"
                    sa += "• ตั้งแอด [ข้อความ]\n"
                    sa += "• ตั้งแทค [ข้อความ]\n"
                    sa += "• ตั้งคอมเม้น [ข้อความ]\n"
                    sa += "──────────────\n"
                    sa += "• เปิดแทค/ปิดแทค\n"
                    sa += "• เปิดแทค2/ปิดแทค2\n"
                    sa += "• เปิดแทค3/ปิดแทค3\n"
                    sa += "• เปิดไลค์/ปิดไลค์\n"
                    sa += "• เปิดคอมเม้น/ปิดคอมเม้น\n"
                    sa += "• เปิดบล็อค/ปิดบล็อค\n"
                    sa += "• เปิดแอด/ปิดแอด\n"
                    sa += "• เปิดกันรัน/ปิดกันรัน\n"
                    sa += "• เปิดต้อนรับ/ปิดต้อนรับ\n"
                    sa += "• เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                    sa += "• เปิดคนออก/ปิดคนออก\n"
                    sa += "• เปิดยกเลิก/ปิดยกเลิก\n"
                    sa += "• เปิดโค๊ดติ๊ก/ปิดโค๊ดติ๊ก\n"
                    sa += "• เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#00FFFF",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#000000",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#",
                                        "action": {
                                            "type":"uri",
                                            "label":"ผู้สร้าง",
                                            "uri":"line://ti/p/~HACK_BOT"
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "help" or text.lower() == "คำสั่ง":
                            s = "#00FFFF"
                            sa = "•✨ คท\n"
                            sa += "•✨ ไอดีเรา\n"
                            sa += "•✨ ชื่อเรา\n"
                            sa += "•✨ ตัสเรา\n"
                            sa += "•✨ รูปเรา\n"
                            sa += "•✨ รูปวีดีโอเรา\n"
                            sa += "•✨ ปกเรา\n"
                            sa += "•✨ ข้อมูล\n"
                            sa += "•✨ รีบอท\n"
                            sa += "•✨ ออน1\n"
                            sa += "•✨ ออน2\n"
                            sa += "•✨ /ลบรัน\n"
                            sa += "•✨ เชค\n"
                            ss = "•✨ แทค\n"
                            sa += "•✨ ยกเชิญ"
                            ss += "•✨ ก็อป @user\n"
                            ss += "•✨ กลับร่าง\n"
                            ss += "•✨ ตั้งapi [พิมเพื่อดูวิธี]\n"
                            ss += "•✨ ล้างapi [คำที่จะลบ]\n"
                            ss += "•✨ เชคapi\n"
                            ss += "•✨ stag [พิม'stag'เพื่อดูวิธี]\n"
                            ss += "•✨ แปรงคท [MID]\n"
                            ss += "•✨ยูทูป [ข้อความ]\n"
                            ss += "•✨ image [text(ภาษาอังกฤษ)]\n"
                            ss += "•✨ รูป [ข้อความ(ภาษาไทย)]\n"
                            ss += "•✨ เพลสโต [ชื่อแอพ]\n"
                            ss += "•✨ ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                            ss += "•✨ ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                            ss += "•✨ ยก [ใส่จำนวนที่จะยกเลิก]"
                            sd = "•✨ ดำ ส่งคท.\n"
                            sd += "•✨ ขาว ส่งคท.\n"
                            sd += "•✨ ดำ @user\n"
                            sd += "•✨ ล้าง @user\n"
                            sd += "•✨ เชคดำ\n"
                            sd += "•✨ คทดำ\n"
                            sd += "•✨ ล้างดำ\n"
                            sd += "•✨ ตั้งต้อนรับ [ข้อความ]\n"
                            sd += "•✨ ตั้งคนออก [ข้อความ]\n"
                            sd += "•✨ ตั้งแอด [ข้อความ]\n"
                            sd += "•✨ ตั้งแทค [ข้อความ]\n"
                            sd += "•✨ ตั้งคอมเม้น [ข้อความ]\n"
                            sd += "•✨ ตั้งค้างเชิญ [จำนวน]\n"
                            sd += "•✨ ตั้งมุดลิ้ง [ข้อความ]\n"
                            sd += "•✨ ตั้งคนบล็อค [ข้อความ]"
                            se = "•✨ เปิดแทค/ปิดแทค\n"
                            se += "•✨ เปิดแทค2/ปิดแทค2\n"
                            se += "•✨ เปิดแทค3/ปิดแทค3\n"
                            se += "•✨ เปิดไลค์/ปิดไลค์\n"
                            se += "•✨ เปิดคอมเม้น/ปิดคอมเม้น\n"
                            se += "•✨ เปิดบล็อค/ปิดบล็อค\n"
                            se += "•✨ เปิดแอด/ปิดแอด\n"
                            se += "•✨ เปิดกันรัน/ปิดกันรัน\n"
                            se += "•✨ เปิดต้อนรับ/ปิดต้อนรับ\n"
                            se += "•✨ เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                            se += "•✨ เปิดคนออก/ปิดคนออก\n"
                            se += "•✨ เปิดยกเลิก/ปิดยกเลิก\n"
                            se += "•✨ เปิดติ๊กคนเข้า/ปิดติ๊กคนเข้า\n"
                            se += "•✨ เปิดติ๊กคนออก/ปิดติ๊กคนออก\n"
                            se += "•✨ เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                            sti = "•✨ เปิดมุดลิ้ง/ปิดมุดลิ้ง\n"
                            sti += "•✨ ตั้งติ๊กคนแอด\n"
                            sti += "•✨ ลบติ๊กคนแอด\n"
                       #     sti += "• ตั้งติ๊กแทคแชท\n"
                       #     sti += "• ลบติ๊กแทคแชท\n"
                            sti += "•✨ ตั้งติ๊กคนแทค\n"
                            sti += "•✨ ลบติ๊กคนแทค\n"
                            sti += "•✨ ตั้งติ๊กคนเข้า\n"
                            sti += "•✨ ลบติ๊กคนเข้า\n"
                            sti += "•✨ ตั้งติ๊กคนออก\n"
                            sti += "•✨ ลบติ๊กคนออก\n"
                            sti += "•✨ เขียน1 [ข้อความ]\n"
                            sti += "•✨ ไอดีไลน์ [idline]\n"
                            sti += "•✨ ดึง @user\n"
                            sti += "•✨ บล็อค @user\n"
                            sti += "•✨ เพิ่มเพื่อน @user\n"
                            sti += "•✨ ลบเพื่อน @user\n"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                               "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งส่วนตัว •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#00FFFF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"HACK_BOT",
                                                     "uri":"line://ti/p/~HACK_BOT"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งพิเศษ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#00FFFF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"HACK_BOT",
                                                     "uri":"line://ti/p/~HACK_BOT"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งเปิด/ปิด •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#00FFFF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"HACK_BOT",
                                                     "uri":"line://ti/p/~HACK_BOT"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งตั้งค่า/ติดดำ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#00FFFF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"HACK_BOT",
                                                     "uri":"line://ti/p/~HACK_BOT"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งทั่วไป •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#00FFFF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"HACK_BOT",
                                                     "uri":"line://ti/p/~HACK_BOT"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = maxgie.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = maxgie.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");maxgie.sendContact(to, str(BackupProfile.mid));maxgie.sendContact(to, str(contact.mid))
                                    
                elif msg.text.lower().startswith("ส่งคลิป "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = duc1.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                duc1.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💖.น้.อ.ง.น้.อ.ง.อ.ย่.า.บ.อ.ก.ใ.ค.ร.น.ะ.อ่.ะ.หิ.หิ.หิ.💗.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.⭐.H.A.C.K.B.O.T.1.0.V.E.💗.N.e.w.2.0.1.9.💗")
                                duc1.sendMessage(receiver, "🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n🌀•คลิปหลุดนักศึกษาเสียวสุดๆ•🌀\n💗.ค.ลิ.ป.ห.ลุ.ด.เ.สี.ย.ว.สุ.ด.ๆ.เ.ล.ย.💟.เ .ฉ.พ.า.ะ.ไ.ล.น์.สี.&ไ.ล.น์.ค.ลั.บ.ค่.ะ.~.💚.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S4.4.4.4.4.4ไ.ว.รั.ส.ฟ.รุ้.ง.มุ้.ง.มิ้.ง.b.y.เ.อ.จั.ง.~.☆.😁.🤗.💚")
                                duc1.sendMessage(to, "🌀ดูคลิปเด็ดในแชท สต.น่ะคับ🌀".format(str(jml)))
                                
                elif text.lower() == "กลับร่าง":
                            try:
                                maxgiestatus = maxgie.getProfile()
                                maxgieName = maxgie.getProfile()
                                maxgieName.statusMessage = ProfileMe["statusMessage"]
                                maxgieName.pictureStatus = str(ProfileMe["pictureStatus"])
                                maxgie.updateProfile(maxgiestatus)
                                maxgieName.displayName = ProfileMe["NameMe"]
                                maxgie.updateProfile(maxgieName)
                                path = maxgie.downloadFileURL(ProfileMe["PictureMe"])
                                maxgie.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                maxgie.updateProfileCoverById(coverId)
                                BackupProfile = maxgie.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ กลับบัญชีเดิมเรียบร้อย", ">_<");maxgie.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟คุณยังไม่ได้ก๊อปปี้🌟")
                elif msg.text.lower().startswith("."):
                    text = msg.text.lower().replace("."," ")
                    maxgie.unsendMessage(msg_id)                                       
                    duc1(msg.to,text)
                if text.lower() == "คท":
                    maxgie.generateReplyMessage(msg.id) 
                    maxgie.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': maxgieMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "ไอดีเรา":
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to,maxgieMID)
                elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ชื่อของคุณ 」\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ตัสของคุณ 」\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                            h = maxgie.getContact(maxgieMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                            h = maxgie.getContact(maxgieMID)
                            if h.videoProfile == None:
                            	return maxgie.sendMessage(to, "คุณไม่ได้ใส่รูปวีดีโอ >_<")
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                            h = maxgie.getContact(maxgieMID)
                            cu = maxgie.getProfileCoverURL(maxgieMID)
                            image = str(cu)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif msg.text in ["ดึง"]:
                        apalo["winvite"] = True
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "🌟ส่งคทที่จะดึงลงมา..🌟")                        
                            
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "อัพดิส":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งรูปที่จะอัพลงมาครับ..🌟")
                elif text.lower() == 'เปิดออก':
                    did["join"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ออกแชทรวมอัตโนมัติ (เปิด) ใช้งาน🌟")
                elif text.lower() == 'ปิดออก':
                    did["join"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ออกแชทรวมอัตโนมัติ (ปิด) ใช้งาน🌟") 
                if text.lower() == "ออน1":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage     
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    eltime = time.time() - mulai
                    van = ggggg(eltime)
                    van2 = "\n\n✨วันที่ :"+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n───────────\n◐เวลา:"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n\n"      
                    data={
"type":"flex",
"altText":"Weclome",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "✨ ออน ✨",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00FFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"contents": [
{
"text": "✨ระยะเวลาของบอท✨",
"size": "md",
"align": "center",
"color": "#00FFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00FFFF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : \n ➡ HACK_BOT",
"size": "xs",
"margin": "none",
"color": "#00FFFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00FFFF",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อเชล",
"uri": "https://line.me/ti/p/~HACK_BOT",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00FFFF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อผู้สร้าง",
"uri": "https://line.me/ti/p/~HACK_BOT",
}
}
]
}
},
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "✨ ปฏิทิน ✨",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00FFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"contents": [
{
"text": "✨วันเดือนปีและเวลา✨",
"size": "md",
"align": "center",
"color": "#00FFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00FFFF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van2,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00FFFF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : \n ➡ HACK_BOT",
"size": "xs",
"margin": "none",
"color": "#00FFFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00FFFF",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อเชล",
"uri": "https://line.me/ti/p/~HACK_BOT",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00FFFF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อผู้สร้าง",
"uri": "https://line.me/ti/p/~HACK_BOT",
}
}
]
}
}
]
}
}                    
                    sendTemplate(to, data)   
                if text.lower() == "ออน2" or text.lower() == "runtime":
                    contact = maxgie.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)   
                    a = "วันที่"+ datetime.strftime(timeNow,'%d-%m-%Y')+"🇹🇭เวลา"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#000000"
                              },
                              "footer": {
                                "backgroundColor": "#000000"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#00FFFF"
                                    },
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00FFFF"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "✨ระยะเวลาทำงาน✨",
                                      "size": "lg",
                                      "align": "center",
                                      "color": "#00FFFF",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00FFFF"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "{}".format(run),
                                          "size": "lg",
                                          "align": "center",
                                          "margin": "none",
                                          "color": "#00FFFF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "HACK_BOT",
                                          "size": "xl",
                                          "action": {
                                            "uri": "line://ti/p/~HACK_BOT",
                                            "type": "uri",
                                            "label": "Add Maker"
                                          },
                                          "margin": "xl",
                                          "align": "center",
                                          "color": "#00FFFF",
                                          "weight": "bold",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "horizontal"
                                }
                              ],
                              "type": "box",
                              "layout": "vertical"
                            }
                        }
                    }
                    sendTemplate(to, data)      
                if text.lower() == "me":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#000000","action":{"type":"uri","label":"HACK_BOT","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/63/c4/12/63c412c55c99b6e0742bebaf53dd40d6.jpg"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "เรา2":
                            s = temp["te"]
                            a = temp["t"]
                            contact = maxgie.getContact(maxgieMID)
                            cover = maxgie.getProfileCoverURL(maxgieMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": " รูปโปรไฟล์ ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "HACK_BOT",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~HACK_BOT"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "รูปปกพื้นหลัง ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "HACK_BOT",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~HACK_BOT"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ชื่อของคุณ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "สเตตัสของคุณ ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "HACK_BOT",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~HACK_BOT"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                if text.lower() == "เรา":
                    contact = maxgie.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "HACK_BOT","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#333333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://img.live/images/2019/02/10/1549778907829.jpg"},"type":"text","text":"HACK_BOT","align":"center","weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://ti/p/~HACK_BOT"},"type":"text","text":"ผู้สร้าง","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#CCFFFF"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF3333"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/02/21/c5f4e567380d0f1e31acb822d0b5cfd2819c8e3b_00.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/21/d1566d9832bd42f14ec4d2538f74ab76.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF3333"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF3333"},{"type":"box","contents":[{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"md","wrap":True,"type":"text","text":" HACK_BOT","weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#FF3333"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})            
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "เวลาออน \n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=uca43cd15fb994f5e04c0984b7c1693ef"
                        } 
                    }
                    sendTemplate(to, data)                            
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออน ⇦\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "ออน" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออน ⇦\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                              #  {
                                              #  "type": "image",
                                                #"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                               # "size": "full"
                                             #  },
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#000000",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "รีบอท" or text.lower() == "reset":
                    gifnya = ["https://i.pinimg.com/originals/2e/d7/37/2ed737ba301b048afdb355fd9d1c2e86.gif"]
                    data = {
                        "type": "template",
                        "altText": "กำลังรีบอท...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~HACK_BOT"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "กรุณาล็อคอินใหม่ด้วยครับ (•ω•)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "ข้อความจากคุณนนท์",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ua053fcd4c52917706ae60c811e39d3ea"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                elif text.lower() == "Sp" or text.lower() == "สปีด":                   
                    contact = maxgie.getContact(sender)
                    start = time.time()
                    maxgie.sendMessage(to, "😏ทดสอบความเร็ว😏")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "🇹🇭ความเร็วเซิร์ฟเวอร์ : PornHubThailand\n🇹🇭ความเร็วเชื่อต่อ : ดีมาก\n🇹🇭ความเร็ว : %.2f วินาที\n🇹🇭ความเร็วสปีด : %.10f วินาที" % (took,elapsed_time)
                    LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                    LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                    data = {
                        "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#000000'
                                            },
                                            "footer": {
                                                "backgroundColor": '#00FFFF'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text":  "{}".format(a),
                                                                "color": "#00FFFF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "HACK_BOT",
                                                    "uri": "line://ti/p/~HACK_BOT"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0        
                                    }
                                }
                            }
                    sendTemplate(to, data)
                elif "คอล " in msg.text.lower():
                   if msg.toType == 2:
                      sep = msg.text.split(" ")
                      resp = msg.text.replace(sep[0] + " ","")
                      num = int(resp)
                      try:
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟กำลังดำเนินการ...🌟") 
                      except:
                         pass
                      for var in range(num):
                            group = maxgie.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            maxgie.acquireGroupCallRoute(msg.to)
                            maxgie.inviteIntoGroupCall(msg.to, contactIds=members)
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟เชิญคอลสำเร็จ🌟")

                elif msg.text.startswith("โทร "):
                    dan = text.split(" ")
                    num = int(dan[1])
                    ret_ = "╭──[ เชิญโทรสำเร็จ ]"
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            for var in range(0,num):
                                group = maxgie.getGroup(to)
                                members = [ls]
                                maxgie.acquireGroupCallRoute(to)
                                maxgie.inviteIntoGroupCall(to, contactIds=members)
                            ret_ += "\n├> @!"
                        ret_ += "\n╰──────────"
                        maxgie.sendPhu(to, ret_, lists)   
                                        
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               maxgie.sendMessage(msg.to, teks)
                        else:
                           maxgie.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            maxgie.sendMessage(msg.to, tulisan)
                elif text.lower() == 'ข้อมูล' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "ubd86e8c77559b1493f0ad64b1dba2d6c"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ เวลาออนบอท :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ ผู้สร้าง : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 HACK_BOT 」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "linkUrl": "line://ti/p/~HACK_BOT"
                            }
                        }
                        sendTemplate(to, data)
                        maxgie.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif text.lower() == "หลุดมือ":
                            gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "รัก" or text.lower() == "รักๆ":
                            gifnya = ['https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "ยิงๆ" or text.lower() == "ยิง":
                            gifnya = ['https://i.pinimg.com/originals/25/bf/35/25bf35850f22b00ff04505f173e16ec8.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "คิมูจิ":
                            gifnya = ['https://sv1.picz.in.th/images/2020/01/04/RzLWT8.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    maxgie.sendAudio(msg.to,"hasil.mp3")
                    
#=================NEW!! โมทกิฟ สติกเกอร์ 21/11/62 ================                         
                elif text.lower() == "เค้างง":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmeZR.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าสั่น":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmsQW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เค้าดีใจ","เย้ๆ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vmms0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าเขิล":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/02/chivaree3.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in "เค้าอาย":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VmI9Z.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าโอเค":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/02/chivaree78.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าไม่เถียง":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vvzdu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["เค้าเผ่น","เค้าวิ่งๆ","เผ่นสิ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/12/9Hj89n.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าเครียด":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4Vjl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เค้าหิว"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9VvMFQ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "เค้าพร้อม":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://img.live/images/2019/01/03/a011.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เค้าชอบ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4Wxu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["อาบน้ำ","เค้าอาบน้ำ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9Vvoyb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)         
                elif text.lower() == "เค้าจะเอา":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/01/13/9X4dnZ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "จัดไป":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGn2t.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif text.lower() == "โยก":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGHTl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["ว้าว","ว้าวว"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSGItW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                     
                elif msg.text in ["ขอบคุณ","ขอบคุน"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJt50.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                      
                elif msg.text in ["เห้อ","เห้ออ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJsJ2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เศร้า","เบื่อ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJvLz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["โอเค","โอเคร"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSJIuI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["กัปตัน","แคป"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSewZI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)   
                elif msg.text in ["วานด้า","วันด้า"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSe1sP.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["แนท","นาตาชา"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSec9e.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["ฟรุ้งฟริ้ง","มุ้งมิ้ง"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSeQUE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["ยิง","เหอะ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSebyn.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["บาย","ไปละ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSesUy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["หึหึ","ธานอส"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSeGH0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)             
                elif msg.text in ["เย่","ธอร์"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmgIb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เบิดเดย์","วันเกิด"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmqhz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                    
                elif msg.text in ["ชอบ","ถูกใจ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSm6Vv.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["น่ารัก","น่ารักก"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSmrYE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["รัก","รักนะ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSyqPS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["เหรอ","ใช่เหรอ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSybbW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["ร้อน","ร้อนน"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSyja2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["จุฟ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFHtS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                  
                elif msg.text in ["สวัสดี","หวัดดี"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFvq2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["โหล","ฮาโหล"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSFMof.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["ฝันดี","ฝรรดี"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSI4i0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                 
                elif msg.text in ["เผ่น","เผ่นๆ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSIZiE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif msg.text in ["เพลีย","เพลียย"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMjae.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["เร็ว","ไวๆ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMo4l.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)               
                elif msg.text in ["ล้อเล่นๆ","ล้อเล่นๆๆ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/11/ZSMDQk.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                     
                elif msg.text in ["พิม่อน"]:
                   chivaree1={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{
                     "type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9G3G9.gif","size":"xxxl","aspectRatio":"1:2","action":{
                             "type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   chivaree2={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9GK7a.gif",
                                       "size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}   
                   chivaree3={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/Z9GgF8.gif",
                                       "size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1560169633-yaJ7kAZB?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}     
                   sendTemplate(to, chivaree1)
                   sendTemplate(to, chivaree2)
                   sendTemplate(to, chivaree3)           
                elif msg.text in ["เหอะๆ","ต่าย"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/17/ZThcTy.png","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["ยิง2","ยิง!"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg0Nxf.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                
                elif msg.text in ["มา","มานี่"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg0t30.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif msg.text in ["อ้อน","อ้อนๆ"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/Zg01aZ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)              
                elif msg.text in ["สติช","สแตช"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSBwz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)           
                elif msg.text in ["สติช2","สแตช2"]:
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSORS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)                   
                elif text.lower() == "สติช3":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSo1W.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)               
                elif text.lower() == "ทีมบิน":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/08/21/ZgSAL1.png","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                   
#=========NEW สติกเกอร์ gif ==================================================
                elif text.lower() == "โยกๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/ge8zUJ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "จัดไป":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geVh38.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "รับแซ่บ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geVwnI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "แล้วไงใครแคร์":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geVoyW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "โยกเอวๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geVpj8.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "จุฟๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geXtG1.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "แปะๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geXDgI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "goodnight":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geXuJk.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                   
#=========NEW สติกเกอร์ gif ==================================================
                elif text.lower() == "สวัสดีเจ้าค่ะ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gevRCQ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบ555":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geGduV.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ต๊ะเอ๋":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geG3RD.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "okเจ้าค่ะ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geGuWV.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ปรบมือรัวๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geGH3g.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบlike":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geGmPb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "รักนะเจ้าคะ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geJe8v.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบจุ๊บๆ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geLDiE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบ...":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gem5Ul.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ว้ายตาเถร":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gemsvn.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบยิ้มอ่อน":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gey0lI.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ดีงามเจ้าค่ะ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geyRCy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ทำกระไรอยู่รึ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geynhP.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบงอล":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geFxze.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบโกรธ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geFl3Q.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบมีความสุข":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/geIuqt.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบเบ้ปาก":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmW9nW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบยินดี":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmWsQt.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบ...2":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmWH9N.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "สู้ๆน้า":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmWGrg.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบขอบคุณ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmdz0q.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบขอโทษ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmdgyv.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "น้องสไบส่งเข้านอน":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/22/gmdl22.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                   
#=========NEW สติกเกอร์ gif ==================================================     
                elif text.lower() == "พร้อม":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmksU1.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=??🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "วอท":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3S8v.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "อะเคร":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3htS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "สวยพี่สวย":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3TfW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "คนไม่รักดี":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3gFJ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ไม่เผือก":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm355z.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "มีพิรุธ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3ji0.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เวรี่กู๊ด":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3lCu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "ย่อ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3awQ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "มาลองไร่":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3vJn.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "คุณพระ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm3Fiy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "ขอบคุณ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm90Db.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "มันบาปนะ":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm9BY8.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "ของมันต้องมี":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm9U1V.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ปัญญา":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm95eS.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ป๊าด":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm92K9.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "อะเฮือก":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm9n3f.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "ลูกเป็นคนดี":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gm9rOa.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "เผ็ด":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmTBbn.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เกมได้ไง":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmTkNW.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "เอ็นดู":
                   data={"type":"template","altText":"🇹🇭🇹?? สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmT3Q2.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "ต้องรู้ไหม":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmTwZD.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "หัวก็โกน":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmTipa.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data) 
                elif text.lower() == "บัตรจีบ48":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/11/23/gmTOsu.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                   
#=========NEW สติกเกอร์ gif ==================================================
                elif text.lower() == "j1":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSzbN.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j2":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSiQb.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j3":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSUZq.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j4":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSO9R.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j5":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSCsl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j6":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSa8S.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j7":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSv0n.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j8":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSGcg.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j9":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSyjy.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j10":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMSMB9.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j11":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYSca.gif","size":"xxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j12":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYzFz.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j13":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYBlR.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j14":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYt7P.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j15":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYKFl.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j16":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYiGE.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j17":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYQqV.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j18":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYUHQ.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j19":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYOCg.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j20":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYoo1.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j21":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭??🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYPfD.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j22":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYv5u.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j23":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMYeiP.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                elif text.lower() == "j24":
                   data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"https://sv1.picz.in.th/images/2019/12/28/iMzR1q.gif","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   sendTemplate(to, data)
                #elif text.lower() == " ":
                   #data={"type":"template","altText":"🇹🇭🇹🇭 สติกเกอร์ By COLA 🇹🇭🇹🇭","template":{"type":"image_carousel","columns":[{"imageUrl":"##","size":"xxxl","aspectRatio":"1:2","action":{"type":"uri","uri": "line://app/1602687308-GXq4Vvk9?type=text&text=🌟🌟•NEVERDIE•🌟🌟",}}]}}
                   #sendTemplate(to, data)
                   
                   
                   
                elif cmd == "random":
                            gifnya = ['https://thumbs.gfycat.com/AngelicCloudyJaeger-size_restricted.gif','https://thumbs.gfycat.com/AgedZealousBlackfootedferret-size_restricted.gif','https://thumbs.gfycat.com/FondHastyChinesecrocodilelizard-size_restricted.gif','https://thumbs.gfycat.com/LividCrazyDipper-size_restricted.gif','https://thumbs.gfycat.com/LoathsomeDevotedGossamerwingedbutterfly-size_restricted.gif','https://thumbs.gfycat.com/SamePhysicalHarrierhawk-size_restricted.gif','https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif','https://thumbs.gfycat.com/ThoseBitesizedBrahmanbull-size_restricted.gif','https://thumbs.gfycat.com/FakeSlowBengaltiger-size_restricted.gif','https://thumbs.gfycat.com/TanSpitefulChupacabra-size_restricted.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
#----------------------------------------------------------------------------#                         
                if  text.lower().startswith("ตั้งรูปโปรไฟล์ "):
                    keyword = msg.text.replace(msg.text.split(" ")[0] + " ", "")
                    pic = "http://dl.profile.line-cdn.net/{}".format(maxgie.profile.pictureStatus)
                    a = subprocess.getoutput('youtube-dl --format mp4 --output tmp.mp4 {}'.format(keyword))
                    pict = maxgie.downloadFileURL(pic)
                    vids = "tmp.mp4"
                    changeVideoAndPictureProfile(pict, vids)
                    os.remove("tmp.mp4")
                    duc1(to, "เปลี่ยน รูป เป็น คลิป YouTube เรียบร้อย")
#=====================================================================

#=====================================================================
                elif msg.text.lower().startswith("/คท "):
                   if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = maxgie.getContact(ls)
                            mi_d = contact.mid
                            maxgie.sendContact(msg.to, mi_d)
                            
                elif text.lower() == "เทส":
                    duc1(to, "█▒... 10.0%")
                    duc1(to, "██▒... 20.0%")
                    duc1(to, "███▒... 30.0%")
                    duc1(to, "████▒... 40.0%")
                    duc1(to, "█████▒... 50.0%")
                    duc1(to, "██████▒... 60.0%")
                    duc1(to, "███████▒... 70.0%")
                    duc1(to, "████████▒... 80.0%")
                    duc1(to, "█████████▒... 90.0%")
                    duc1(to, "██████████▒... 100.0%")
                    duc1(to,"นนท์ยังอยู่!!")
#=========NEW สติกเกอร์ กิฟ 22/11/62===========
                elif text.lower() == "สติกเกอร์ทั้งหมด":
                    duc1(to, "เมนูสติกเกอร์ทั้งหมด")
                    duc1(to, "1. สติ๊กเกอร์ - HyperRabbit")
                    duc1(to, "2. สติ๊กเกอร์ - น้องสไบดุ๊กดิ๊ก")
                    duc1(to, "3. สติ๊กเกอร์ - ดึ๊บ ดึ๊บ")
                    duc1(to, "4. สติกเกอร์ - Cinderella Girls")
                    duc1(to, "- เทส5")
                    duc1(to, "- เทส6")
#==================================================                    
                elif text. lower() == "ติก1":
                    duc1(to, "รายชื่อสติกเกอร์ในชุด")
                    duc1(to, "โยกๆ")
                    duc1(to, "จัดไป")
                    duc1(to, "รับแซ่บ")
                    duc1(to, "แล้วไงใครแคร์")
                    duc1(to, "โยกเอวๆ")
                    duc1(to, "จุฟๆ")
                    duc1(to, "แปะๆ")
                    duc1(to, "goodnight")
                    
                elif text. lower() == "ติก2":
                    duc1(to, "สวัสดีเจ้าค่ะ")
                    duc1(to, "น้องสไบ555")
                    duc1(to, "ต๊ะเอ๋")
                    duc1(to, "okเจ้าค่ะ")
                    duc1(to, "ปรบมือรัวๆ")
                    duc1(to, "น้องสไบlike")
                    duc1(to, "รักนะเจ้าคะ")
                    duc1(to, "น้องสไบจุ๊บๆ")
                    duc1(to, "น้องสไบ...")
                    duc1(to, "ว้ายตาเถร")
                    duc1(to, "น้องสไบยิ้มอ่อน")
                    duc1(to, "ดีงามเจ้าค่ะ")
                    duc1(to, "ทำกระไรอยู่รึ")
                    duc1(to, "น้องสไบงอล")
                    duc1(to, "น้องสไบโกรธ")
                    duc1(to, "น้องสไบมีความสุข")
                    duc1(to, "น้องสไบเบ้ปาก")
                    duc1(to, "น้องสไบยินดี")
                    duc1(to, "น้องสไบ...2")
                    duc1(to, "สู้ๆน้า")
                    duc1(to, "น้องสไบขอบคุณ")
                    duc1(to, "น้องสไบขอโทษ")
                    duc1(to, "น้องสไบส่งเข้านอน")
                    
                elif text. lower() == "ติก3":
                    duc1(to, "พร้อม")
                    duc1(to, "วอท")
                    duc1(to, "อะเคร")
                    duc1(to, "สวยพี่สวย")
                    duc1(to, "คนไม่รักดี")
                    duc1(to, "ไม่เผือก")
                    duc1(to, "มีพิรุธ")
                    duc1(to, "เวรี่กู๊ด")
                    duc1(to, "ย่อ")
                    duc1(to, "มาลองไร่")
                    duc1(to, "คุณพระ")
                    duc1(to, "ขอบคุณ")
                    duc1(to, "มันบาปนะ")
                    duc1(to, "ของมันต้องมี")
                    duc1(to, "ปัญญา")
                    duc1(to, "ป๊าด")
                    duc1(to, "อะเฮือก")
                    duc1(to, "ลูกเป็นคนดี")
                    duc1(to, "เผ็ด")
                    duc1(to, "เกมได้ไง")
                    duc1(to, "เอ็นดู")
                    duc1(to, "ต้องรู้มั้ย")
                    duc1(to, "หัวก็โกน")
                    duc1(to, "บัตรจีบ48")
                    
                elif text. lower() == "ติก4":
                    duc1(to, "j1")
                    duc1(to, "j2")
                    duc1(to, "j3")
                    duc1(to, "j4")
                    duc1(to, "j5")
                    duc1(to, "j6")
                    duc1(to, "j7")
                    duc1(to, "j8")
                    duc1(to, "j9")
                    duc1(to, "j10")
                    duc1(to, "j11")
                    duc1(to, "j12")
                    duc1(to, "j13")
                    duc1(to, "j14")
                    duc1(to, "j15")
                    duc1(to, "j16")
                    duc1(to, "j17")
                    duc1(to, "j18")
                    duc1(to, "j19")
                    duc1(to, "j20")
                    duc1(to, "j21")
                    duc1(to, "j22")
                    duc1(to, "j23")
                    duc1(to, "j24")
                
                
                
                #elif text. lower() == " ":
                	#duc1(to, " ")

                elif msg.text in ["นับ"]:
                    duc1(to,"「 HACK_BOT 」")
                    duc1(to,"💝:::⭐ 1 ⭐:::💝")
                    duc1(to,"💝:::⭐ 5 ⭐:::💝")
                    duc1(to,"💝:::⭐ 10 ⭐:::💝")
                    duc1(to,"กูนับเส็จละไวมั้ย" +datetime.today().strftime('%H:%M:%S')+ "👈เวลาปัจจุบัน") 
#=====================================================================
                elif msg.text.lower().startswith("ประกาศแชท: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = maxgie.friends
                    for friend in friends:
                        maxgie.sendMessage(friend, "「ข้อความอัตโนมัติ ประกาศแชท」\n{}".format(str(txt)))
                    duc1(to, "ส่งข้อความถึงเพื่อน {} คน".format(str(len(friends))))
#=============================================================================           
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        maxgie.sendMessage(to, 'Add to TalkBan')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ล้าง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        maxgie.sendMessage(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                elif text.lower() == "เชคดำ":
                            if apalo["Talkblacklist"] == {}:
                              maxgie.unsendMessage(msg_id)
                              duc1(to, "🌟ไม่พบคนที่ยัดดำ🌟")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +maxgie.getContact(m_id).displayName + "\n"
                              duc1(to,"รายชื่อคนติดดำ :\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "เปิดแล้ว (｀・ω・´)"
                  else:
                      sa = "เปิดอยู่แล้ว (｀・ω・´)"
                  duc1(to, sa)
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      duc1(to,"ปิดแล้ว (｀・ω・´)")
                  else:
                      duc1(to,"ปิดอยู่แล้ว (｀・ω・´)")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    sa = "เปิดแล้วว >_<"
                    duc1(to,str(sa))
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    sa = "ปิดแล้ว >_<"
                    duc1(to,str(sa))
                if text.lower() == "เปิดกันรัน":
                    settings["autoCancel"]["on"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดกันรันเรียบร้อย🌟")
                if text.lower() == "ปิดกันรัน":
                    settings["autoCancel"]["on"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดกันรันเรียบร้อย🌟")
                if text.lower() == "กินห้องเปิด":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟กินห้อง (เปิด) ใช้งาน🌟")
                  else:
                      maxgie.sendMessage(msg.to,"「 Status Autoleave 」\nเปิดใช้งานกินห้องอัตโนมัติแล้ว")
                if text.lower() == "กินห้องปิด":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = False
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟กินห้อง (ปิด) ใช้งาน🌟")
                  else:
                      maxgie.sendMessage(msg.to,"「 Status Autoleave 」\nเปิดใช้งานกินห้องอัตโนมัติแล้ว") 
                if text.lower() == "เปิดแอด":
                    settings["autoAdd"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแอดเรียบร้อย🌟")
                if text.lower() == "ปิดแอด":
                    settings["autoAdd"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแอดเรียบร้อย🌟")
                if text.lower() == "ปิดไลค์":
                   sets["l"] = False
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "🌟ปิดไลค์แล้ว🌟")
                if text.lower() == "เปิดไลค์":
                   sets["l"] = True
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "🌟เปิดไลค์แล้ว🌟")
                if text.lower() == "เปิดแทค2":
                    tagadd["tagss"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแทค2เรียบร้อย🌟")
                if text.lower() == "ปิดแทค2":
                    tagadd["tagss"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแทค2เรียบร้อย🌟")
                if text.lower() == "เปิดคอมเม้น":
                    settings["com"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดคอมเม้นเรียบร้อย🌟")
                if text.lower() == "ปิดคอมเม้น":
                    settings["com"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดคอมเม้นเรียบร้อย🌟")
                if text.lower() == "เปิดต้อนรับ":
                    settings["Welcome"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดต้อนรับเรียบร้อย🌟")
                if text.lower() == "ปิดต้อนรับ":
                    settings["Welcome"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดต้อนรับเรียบร้อย🌟")
                if text.lower() == "เปิดต้อนรับ2":
                    settings["Wc"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดต้อนรับ2เรียบร้อย🌟")
                if text.lower() == "ปิดต้อนรับ2":
                    settings["Wc"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดต้อนรับ2เรียบร้อย🌟")
                if text.lower() == "เปิดคนออก":
                    settings["Leave"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดคนออกเรียบร้อย🌟")
                if text.lower() == "ปิดคนออก":
                    settings["Leave"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดคนออกเรียบร้อย🌟")
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดยกเลิกเรียบร้อย🌟")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดยกเลิกเรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กใหญ่":
                    settings["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กใหญ่เรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กใหญ่":
                    settings["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กใหญ่เรียบร้อย🌟")
                if text.lower() == "เปิดโค๊ดติ๊ก":
                    sets["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดโค๊ดติ๊กเรียบร้อย🌟")
                if text.lower() == "ปิดโค๊ดติ๊ก":
                    sets["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดโค๊ดติ๊กเรียบร้อย🌟")
                if text.lower() == "เปิดแทค3":
                    sets["tagsticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแทค3เรียบร้อย🌟")
                if text.lower() == "ปิดแทค3":
                    sets["tagsticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแทค3เรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กคนออก":
                    settings["lv"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กคนออกเรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กคนออก":
                    settings["lv"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กคนออกเรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กคนเข้า":
                    settings["wcsti2"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กคนเข้าเรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กคนเข้า":
                    settings["wcsti2"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กคนเข้าเรียบร้อย🌟")
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดมุดลิ้งเรียบร้อย🌟")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดมุดลิ้งเรียบร้อย🌟")

                elif text.lower() == 'speed':start = time.time();maxgie.sendMessage("u21d04f683a70ee8776c4c58a0358c204", "เช็คความเร็วแสง!!");elapsed_time = time.time() - start;duc1(to, "Speed : %s second"%str(round(elapsed_time,4)))
                
                elif msg.text.lower().startswith("ประกาศ "):
                            delcmd = msg.text.split(" ")
                            get = msg.text.replace(delcmd[0]+" ","").split("/")
                            kw = get[0]
                            ans = get[1]
                            groups = maxgie.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = " ประกาศ \n\n{}".format(str(kw))
                                data = {
"type":"flex",
"altText":"แจกฟรี!!",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "🌟 ประกาศกลุ่ม 🌟",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00FFFF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
},
{
"type": "separator",
"color": "#000000"
},
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
},
{
"contents": [
{
"text": sa,
"size": "md",
"align": "center",
"color": "#00FFFF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#000000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": sa,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#000000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : Bot-Lnw-Non ",
"size": "xs",
"margin": "none",
"color": "#00FFFF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#000000",
"height": "sm",
"action": {
"type": "uri",
"label": "• กดที่นี่ •",
"uri": "https://line.me/ti/p/~{}".format(ans),
}
},
]
}
}
]
}
}
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#                
                elif msg.text.lower().startswith("ขายของ1"):
                           contact = maxgie.getContact(sender) 
                           groups = maxgie.getGroupIdsJoined()
                           for group in groups:
                               dataProfile = [ 
                                     {
                                     "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★ID HACK_BOT ★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/01/20190624_131500.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "กลุ่ม VIP ไลฟ์สด",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": " ราคา 150 บาท 1 เดือน ",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 300 บาท/ตลอดชีพ ",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไลฟ์เริ่ม 21.00น - 00.00น",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สมัคร 300 (ฟรีกลุ่มคลิป)",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ กดที่ปุ่มนี่",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★ID HACK_BOT ★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/01/20190624_131151.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "กลุ่ม VIP ไลฟ์สด",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 150 บาท 1 เดือน",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 300 บาท/ตลอดชีพ",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไลฟ์เริ่ม 21.00น - 00.00น",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สมัคร 300 (ฟรีกลุ่มคลิป)",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ กดที่ปุ่มนี่",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★ID HACK_BOT ★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/01/20190624_131231.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/01/G-olden-c-Rown.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "กลุ่ม VIP ไลฟ์สด",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 150 บาท 1 เดือน",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 300 บาท ตลอดชีพ",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไลฟ์เริ่ม 21.00น - 00.00น",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "สมัคร 300 (ฟรีกลุ่มคลิป)",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": " สนใจติดต่อ กดที่ปุ่มนี่ ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                               ]
                               data = {
                                   "type": "flex",
                                   "altText": "มีข้อความถึงคุณ",
                                   "contents": {
                                       "type": "carousel",
                                       "contents": dataProfile
                                   }
                               }
                               sendTemplate(group, data)
                               time.sleep(1)
                           maxgie.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif msg.text.lower().startswith("ขายของ2"):
                            contact = maxgie.getContact(sender) 
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★LINE ID HACK_BOT★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/F6FBB34A-3B96-41A7-944D-E17454BC6F25.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451636487.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "self bot python3",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100 บาท/เดือน",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ห้องบอท",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 200 บาท",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการใช้งาน",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★LINE ID HACK_BOT★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/D88BDCD7-3CFC-4BD9-BE86-210B7A22CD3C.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451634501.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ติ๊กเกอร์ ราคาถูก",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "เหรียญเหมาเหรียญแท้ๆ",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ติ๊กโปรทุกวัน",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคาถูกสอบถามได้",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "พ่อค้าแม่ค้าใจดี",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★LINE ID HACK_BOT★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/2832_20180721151831.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://i.dlpng.com/static/png/75778_thumb.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ขายสคิป/เฟค/คิก/ธรรมดา",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไฟลบอทล็อคอิน",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ปล่อยเช่าเชิฟเวอร์",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคาสบายๆกระเป๋า",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการใช้งาน",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "มีของมาขาย",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#                            
                elif msg.text.lower().startswith("ขายของ3"):
                            contact = maxgie.getContact(sender) 
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★พื้นที่สำรับโฆษณา★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★ฟื้นที่สำรับโฆษณา★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#00FFFF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "..★ฟื้นที่สำรับโฆษณา★..",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FFFF"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~HACK_BOT"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/07/12/20190712_170109.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ฟื้นที่สำรับโฆษณา",
                                                  "color": "#00FFFF",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://ti/p/~HACK_BOT",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "รับประกาศโฆษณา Flex",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            maxgie.sendMessage(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "แทค":
                        group = maxgie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(maxgie.getProfile().mid)
                        maxgie.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == "/แทค" or text.lower() == "tagall":
                    if msg._from in maxgieMID:
                        group = maxgie.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya ="http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya +"&chts=ff3333,70&chf=bg,s,ff3333"
                    maxgie.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("เขียน1 "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ", "")
                    text = "{}".format(textnya)
                    contact = maxgie.getContact(maxgieMID)
                    data = {
                        "type": "flex",
                        "altText": "มาอ่าน",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#00FFFF'
                                    },
                                 },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "aspectRatio":"1:1",
                                "aspectMode":"cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(text),
                                        "color":"#000000",
                                        "wrap": True,
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       maxgie.findAndAddContactsByMid(ls)
                                       maxgie.inviteIntoGroup(to, [ls])
                                    except:
                                       duc1(to, "Limited !")
                elif msg.text.lower().startswith("สะกด"):
                  if msg.toType == 2:
                    data = text.replace("สะกด ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            maxgie.unsendMessage(msg_id)
                            maxgie.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(maxgie.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % maxgie.getContact(ls).pictureStatus})
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#66FF00"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#333300"
                                            },
                                            "footer": {
                                                "backgroundColor": "#66FF00",
                                                "separator": True,
                                               "separatorColor": "#333300"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "YouTube",
                                                    "weight": "bold",
                                                    "color": "#333300",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#333300"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "ชื่อ วีดีโอ",
                                                    "color": "#333300",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#333300",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#333300",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "เปิด",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#333300",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#333300",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//20
                                for aa in range(k+2):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*20 : (aa+2)*20]
                                        }
                                    }
                                    sendTemplate(to, data)
                
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("เพลสโต "):
                                query = removeCmd("เพลสโต", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                                        
                 #=====================================================================

                elif msg.text.lower().startswith("ยกเชิญ"):
                                if msg._from in maxgieMID:                                
                                    if msg.toType == 2:
                                        group = maxgie.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//20
                                        maxgie.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*20 : (i+1)*20]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                maxgie.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            maxgie.sendMessage(receiver,"พักแปปเดียวยกต่อ (•ω•)\n 『★ढेণढेююທ์★』 ")
                                            time.sleep(random.uniform(15,10))
                                        maxgie.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว👏]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        maxgie.sendMessage(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว👏\n『HACK_BOT』".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.leaveGroup(receiver)
                                								
                                    maxgie.sendMessage(receiver,"[ไม่มีค้างเชิญ แล้วนะ😁]")
                                    maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    maxgie.leaveGroup(receiver)
                #=====================================================================              
                elif msg.text.lower().startswith("ยกเลิก "):
                   args = msg.text.lower().replace("ยกเลิก ","")
                   mes = 0
                   try:
                       mes = int(args[1])
                   except:
                       mes = 100
                       M = maxgie.getRecentMessagesV2(to, 100)
                       MId = []
                       for ind,i in enumerate(M):
                           if ind == 0:
                               pass
                           else:
                               if i._from == maxgie.profile.mid:
                                   MId.append(i.id)
                                   if len(MId) == mes:
                                       break
                       def unsMes(id):
                           maxgie.unsendMessage(id)
                       for i in MId:
                           thread1 = threading.Thread(target=unsMes, args=(i,))
                           thread1.start()
                           thread1.join()
                       duc1(to, ' 「 กำลังยกเลิก 」\nยกเลิกทั้งหมด {} ข้อความ'.format(len(MId))) 
                       maxgie.unsendMessage(msg_id)                                       
#=====================================================================                                       
                
                
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.findAndAddContactsByMid(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    n = len(maxgie.getAllContactIds())
                                    try:
                                        maxgie.deleteContact(ls)
                                    except:pass
                                    t = len(maxgie.getAllContactIds())
                                    maxgie.generateReplyMessage(msg.id)
                                    duc1(id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.blockContact(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("ไอดีไลน์ "):
                            a = removeCmd("ไอดีไลน์", text)
                            b = maxgie.findContactsByUserid(a)
                            line = b.mid
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "line://ti/p/~" + a)
                            maxgie.sendContact(to, line)                                                                                           
                            maxgie.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = maxgie.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif "/ลบรัน" in msg.text.lower():
                    spl = re.split("/ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = maxgie.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        data = {"type": "text","text": "{}".format(str(txt)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                        sendTemplate(to, data)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                maxgie.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    maxgie.sendMessage(gr,spl[1])
                                maxgie.leaveGroup(gr)
                            except:
                                pass
                        sis = "สำเร็จแล้ว (｀・ω・´)"
                        data = {"type": "text","text": "{}".format(str(sis)),"sentBy": {"label": "{}".format(maxgie.getContact(maxgieMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                        sendTemplate(to, data)
            
#=====================================================================
#==============================================================================#
                elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอด":
                    group = maxgie.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                 #   profile = "https://profile.line-scdn.net/" + str(pp)
                    data = {
                        "type": "flex",
                        "altText": "แอดกลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "HACK_BOT",
                                        "size":"md",
                                       # "weight":"bold",
                                        "color":"#FF3333",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#FF3333",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendContact(to, c)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = maxgie.getGroup(to)
                  #  
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "{ Group ID }\n" + gid.id)
                    maxgie.sendMessage(to, maxgie.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+maxgie.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "HACK_BOT", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': 'HACK_BOT', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == 'รูปกลุ่ม':
                    group = maxgie.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = maxgie.getGroup(to)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "ชื่อกลุ่ม -> \n" + gid.name) 
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = maxgie.reissueGroupTicket(to)
                            maxgie.sendMessage(to, "ลิ้งของกลุ่ม : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "🌟เปิดลิ้งเรียบร้อย🌟")
                        else:
                            group.preventedJoinByTicket = False
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == True:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "🌟ปิดลิ้งเรียบร้อย🌟")
                        else:
                            group.preventedJoinByTicket = True
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = maxgie.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างกลุ่มนี้ลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(maxgie.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══『HACK_BOT』"
                    data = {
                        "type": "flex",
                        "altText": "กลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                            #        {
                            #            "type": "image",
                            #            "url": path, 
                            #            "size": "xl"
                            #        },
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'คนในห้อง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        ret_ = "รายชื่อสามชิกในกลุ่มนี้\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nจำนวน {} คน".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "กลุ่ม",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#000000'
                                    },
                                },
                                   "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = maxgie.groups
                        ret_ = "รายชื่อกลุ่มทั้งหมด :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = maxgie.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#000000'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "อัพรูปโปร":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งรูปภาพที่จะอัพมาเลยครับ🌟")
                elif text.lower() == "อัพรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "🌟ส่งรูปภาพที่จะอัพมาเลยครับ🌟")
            
                elif text.lower() == 'เพื่อน':
                    contactlist = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(contactlist)
                    num=1
                    msgs="☢️รายชื่อเพื่อนทั้งหมด☢️"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n☢️รายชื่อเพื่อนทั้งหมด☢️\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    maxgie.sendMessage(msg.to, msgs)
            #      if msg.toType == 2:                
#
             #              ginfo = line.getGroup(receiver)
             #              try:
             #                  gcmid = ginfo.creator.mid
             #              except:
             #                  gcmid = "Error"
             #              if settings["lang"] == "JP":
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่ม")
             #              else:
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")
                                
#====================================================================
                elif msg.text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "??ลบติ๊กคนแทคแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนเข้าแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนออกแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนแอดแล้วครับ🌟")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมาครับ🌟")
                elif msg.text.lower() == "ลบติ๊กมุดลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กมุดลิ้งแล้ว🌟")
                    
#=====================================================================
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = maxgie.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    maxgie.updateProfilePicture(path)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ทำการเปลี่ยนแล้วครับ🌟")
                    
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            maxgie.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            maxgie.sendMessage(to, str(ret_))
                        except Exception as error:
                            maxgie.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in maxgieMID:
                            try:
                                maxgie.kickoutFromGroup(msg.to,[sender])
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟บอกแล้วอย่าพิมจุกไปดิครับ🌟")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = maxgie.findGroupByTicket(ticket_id)
                                maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                maxgie.sendMessage(group.id,str(tagadd["m"]))
                            #    msgSticker = sets["messageSticker"]["listSticker"]["join2"]
                            #    if msgSticker != None:
                            #        sid = msgSticker["STKID"]
                            #        spkg = msgSticker["STKPKGID"]
                            #        sver = msgSticker["STKVER"]
                            #        sendSticker(group.id, str(sver), str(spkg), str(sid))
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟มุดเข้าลิ้งกลุ่ม %s เรียบร้อย 555🌟" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Sticker " + name + " Done...")
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    maxgie.sendMessage(to, str(ret_))
#=====================================================================
        if op.type == 22:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)              
        if op.type == 24:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == ".":
                    duc1(to, "🌟HACK_BOT🌟")
                if text.lower() =="คำสั่งแอดมิน":
                    maxgie.sendMessage(to,"คำสั่งแอด")
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] ข้อความจากคนอื่นที่ส่ง (•ω•)")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
             #   elif msg.contentType == 7:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
            #    elif msg.contentType == 7:
            #        if "/ti/g/" in msg.text.lower():
            #            if sets["autoJoinTicket"] == True:
            #                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
            #                links = link_re.findall(text)
            #                n_links = []
            #                for l in links:
            #                    if l not in n_links:
            #                        n_links.append(l)
            #                for ticket_id in n_links:
            #                    group = maxgie.findGroupByTicket(ticket_id)
            #                    maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   maxgie.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if tagadd["tags"] == True:
                             me = maxgie.getContact(sender)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in maxgieMID:
                                          cover = maxgie.getProfileCoverURL(sender)
                                          pp = me.pictureStatus
                                          profile = "https://profile.line-scdn.net/" + str(pp)
                                          name = me.displayName
                                          status = "\nสเตตัส\n" + me.statusMessage
                                          pk = str(tagadd["tag"])
                                          tz = pytz.timezone("Asia/Jakarta")
                                          timeNow = datetime.now(tz=tz)
                                          van2 = "✨เวลา:"+ datetime.strftime(timeNow,'%H:%M:%S')                                 	
                                          data = {
"type":"flex",
"altText": pk, 
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"contents": [
{
"text": name,
"size": "sm",
"align": "center",
"color": "#33FF33",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": pk, 
"align": "center",
"size": "sm",
"weight": "bold",
"color": "#33FF33",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"text": " ✨➡ เวลาแทค :"+van2 +" \n ✨➡ HACK_BOT",
"size": "xs",
"margin": "none",
"color": "#33FF33",
"wrap": True,
"weight": "regular",
"type": "text"
}
]
}
}
]
}
}                                          
                                          sendTemplate(to, data)                        
        if op.type == 26:
            print ("[ 26 ] ตรวจพบข้อความจากแชท ( • ̀ω•́  )")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                    #  contact = maxgie.getContact(maxgieMID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if maxgieMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   maxgie.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปรงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    maxgie.sendContact(msg.to,str(getx))
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        maxgie.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "list API", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~topzalove123"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != maxgie.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] ข้อความจากคนอื่นที่ส่ง (•ω•)")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxgie.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nเวลา :\n{} ที่ผ่าน".format(waktumsg)
                            rat_ += "\nข้อความที่ยกเลิก :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "#ตรวจพบยกเลิกข้อความ\n\nชื่อคนยกเลิก :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nเวลา :\n{} ที่ผ่าน".format(waktumsg)
                                rat_ += "\nรูปภาพที่ยกเลิก :"
                                sendMentionFooter(at, ikkeh.mid, "#ตรวจพบยกเลิกรูปภาพ\n\nชื่อคนยกเลิก :\n", str(rat_))
                                maxgie.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nเวลา :\n{} ที่ผ่าน".format(waktumsg)
                                    rat_ += "\nวิดีโอที่ยกเลิก :"
                                    sendMentionFooter(at, ikkeh.mid, "#ตรวจพบยกเลิกวิดีโอ\n\nชื่อคนยกเลิก :\n", str(rat_))
                                    maxgie.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxgie.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nเวลา :\n{} ที่ผ่าน".format(waktumsg)
                                            rat_ += "\nสติกเกอร์ที่ยกเลิก :"
                                            sendMentionFooter(at, ikkeh.mid, "#ตรวจพบยกเลิกสติกเกอร์\n\nชื่อคนยกเลิก :\n", str(rat_))
                                            maxgie.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxgie.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxgie.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxgie.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
        if op.type in [26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                  to = receiver
               elif msg.toType == 2:
                  to = receiver
               if msg.contentType == 0:
                  if text is None:
                     return
                  else:
                    if receiver in temp_flood:
                      if temp_flood[receiver]["expire"] == True:
                        if msg.text == "/open":
                           temp_flood[receiver]["expire"] = False
                           temp_flood[receiver]["time"] = time.time()
                           maxgie.sendMessage(to,"Bot Actived")
                        return
                      elif time.time() - temp_flood[receiver]["time"] <= 5:
                         temp_flood[receiver]["flood"] += 1
                         if temp_flood[receiver]["flood"] >= 200:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟มีคนส่งข้อความเกิน200ระบบขอออกอัติโนมัติ🌟")
                            maxgie.leaveGroup(to)
                      else:
                       temp_flood[receiver]["flood"] = 0
                      temp_flood[receiver]["time"] = time.time()
                    else:
                      temp_flood[receiver] = {
                       "time": time.time(),
                       "flood": 0,
                       "expire": False
}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
        if op.type == 55:
            print ("[ 55 ] ตรวจพบข้อความจากคนอื่น")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = maxgiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(maxgieBot(op))
                   maxgiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
