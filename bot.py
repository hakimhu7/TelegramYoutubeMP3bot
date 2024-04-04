import telebot
from pytube import *
from moviepy.editor import *


BOT_TOKEN =  YOUR_BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, Enter a YouTube link to start your MP3 download!")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    received_text = message.text
    print("Received text:", received_text)
    
    # Check if the received text is a valid YouTube link
    if 'youtube.com' in received_text or 'youtu.be' in received_text:
        try:
            yt = YouTube(received_text)
            file_path = yt.streams.first().download()
            processing_text = "Your file is being processed!"
            bot.send_message(message.chat.id, processing_text)

            video = VideoFileClip(file_path)
            mp3_file_path = file_path.replace('.mp4', '.mp3')
            video.audio.write_audiofile(mp3_file_path)

            with open(mp3_file_path, 'rb') as audio_file:
                bot.send_audio(message.chat.id, audio_file)
                bot.reply_to(message, "Enjoy!")
        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
    else:
        bot.reply_to(message, "Please enter a valid YouTube link.")

# Start the bot polling
bot.polling()
