import json
import os
import requests
def lambda_handler(event,context):
    json_str = json.dumps(event)
    request_body = json.loads(json_str)
    request_msg = request_body['message']
    chat_id = request_body['message']['chat']['id']
    command = request_body['message']['text'].strip('"')
   
   # TODO implement
    BOT_TOKEN = ''
    BOT_CHAT_ID = ''
    BOT_CHAT_ID = chat_id 
   
    
    print(command)
    
    if command == 'start':
       message = "Welcome to my bot! How can I help you today?"
    elif command == 'help':
       message = "Here are the available commands: /start, /help"
    else:
       message = "I'm sorry, I didn't understand that command. Please try again."
       
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + \
        '&parse_mode=HTML&text=' + message
    response = requests.get(send_text)
    
    print(send_text)
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
   }
