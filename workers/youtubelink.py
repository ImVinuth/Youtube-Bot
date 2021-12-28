"""

███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗██████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔══██╗╚══██╔══╝╚██╗██╔╝
██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║█████╗╚██╗░██╔╝██████╔╝░░░██║░░░░╚███╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║╚════╝░╚████╔╝░██╔══██╗░░░██║░░░░██╔██╗░
██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝░░░░░░░░╚██╔╝░░██║░░██║░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["youtubelink"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bots Channel", url="https://t.me/Vinuth_BOTs")],
        [InlineKeyboardButton("Developer", url="https://t.me/VinuthPMBot")],
        [InlineKeyboardButton("BotsList", url="https://t.me/j")],
        [InlineKeyboardButton("Leech & Mirror", url="https://t.me/l")],
        [InlineKeyboardButton("Movies & Demand", url="https://t.me/g")]
    ])
    youtube_ex = f"""
**Some example youtube channels and songs if you don't know then what u want**
- type /github if I helped u in AnyWay. 
```Pʀᴇᴅ∆ᴛᴏʀ``` """

   
    
    await message.reply_text(youtube_ex, reply_markup=joinButton)
    raise StopPropagation






