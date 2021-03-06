from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(update: Update, context: CallbackContext):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

def main():
    updater = Updater('5567007227:AAEbCNCSOj5fE0dGyxw4ZeVSpWV40n3qxok', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
