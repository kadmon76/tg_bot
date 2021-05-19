import json
import re
import requests
import datetime as dt
from varibales import YOUTUBE_REGEX , TELEGRAM_TOKEN
from urllib.parse import urlparse, parse_qs


#--- func for opening files
#varibles :
#file_name(str)
#type_of_command ('r','w','a')
#payload = default as None
def open_file(filename , type_of_command, payload = None):
    with open(filename , type_of_command) as f:
        if type_of_command == 'r':
            return f.readlines()
        elif type_of_command == 'w' :
            return f.write(payload+'\n')
        elif  type_of_command == 'a':
            return f.write(payload + '\n')
#---check if message contains url ---#
# param message = telegram message (type dic)
def check_if_url(message):
    if "entities" in message["message"]:
        if message["message"]["entities"][0]["type"] == "url":
            return True
    else: print("only text")
#---check if there youtube url and extract url
#param - message = telegram message (type - dic)
#return youtube_link_str (type -str)
def parse_yt_url(message):
    text_message = message["message"]["text"]
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    youtube_link_tuple = re.findall(regex,text_message) #<--find url
    youtube_link_str = "".join([x[0] for x in youtube_link_tuple]) 
    print(youtube_link_str)
    match = YOUTUBE_REGEX.match(youtube_link_str) #<---matching text to youtube
    if match: #<--if there is youtube url
        return youtube_link_str

#-----parse message id from telegram message-----#
def get_message_number(message):
    return message['message']['message_id']

#-----parse message date from telegram message------#
def date_from_message(message):
    json_date = message['message']['date']
    message_date = dt.date.fromtimestamp(json_date).strftime('%d/%m/%Y')
    return message_date

#---parse name of message sender ----#
def name_of_sender(message):
    name_sender = message['message']['chat']['first_name'] +" "+ message['message']['chat']['last_name']
    return name_sender

#---grab youtube video id
#param url = youtube url (type- str)
def get_yt_video_id(url):
    """Returns Video_ID extracting from the given url of Youtube
    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',
      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url
        
    query = urlparse(url)
    
    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError

#---check if it is not a repost return bool ---#
def check_for_repost(youtube_video_id , list_videos_id):
    if  [True for i in list_videos_id if i == youtube_video_id]:
        return True

#----save youtube link with name and date to txt file----#
def save_youtube_link_to_file(message_number , youtube_link , name_of_sender , date_of_message ):
    payload = {
    'message_number' : message_number ,
    "youtube_link" : youtube_link ,
    "name_of_sender": name_of_sender ,
    "date_of_message" : date_of_message
    }
    with open('youtube_links.txt' , 'a') as f:
        json.dump(payload , f)
        f.write('\n')

#---send message to telegram 
def send_message_to_telegram_chat(chat_id, text = 'bla bla'):
    #param :
    #chat_id - telegram chat id
    #text = defualt "bla bla" (type -str)
    #return r
    urlencode = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id' : chat_id, 'text' : text}
    r = requests.post(urlencode, json = payload)
    return r

#---check for reg in message txt 
def regex_check(message_txt, reg = ''):
    #param messgae_txt = message text (type - str)
    #param reg = regular expretion (type -str)
    #return bool
    x = re.search(reg, message_txt)
    if x :
        print('asking for playlist')
        return True


# def add_video_to_pl ():
#     youtube = build('youtube','v3', credentials = credentials)
#     playlist_request = youtube.playlistItems().insert(
#         part="snippet,status",
#         body={
#         "kind": "youtube#playlistItem",
#         "snippet": {
#             "playlistId": playlist_info['id'],
#             "resourceId": {
#             "kind": "youtube#video",
#             "videoId": youtube_id
#             }
#         },
#         "status": {
#             "privacyStatus": "public"
#         }
#         }
#     )
#     response = playlist_request.execute() 
#     time.sleep(0.3)
#     print(f"adding video_id {youtube_id}")


def main():
    # message = read_json_file(r'C:\yaron\python\telegram_bot\bot2\telegram_message.json')
    # if check_if_url(message) : #<-- check if message contain url
    #     youtube_link = parse_yt_url(message) #<--parse youtube link    
    #     sender_name = name_of_sender(message) #<-- parse name of sender
    #     message_date = date_from_message(message) #<-- parse date
    #     youtube_video_id = get_yt_video_id(youtube_link)
    #     save_youtube_link_to_file(youtube_link , sender_name , message_date)
    pass
#main()

