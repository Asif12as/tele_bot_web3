
#TELE BOT NAME IS (webthree_com)

import gspread
import keys

from oauth2client.service_account import ServiceAccountCredentials
from telegram.ext import *

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)
client = gspread.authorize(creds)
sheet = client.open("bot")

print('Starting up bot...')

investor_flag = 0
all_inputs= " "
start_flag=0
answers={}

def start_command(update, context):
    update.message.reply_text('Hello there 👋 ! I\'m a smart bot 🕶️ . What\'s up?')

def reply_command(update, context):
    update.message.reply_text( context)



def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

def company_command(update, context):
    update.mesaage.reply_text('Thank  you for choosing  a company 👍')



def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')

def investor_(update, context):
    update.message.reply_text('.')


    

def handle_response(text) -> str:
    global investor_flag
    global all_inputs
    global start_flag
    global answers
    global sheet
   
    
        
    if 'investor' in text or 'investor' in all_inputs :

        
        if investor_flag ==0:
            status=('\n 👉💥--> Please tell us your exprience till now in,\n if it is possible let us know about web3.0 field wthin max of max --> 20words  📩 \n do not worry about it , if you do not want to share, you can skip this by giving us any albhabetic letter ➿  ==>')
            investor_flag=1
            all_inputs += text
            return status
        if investor_flag ==1:
            answers["exprience"] = text
            name=('\n What is your name 👉💥-->> ')
            investor_flag=2
            all_inputs += text
            return name
        if investor_flag ==2:
            answers["name"] = text
            c_company=('\n What is the name of the company in which you have invested 👉-->>')
            investor_flag=3
            all_inputs += text
            return c_company
        if investor_flag ==3:
            answers["company_name"] = text  
            web_name=('\n website name 👉💥-->> ')
            investor_flag=4
            all_inputs += text 
            return web_name
        if investor_flag ==4:
            answers["website_name"] = text
            linkdn=('\n Enter the linkedin profile if it is possible👉 💥 \n or else you can skip this  question by sending us a message NA ⚠️-->> ')
            investor_flag=5  
            all_inputs += text 
            return linkdn
        if investor_flag ==5:
            answers["linkedin_profile"] = text    
            submitted=('❤️❤️ Thank for giving  your valuable time ❤️❤️❤️❤️...\n')
            stored=('Your 🔹 data has been successfully added 🔹 to the Edgeln platform\n\n')

            display = ('Exprience:👉 '+ answers.get('exprience')+'\n')
            display += ('Your name:👉 '+ answers.get('name')+'\n')
            display += ('Company :👉 '+ answers.get('company_name')+'\n')
            display += ('website:👉 '+ answers.get('website_name')+'\n')
            display += ('socail id:👉 '+ answers.get('linkedin_profile')+'\n')
            sheet.get_worksheet(0).append_row([answers.get('exprience'),answers.get('name'),answers.get('company_name'),answers.get('website_name'),answers.get('linkedin_profile')])

            investor_flag = 0
            all_inputs= " "
            start_flag=0
            answers={}
           
            return submitted + stored+display

          
       
    if 'company' in text or 'company' in all_inputs:

        if investor_flag ==0: 
            


            name=('\n What is your company name 👉-->> ')
           
            investor_flag=1
            all_inputs += text
            return name
        if investor_flag ==1:
            answers["company_name"] = text
            comp_web=('\n Please Enter your company website 👉-->> ')
            investor_flag=2
            all_inputs += text
            return comp_web
        if investor_flag ==2:
            answers["company_web"] = text
            c_company=('\n Please let us know a short description 🔹about your company  \n Do not worry it\'s optional🏚️\n If you do not want to describe about your company so please add anything in the typing box  and go further\n\n 👉-->>')
            investor_flag=3
            all_inputs += text
            return c_company
      
       
        if investor_flag ==3: 
            answers["company_deatil"] = text 

            submitted=('❤️❤️🔹 Thanks  for your valuable time ❤️🔹❤️...')
            stored=('\n💠 Your data has been 🔹successfully added🔹 to the Edgeln🔹 platform..')


            
            display1 = ('\n\nCompany name:👉 '+ answers.get('company_name')+'\n')
            display1 += ('Company website :👉 '+ answers.get('company_web')+'\n')
            display1 += ('About company (optional):👉 '+ answers.get('company_deatil')+'\n')
          
            sheet.get_worksheet(1).append_row([answers.get('company_name'),answers.get('company_web'),answers.get('company_deatil')])

            investor_flag = 0
            all_inputs= " "
            start_flag=0
            answers={}
             
            return submitted + stored + display1
        

    #if start_flag ==1  and ('investor' not in text or 'company'  not in text):
   
        # noop= (" 👉💥----> Please choose ...anyone of the given followings \n 👉 💥-->  1_investor \n 👉💥-->  2_company " )
        # return noop

    else:
        start_flag=1
        greet= 'hii there! i am a smart bot\n\n🥰'
        noop= (" 👉💥----> Please Type  anyone of the  followings given below you are belongs to. \n 👉 💥-->  (1)investor \n 👉💥-->  (2)company " )
        return greet + noop


def handle_message(update, context):

    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''


    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    
    if message_type == 'group':
     
        if '@web_info_asi1_bot' in text:
            new_text = text.replace('@web_info_asi1_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

 
    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('invesor', investor_))

    dp.add_handler(CommandHandler('company', company_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idle()