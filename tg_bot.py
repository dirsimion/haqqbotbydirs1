import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import lxml

bot = telebot.TeleBot('5369582486:AAFbiW1ayq0Cc8KgYsrMmfcl89lMUh4KZA0')
context = {}
valtoken = ''
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome to haqq_cryptoBOT! To read the help, send me /help')

@bot.message_handler(commands=['help'])
def helps(message):
    bot.send_message(message.chat.id, '''Commands of this bot:
/help - help(this message)
/add - to add and check valoper
/info - to read info about HAQQ
/roadmap - to check haqq-roadmap
/workflow - to check workflow
''')

@bot.message_handler(commands=['info'])
def infomessage(message):
    bot.send_message(message.chat.id, '''Haqq Blockchain — Haqq (Arabic for truth) is a Proof of Stake
blockchain network compatible with the existing ecosystem of 
Blockchain tools and developer instruments (primarily, Ethereum and Cosmos)
and meeting modern industry requirements, with fast-finality
and high transactions troughtput. Haqq’s purpose is to serve 
the international Muslim community by providing a financial 
and technological tool that allows for independent financial interaction,
while supporting technological evolution and philanthropy.
Islamic Coin — purposeful community crypto asset. 
It’s used as a native coin on the Haqq blockchain. 
Each time a new Islamic Coin is minted, 10% of the issued amount is deposited into a special. 
Evergreen DAO for further investment into projects beneficiary 
for Muslim community or given to Islamic charities. 
This is the first introduction of a coin bringing direct economic value to a community.''')
    photo = open('islamic_coin.jpg','rb')
    bot.send_photo(message.chat.id, photo)
@bot.message_handler(commands=['roadmap'])
def roadmappic(message):
    photo = open('roadmap.jpg','rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['workflow'])
def workflowpic(message):
    photo = open('workflow.jpg','rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['add'])
def add_token(message):
   message =  bot.send_message(message.chat.id, 'Now send me the valoper address')
   bot.register_next_step_handler(message, get_token)
def get_token(message):
    global valtoken
    valtoken = message.text

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    url = "https://haqq.explorers.guru/validator/" + valtoken
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    valinfo = soup.find_all(class_="card css-1h397wl")
    valinfo = str(valinfo)
    status_info = "Inactive"
    if valinfo.find("Inactive") == -1:
        status_info = "Active"

    injail_info = "No"
    if valinfo.find("No") == -1:
        injail_info = "Yes"
    bot.send_message(message.chat.id, f'Status: {status_info}\nInJail: {injail_info}')






bot.polling(none_stop=True)