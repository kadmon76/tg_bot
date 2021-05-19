import re
TELEGRAM_TOKEN= '1735520343:AAGsQ-7Uj4HS2nmQMNyDYx7G_j38ANUWarQ'

TELEGRAM_CHAT_ID = '896664897'

YOUTUBE_REGEX = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})')
#change root file when mooving to server!!!
YOTUBE_PLAYLIST_URL = 'https://www.youtube.com/playlist?list='
LIST_OF_VIDEOS_IDS = 'list_of_videos_ids.txt'
YOUTUBE_LINKS_PATH        = r'C:\yaron\python\telegram_bot\bot2\youtube_links.txt' 
#change root file when mooving to server!!!
JSON_TELEGRAM_file = 'telegram_message.json'
#change root file when mooving to server!!!
list_PLAYLIST_ID = 'playlist_ids.txt'
youtube_id = ''


#https://api.telegram.org/bot1735520343:AAGsQ-7Uj4HS2nmQMNyDYx7G_j38ANUWarQ/setWebhook?url=https://dc18dc0da46a.ngrok.io
# https://api.telegram.org/bot1390583042:AAF13Dnxv0CxzrK-3mEn3BsNIkQG_hd2qdM/deleteWebhook?url=https://yaronl.com