import html
import json
import os
import psutil
import random
import time
import datetime
from typing import Optional, List
import re
import requests
from telegram.error import BadRequest
import lucifer.modules.helper_funcs.cas_api as cas
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from lucifer.modules.helper_funcs.chat_status import user_admin, is_user_admin
from lucifer import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, DEV_USERS
from lucifer.__main__ import STATS, USER_INFO, TOKEN
from lucifer.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler
from lucifer.modules.helper_funcs.extraction import extract_user
from lucifer.modules.helper_funcs.filters import CustomFilters
import lucifer.modules.sql.users_sql as sql

@run_async
def info(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    chat = update.effective_chat
    user_id = extract_user(update.effective_message, args)

    if user_id:
        user = bot.get_chat(user_id)

    elif not message.reply_to_message and not args:
        user = message.from_user

    elif not message.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not message.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        message.reply_text("I can't extract a user from this.")
        return

    else:
        return
    
    text = (f"<b>User Information:</b>\n"
            f"ID: <code>{user.id}</code>\n"
            f"Name: {html.escape(user.first_name)}")

    if user.last_name:
        text += f"\nLast Name: {html.escape(user.last_name)}"

    if user.username:
        text += f"\nUsername: @{html.escape(user.username)}"

    text += f"\nPermanent user link: {mention_html(user.id, 'link')}"

    num_chats = sql.get_user_num_chats(user.id)
    text += f"\nChat count: <code>{num_chats}</code>"
    text += "\nNumber of profile pics: {}".format(bot.get_user_profile_photos(user.id).total_count)
   
    try:
        user_member = chat.get_member(user.id)
        if user_member.status == 'administrator':
            result = requests.post(f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={chat.id}&user_id={user.id}")
            result = result.json()["result"]
            if "custom_title" in result.keys():
                custom_title = result['custom_title']
                text += f"\n🛡This user holds the title <b>{custom_title}</b> here."
    except BadRequest:
        pass

   

    if user.id == OWNER_ID:
        text += "\nThis person is my owner - I would never do anything against them!."
    else:
        if user.id == int(254318997):
            text += "\nThis person is owner of my Mother Mrs Haruka Aya because of her and him I am Alive Now Thanks a Lot ❤!."
        
        elif user.id in DEV_USERS:
              text += "\nThis person is my dev - I would never do anything against them!."
        
        elif user.id in SUDO_USERS:
              text += "\nThis person is one of my sudo users! " \
                              "Nearly as powerful as my owner - so watch it.."
        
        elif user.id in SUPPORT_USERS:
              text += "\nThis person is one of my support users! " \
                             "Not quite a sudo user, but can still gban you off the map."
        
  
       
        elif user.id in WHITELIST_USERS:
              text += "\nThis person has been whitelisted! " \
                             "That means I'm not allowed to ban/kick them."
    


    text +="\n"
    text += "\nCAS banned: "
    result = cas.banchecker(user.id)
    text += str(result)
    for mod in USER_INFO:
        if mod.__mod_name__ == "Users":
            continue

        try:
            mod_info = mod.__user_info__(user.id)
        except TypeError:
            mod_info = mod.__user_info__(user.id, chat.id)
        if mod_info:
            text += "\n" + mod_info
    try:
        profile = bot.get_user_profile_photos(user.id).photos[0][-1]
        bot.sendChatAction(chat.id, "upload_photo")
        bot.send_photo(chat.id, photo=profile, caption=(text), parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    except IndexError:
        update.effective_message.reply_text(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

INFO_HANDLER = DisableAbleCommandHandler("info", info, pass_args=True)
dispatcher.add_handler(INFO_HANDLER)    
