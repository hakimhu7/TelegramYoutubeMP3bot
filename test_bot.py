from unittest.mock import MagicMock
from bot import handle_text

def test_handle_text_with_youtube_link():

    message = MagicMock()
    message.text = "https://www.youtube.com/watch?v=cSLAO7zxS2M&ab_channel=gootmusic"
    message.chat.id = 123456789
    # Call the function under test
    handle_text(message)

    # Assert that the bot replies with a processing message
    message.reply_to.assert_called_once_with(message, "Your file is being processed!")

    # Assert that the bot sends the audio file
    message.bot.send_audio.assert_called_once_with(message.chat.id, audio_file)

    # Assert that the bot sends the enjoy message
    message.reply_to.assert_called_with(message, "Enjoy!")
