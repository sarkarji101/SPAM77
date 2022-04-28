import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from Config import STRING, SUDO, BIO_MESSAGE, ALIVE_NAME, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8, STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15,STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30, STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50, STRING51, STRING52, STRING53, STRING54, STRING55, STRING56, STRING57, STRING58, STRING59, STRING60
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25
tsix = STRING26
tseven = STRING27
teight = STRING28
tnine = STRING29
thirty = STRING30
gone  = STRING31
gtwo = STRING32
gthree = STRING33
gfour = STRING34
gfive = STRING35
gsix = STRING36
gseven = STRING37
geight = STRING38
gnine = STRING39
gten = STRING40
fone = STRING41
ftwo = STRING42
fthree = STRING43
ffour = STRING44
ffive = STRING45
fsix = STRING46
fseven = STRING47
feight = STRING48
fnine = STRING49
ften = STRING50
sone = STRING51
stwo = STRING52
sthree = STRING53
sfour = STRING54
sfive = STRING55
ssix = STRING56
sseven = STRING57
seight = STRING58
snine = STRING59
sten = STRING60


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""
eag = ""
gle = ""
wal = ""
aaa = ""
boy = ""
aab = ""
aac = ""
aad = ""
aae = ""
aaf = ""
aag = ""
aah = ""
aai = ""
aaj = ""
aak = ""
aal = ""
aam = ""
aan = ""
aao = ""
aap = ""
aaq = ""
aar = ""
aas = ""
aat = ""
aau = ""
aav = ""
aaw = ""
aax = ""
aay = ""
aaz = ""
bba = ""
bbb = ""
bbc = ""
bbd = ""
bbe = ""


que = {}

