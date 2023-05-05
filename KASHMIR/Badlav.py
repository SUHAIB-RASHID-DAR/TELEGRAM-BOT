from pyrogram import Client, filters
import os



# Specify the download directory
download_dir = '/path/to/download/dir/'


# Define a function to handle incoming messages
@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
def rename_media(bot, message):
    # Get the media file
    media = message.media
    # Get the original file name
    orig_file_name = media.document.file_name
    # Ask the user for a new file name
    bot.send_message(chat_id=message.chat.id, text='Enter a new name for the file:')
    # Wait for the user's response
    new_file_name = client.listen(message.chat.id)
    # Rename the file
    try:
        media.download(file_name=os.path.join(download_dir, orig_file_name), progress=progress_callback)
        os.rename(os.path.join(download_dir, orig_file_name), os.path.join(download_dir, new_file_name))
        bot.send_message(chat_id=message.chat.id, text=f'The file has been renamed to {new_file_name}.')
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f'An error occurred: {e}')
    

# Define a function to track the download progress
def progress_callback(current, total):
    progress = (current / total) * 100
    bot.send_message(chat_id=message.chat.id, text=f'Download progress: {progress:.2f}%')



