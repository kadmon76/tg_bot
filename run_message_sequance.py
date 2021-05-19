from messages_function import *
from varibales import *
def run_message_sequance(message):
    if check_if_url(message) : #<-- check if message contain url
        message_number = get_message_number(message) #<--parse message number
        youtube_link = parse_yt_url(message) #<--parse youtube link    
        sender_name = name_of_sender(message) #<-- parse name of sender
        message_date = date_from_message(message) #<-- parse message date
        message_txt = message["message"]["text"]
        youtube_video_id = get_yt_video_id(youtube_link) #<-- parse video id
        list_videos_ids = open_file(LIST_OF_VIDEOS_IDS , 'r')
        print (list_videos_ids)
        if check_for_repost(youtube_video_id , [i.strip() for i in list_videos_ids]) != True: #<-- check if it is a repost
        #---not a repost---#
            open_file(LIST_OF_VIDEOS_IDS,'a',youtube_video_id) #<--add video id to list of video ids
            save_youtube_link_to_file(message_number , youtube_link , sender_name , message_date)
            send_message_to_telegram_chat(TELEGRAM_CHAT_ID , 'bip bop I am a bot \n youtube link saved ')
            print('saved to youtube_links and to list_of_videos_ids')
            return print(message_number , youtube_link , sender_name , message_date, youtube_video_id)
        #-----repost---#
        else:
            send_message_to_telegram_chat(TELEGRAM_CHAT_ID , 'bip bop I am a bot \n this is a repost')
    else:
        message_txt = message["message"]["text"]
        if regex_check(message_txt, reg = '^\/playlist$'):
            with open(list_PLAYLIST_ID, 'r') as f:
                payload = f.read()
                send_message_to_telegram_chat(TELEGRAM_CHAT_ID,text =f'beep bop I am a bot\n{YOTUBE_PLAYLIST_URL+payload}')
    