SMEX_USERS = [5098147320 ,5088683114]
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_aries():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    global eag
    global gle
    global wal
    global aaa
    global boy
    global aab
    global aac
    global aad
    global aae
    global aaf
    global aag
    global aah
    global aai
    global aaj
    global aak
    global aal
    global aam
    global aan
    global aao
    global aap
    global aaq
    global aar
    global aas
    global aat
    global aau
    global aav
    global aaw
    global aax
    global aay
    global aaz
    global bba
    global bbb
    global bbc
    global bbd
    global bbe    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            await idk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, a, b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, a, b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, a, b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, a, b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, a, b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, a, b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await aan.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, a, b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, a, b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, a, b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, a, b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, a, b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, a, b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
    if tsix:
        session_name = str(tsix)
        print("String 26 Found")
        eag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await eag.start()
            botme = await eag.get_me()
            await eag(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        eag = TelegramClient(session_name, a, b)
        try:
            await eag.start()
        except Exception as e:
            pass
   
    if tseven:
        session_name = str(tseven)
        print("String 27 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await gle.start()
            await gle(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gle.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        gle = TelegramClient(session_name, a, b)
        try:
            await gle.start()
        except Exception as e:
            pass

    if teight:
        session_name = str(teight)
        print("String 28 Found")
        wal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await wal.start()
            await wal(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await wal.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        wal = TelegramClient(session_name, a, b)
        try:
            await wal.start()
        except Exception as e:
            pass

    if tnine:
        session_name = str(tnine)
        print("String 29 Found")
        aaa = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await aaa.start()
            await aaa(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await aaa.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        aaa = TelegramClient(session_name, a, b)
        try:
            await aaa.start()
        except Exception as e:
            pass

    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        boy = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await boy.start()
            await boy(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await boy.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        boy = TelegramClient(session_name, a, b)
        try:
            await boy.start()
        except Exception as e:
            pass

    if gone:
        session_name = str(gone)
        print("String 30 Found")
        aab = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 31")
            await gone.start()
            await gone(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gone.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aab = TelegramClient(session_name, a, b)
        try:
            await aab.start()
        except Exception as e:
            pass

    if gtwo:
        session_name = str(gtwo)
        print("String Found")
        aac = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 32")
            await gtwo.start()
            await gtwo(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gtwo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aac = TelegramClient(session_name, a, b)
        try:
            await aac.start()
        except Exception as e:
            pass

    if gthree:
        session_name = str(gthree)
        print("String Found")
        aad = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 33")
            await gthree.start()
            await gthree(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gthree.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aad = TelegramClient(session_name, a, b)
        try:
            await aad.start()
        except Exception as e:
            pass

    if gfour:
        session_name = str(gfour)
        print("String Found")
        aae = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 34")
            await gfour.start()
            await gfour(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gfour.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aae = TelegramClient(session_name, a, b)
        try:
            await aae.start()
        except Exception as e:
            pass

    if gfive:
        session_name = str(gfive)
        print("String Found")
        aaf = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 35")
            await gfive.start()
            await gfive(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gfive.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aaf = TelegramClient(session_name, a, b)
        try:
            await aaf.start()
        except Exception as e:
            pass

    if gsix:
        session_name = str(gsix)
        print("String Found")
        aag = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 36")
            await gsix.start()
            await gsix(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gsix.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aag = TelegramClient(session_name, a, b)
        try:
            await aag.start()
        except Exception as e:
            pass

    if gseven:
        session_name = str(gseven)
        print("String Found")
        aah = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 37")
            await gseven.start()
            await gseven(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gseven.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aah = TelegramClient(session_name, a, b)
        try:
            await aah.start()
        except Exception as e:
            pass

    if geight:
        session_name = str(geight)
        print("String Found")
        aai = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 38")
            await geight.start()
            await geight(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await geight.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aai = TelegramClient(session_name, a, b)
        try:
            await aai.start()
        except Exception as e:
            pass

    if gnine:
        session_name = str(gnine)
        print("String Found")
        aaj = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 39")
            await gnine.start()
            await gnine(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gnine.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aaj = TelegramClient(session_name, a, b)
        try:
            await aaj.start()
        except Exception as e:
            pass

    if gten:
        session_name = str(gten)
        print("String Found")
        aak = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 40")
            await gteny.start()
            await gten(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await gten.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aak = TelegramClient(session_name, a, b)
        try:
            await aak.start()
        except Exception as e:
            pass

    if fone:
        session_name = str(fone)
        print("String Found")
        aal = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 41")
            await fone.start()
            await fone(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await fone.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aal = TelegramClient(session_name, a, b)
        try:
            await aal.start()
        except Exception as e:
            pass

    if ftwo:
        session_name = str(ftwo)
        print("String 30 Found")
        aam = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 42")
            await ftwo.start()
            await ftwo(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ftwo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aam = TelegramClient(session_name, a, b)
        try:
            await aam.start()
        except Exception as e:
            pass

    if fthree:
        session_name = str(fthree)
        print("String Found")
        aan = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 43")
            await fthree.start()
            await fthree(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await fthree.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aan = TelegramClient(session_name, a, b)
        try:
            await aan.start()
        except Exception as e:
            pass

    if ffour:
        session_name = str(ffour)
        print("String Found")
        aao = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 44")
            await ffour.start()
            await ffour(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ffour.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aao = TelegramClient(session_name, a, b)
        try:
            await aao.start()
        except Exception as e:
            pass

    if ffive:
        session_name = str(ffive)
        print("String Found")
        aap = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 45")
            await ffive.start()
            await ffive(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ffive.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aap = TelegramClient(session_name, a, b)
        try:
            await aap.start()
        except Exception as e:
            pass

    if fsix:
        session_name = str(fsix)
        print("String Found")
        aaq = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 46")
            await fsixy.start()
            await fsix(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await fsix.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aaq = TelegramClient(session_name, a, b)
        try:
            await aaq.start()
        except Exception as e:
            pass

    if fseven:
        session_name = str(fseven)
        print("String Found")
        aar = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 47")
            await fseven.start()
            await fseven(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await fseven.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aar = TelegramClient(session_name, a, b)
        try:
            await aar.start()
        except Exception as e:
            pass

    if feight:
        session_name = str(feight)
        print("String Found")
        aas = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 48")
            await feighty.start()
            await feight(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await feight.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aas = TelegramClient(session_name, a, b)
        try:
            await aas.start()
        except Exception as e:
            pass

    if fnine:
        session_name = str(fnine)
        print("String Found")
        aat = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 49")
            await fnine.start()
            await fnine(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await fnine.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aat = TelegramClient(session_name, a, b)
        try:
            await aat.start()
        except Exception as e:
            pass

    if ften:
        session_name = str(ften)
        print("String Found")
        aau = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 50")
            await ften.start()
            await ften(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ften.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aau = TelegramClient(session_name, a, b)
        try:
            await aau.start()
        except Exception as e:
            pass

    if sone:
        session_name = str(sone)
        print("String Found")
        aav = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 51")
            await sone.start()
            await sone(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sone.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aav = TelegramClient(session_name, a, b)
        try:
            await aav.start()
        except Exception as e:
            pass

    if stwo:
        session_name = str(stwo)
        print("String Found")
        aaw = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 52")
            await stwo.start()
            await stwo(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await stwo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aaw = TelegramClient(session_name, a, b)
        try:
            await aaw.start()
        except Exception as e:
            pass

    if sthree:
        session_name = str(sthree)
        print("String Found")
        aax = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 53")
            await sthree.start()
            await sthree(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sthree.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aax = TelegramClient(session_name, a, b)
        try:
            await aax.start()
        except Exception as e:
            pass

    if sfour:
        session_name = str(sfour)
        print("String Found")
        aay = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 54")
            await sfour.start()
            await sfour(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sfour.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aay = TelegramClient(session_name, a, b)
        try:
            await aay.start()
        except Exception as e:
            pass

    if sfive:
        session_name = str(sfive)
        print("String Found")
        aaz = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 55")
            await sfive.start()
            await sfive(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sfive.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        aaz = TelegramClient(session_name, a, b)
        try:
            await aaz.start()
        except Exception as e:
            pass

    if ssix:
        session_name = str(ssix)
        print("String Found")
        bba = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 56")
            await ssix.start()
            await ssix(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await ssix.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        bba = TelegramClient(session_name, a, b)
        try:
            await bba.start()
        except Exception as e:
            pass

    if sseven:
        session_name = str(sseven)
        print("String Found")
        bbb = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 57")
            await sseveny.start()
            await sseven(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sseven.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        bbb = TelegramClient(session_name, a, b)
        try:
            await bbb.start()
        except Exception as e:
            pass

    if seight:
        session_name = str(seight)
        print("String Found")
        bbc = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 58")
            await seight.start()
            await seight(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await seight.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        bbc = TelegramClient(session_name, a, b)
        try:
            await bbc.start()
        except Exception as e:
            pass

    if snine:
        session_name = str(snine)
        print("String Found")
        bbd = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 59")
            await snine.start()
            await snine(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await snine.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        bbd = TelegramClient(session_name, a, b)
        try:
            await bbd.start()
        except Exception as e:
            pass

    if sten:
        session_name = str(sten)
        print("String Found")
        bbe = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 60")
            await sten.start()
            await sten(functions.channels.JoinChannelRequest(channel="@DAKU_SPAM"))
            botme = await sten.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session not Found")
        pass
        session_name = "startup"
        bbe = TelegramClient(session_name, a, b)
        try:
            await bbe.start()
        except Exception as e:
            pass
                
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_aries())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.xs")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.xs")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.xs")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.xs")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.xs")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.xs"))
async def xs(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.xs <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        flash = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(flash) == 2:
            message = str(flash[1])
            counter = int(flash[0])
            if counter > 5000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(flash[0])
            if counter > 5000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(flash[0])
            if counter > 5000:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.raid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.raid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.raid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.raid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.raid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(aries[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.01)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(aries[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.01)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
          
@idk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.alive")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.alive")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.alive")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.alive")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.alive")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.alive"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        text = " [⚚ 𓆩𝐃𝐀𝐊𝐔𝐱𝐄𝐍𝐆𝐈𝐍𝐄𝐄𝐑𓆪️ ⚚] \n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➤ 𝐎𝐅 : ENGINEER\n ┣➤ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : @NITPAID \n ┣➤ 𝐁𝐘 : 𝐒𝐀𝐑𝐊𝐀𝐑\n ┗━━━━━━━━━━━━━━━━━━━ "
        await e.reply(text, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def join(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = aries[0]
            text = "𝗔𝗥𝗛𝗔 𝗛𝗨 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 😠🔥"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝗔𝗥𝗛𝗔 𝗛𝗨 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 😠🔥️")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
                        

@idk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bio")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bio")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bio")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bio")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bio")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
async def bio(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(yukki[0])
            text = "ʙɪᴏ ᴄʜᴀɴɢɪɴɢ ᴅᴏɴᴇ ༒"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("ʙɪᴏ ᴄʜᴀɴɢɪɴɢ ᴅᴏɴᴇ ༒")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "ᗩᗷ ᑕᕼᑌᗞᗴᏀᏆ ᎢᗴᖇᏆ ᗰᗩ̂ᗩ̂"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "𝔸𝔹 𝔹𝕆𝕃 𝔹𝕊𝔻𝕂 𝕂𝔼 "
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def dreplyraid(e):
    global que
    usage = "𓆩𝘿𝘼𝙆𝙐〆𝙀𝙉𝙂𝙄𝙉𝙀𝙀𝙍𓆪\n\n 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 \n【﻿Command :】\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝐀𝐁 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐂𝐇𝐔𝐃𝐄𝐆𝐈 😂"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "𝐉𝐀𝐀 𝐌𝐀𝐀𝐅 𝐊𝐈𝐘𝐀 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )                     
          


@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.leave")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.leave")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.leave")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.leave")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.leave")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def leave(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "𝗦𝗢𝗢𝗡 𝗕𝗔𝗖𝗞 𝗕𝗦𝗗𝗞"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝗦𝗢𝗢𝗡 𝗕𝗔𝗖𝗞 𝗕𝗦𝗗𝗞")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def bigspam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.01)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.01)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(aries[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.01)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
 
               
@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.ping"))     
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = " ⚚ 𓆩𝗗𝗔𝗞𝗨𝘅𝗘𝗡𝗚𝗜𝗡𝗘𝗘𝗥𓆪️ ⚚️ "
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 500
        await event.edit(f"  ⚚ 𓆩𝗗𝗔𝗞𝗨𝘅𝗘𝗡𝗚𝗜𝗡𝗘𝗘𝗥𓆪️ ⚚️  `{ms}` ")




@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝗥𝗘𝗦𝗧𝗔𝗥𝗧𝗜𝗡𝗚...."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        try:
            await vkk.disconnect()
        except Exception as e:
            pass
        try:
            await kkk.disconnect()
        except Exception as e:
            pass
        try:
            await lkk.disconnect()
        except Exception as e:
            pass
        try:
            await mkk.disconnect()
        except Exception as e:
            pass
        try:
            await sid.disconnect()
        except Exception as e:
            pass
        try:
            await shy.disconnect()
        except Exception as e:
            pass
        try:
            await aan.disconnect()
        except Exception as e:
            pass
        try:
            await ake.disconnect()
        except Exception as e:
            pass
        try:
            await eel.disconnect()
        except Exception as e:
            pass
        try:
            await khu.disconnect()
        except Exception as e:
            pass
        try:
            await shi.disconnect()
        except Exception as e:
            pass
        try:
            await yaa.disconnect()
        except Exception as e:
            pass
        try:
            await dav.disconnect()
        except Exception as e:
            pass
        try:
            await raj.disconnect()
        except Exception as e:
            pass
        try:
            await put.disconnect()
        except Exception as e:
            pass
        try:
            await eag.disconnect()
        except Exception as e:
            pass
        try:
            await gle.disconnect()
        except Exception as e:
            pass
        try:
            await wal.disconnect()
        except Exception as e:
            pass
        try:
            await aaa.disconnect()
        except Exception as e:
            pass
        try:
            await boy.disconnect()
        except Exception as e:
            pass
        try:
            await aab.disconnect()
        except Exception as e:
            pass
        try:            
            await aac.disconnect()
        except Exception as e:
            pass
        try:            
            await aad.disconnect()
        except Exception as e:
            pass
        try:            
            await aae.disconnect()
        except Exception as e:
            pass
        try:            
            await aaf.disconnect()
        except Exception as e:
            pass
        try:            
            await aag.disconnect()
        except Exception as e:
            pass
        try:            
            await aah.disconnect()
        except Exception as e:
            pass
        try:            
            await aai.disconnect()
        except Exception as e:
            pass
        try:            
            await aaj.disconnect()
        except Exception as e:
            pass
        try:            
            await aak.disconnect()
        except Exception as e:
            pass
        try:            
            await aal.disconnect()
        except Exception as e:
            pass
        try:            
            await aam.disconnect()
        except Exception as e:
            pass
        try:            
            await aan.disconnect()
        except Exception as e:
            pass
        try:            
            await aao.disconnect()
        except Exception as e:
            pass
        try:            
            await aap.disconnect()
        except Exception as e:
            pass
        try:            
            await aaq.disconnect()
        except Exception as e:
            pass
        try:            
            await aar.disconnect()
        except Exception as e:
            pass
        try:            
            await aas.disconnect()
        except Exception as e:
            pass
        try:            
            await aat.disconnect()
        except Exception as e:
            pass
        try:            
            await aau.disconnect()
        except Exception as e:
            pass
        try:            
            await aav.disconnect()
        except Exception as e:
            pass
        try:            
            await aaw.disconnect()
        except Exception as e:
            pass
        try:            
            await aax.disconnect()
        except Exception as e:
            pass
        try:            
            await aay.disconnect()
        except Exception as e:
            pass
        try:            
            await aaz.disconnect()
        except Exception as e:
            pass
        try:            
            await bba.disconnect()
        except Exception as e:
            pass
        try:            
            await bbb.disconnect()
        except Exception as e:
            pass
        try:            
            await bbc.disconnect()
        except Exception as e:
            pass
        try:            
            await bbd.disconnect()
        except Exception as e:
            pass
        try:            
            await bbe.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.help")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.help")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.help")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.help")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.help")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@eag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@gle.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@boy.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aab.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aac.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aad.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aae.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaf.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aah.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aai.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aak.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aam.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aao.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aap.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaq.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aar.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aas.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aat.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aau.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaw.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aax.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aay.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@aaz.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bba.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bbb.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bbc.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bbd.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bbe.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.sudo\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.pornspam\n.delayspam\n.bigspam\n.sraid\n.jraid\n.craid\n.replyraid\n.dreplyraid\n\n\n𝑇𝑌𝑃𝐸 𝑃𝐿𝑈𝐺𝐼𝑁𝑆 𝑁𝐴𝑀𝐸 TO JOIN @DAKU_SPAM"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """
⚜️ 𝙂𝙤 𝘿𝙤 .𝙥𝙞𝙣𝙜 𝙖𝙩 @DAKU_SPAM ⚜️"""

print(text)
print("")
print("𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗥𝗘𝗔𝗗𝗬 𝗙𝗢𝗥 𝗨𝗦𝗘")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
    try:
        eag.disconnect()
    except Exception as e:
        pass
    try:
        gle.disconnect()
    except Exception as e:
        pass
    try:
        wal.disconnect()
    except Exception as e:
        pass
    try:
        aaa.disconnect()
    except Exception as e:
        pass
    try:
        boy.disconnect()
    except Exception as e:
        pass
    try:
        aab.disconnect()
    except Exception as e:
        pass
    try:
        aac.disconnect()
    except Exception as e:
        pass
    try:
        aad.disconnect()
    except Exception as e:
        pass
    try:
        aae.disconnect()
    except Exception as e:
        pass
    try:
        aaf.disconnect()
    except Exception as e:
        pass
    try:
        aag.disconnect()
    except Exception as e:
        pass
    try:
        aah.disconnect()
    except Exception as e:
        pass
    try:
        aai.disconnect()
    except Exception as e:
        pass
    try:
        aaj.disconnect()
    except Exception as e:
        pass
    try:
        aak.disconnect()
    except Exception as e:
        pass
    try:
        aal.disconnect()
    except Exception as e:
        pass
    try:
        aam.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        aao.disconnect()
    except Exception as e:
        pass
    try:
        aap.disconnect()
    except Exception as e:
        pass
    try:
        aaq.disconnect()
    except Exception as e:
        pass
    try:
        aar.disconnect()
    except Exception as e:
        pass
    try:
        aas.disconnect()
    except Exception as e:
        pass
    try:
        aat.disconnect()
    except Exception as e:
        pass
    try:
        aau.disconnect()
    except Exception as e:
        pass
    try:
        aav.disconnect()
    except Exception as e:
        pass
    try:
        aaw.disconnect()
    except Exception as e:
        pass
    try:
        aax.disconnect()
    except Exception as e:
        pass
    try:
        aay.disconnect()
    except Exception as e:
        pass
    try:
        aaz.disconnect()
    except Exception as e:
        pass
    try:
        bba.disconnect()
    except Exception as e:
        pass
    try:
        bba.disconnect()
    except Exception as e:
        pass
    try:
        bbc.disconnect()
    except Exception as e:
        pass
    try:
        bbd.disconnect()
    except Exception as e:
        pass
    try:
        bbe.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        gle.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        boy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aab.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aac.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aad.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aae.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaf.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aah.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aai.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aak.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aam.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aao.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aap.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aaq.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aar.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aas.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aat.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aau.run_until_disconnected()
    except Exception as e:
        pass   
    try:             
        aav.run_until_disconnected()
    except Exception as e:
        pass 
    try:               
        aaw.run_until_disconnected()
    except Exception as e:
        pass
    try:        
        aax.run_until_disconnected()
    except Exception as e:
        pass
    try:        
        aay.run_until_disconnected()
    except Exception as e:
        pass 
    try:               
        aaz.run_until_disconnected()
    except Exception as e:
        pass
    try:        
        bba.run_until_disconnected()
    except Exception as e:
        pass 
    try:       
        bbb.run_until_disconnected()
    except Exception as e:
        pass
    try:        
        bbc.run_until_disconnected()
    except Exception as e:
        pass
    try:        
        bbe.run_until_disconnected()
    except Exception as e:
        pass        