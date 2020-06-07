import random

from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.ext import CommandHandler, run_async

import lucifer.modules.helper_funcs.fun_strings as fun_strings
from lucifer import dispatcher
from lucifer.modules.disable import DisableAbleCommandHandler

@run_async
def pro(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.PRO_STRINGS)) 
    
    
@run_async
def pubg(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("PUBG Chutiyo ka Game! Be lyk moi Use Tik-Tok and become Chakka")
    
    
@run_async
def tiktok(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("Bulati Hai Magar Janeka Nhi...! ")
    
           
@run_async
def rape(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.RAPE_STRINGS)) 
    
    
@run_async 
def thanos(bot: Bot, update: Update): 
    update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.THANOS_STRINGS))
    
    
@run_async 
def chu(bot: Bot, update: Update):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.CHU_STRINGS)) 

__help__ = """
 - /pro: this is only for peru peeps not for u kek.
 - /thanos: use only when u need thanos to kill anyone.
 - /chu: abuses chu peeps for u.
 - /pubg: Try Yourself!
 - /tiktok: Try Yourself!
 - /rape: Try Yourself!
"""

__mod_name__ = "Fun"

PRO_HANDLER = DisableAbleCommandHandler("pro", pro, admin_ok=True)
THANOS_HANDLER = DisableAbleCommandHandler("thanos", thanos, admin_ok=True)
CHU_HANDLER = DisableAbleCommandHandler("chu", chu, admin_ok=True)
RAPE_HANDLER = DisableAbleCommandHandler("rape", rape, admin_ok=True)
PUBG_HANDLER = DisableAbleCommandHandler("pubg", pubg, admin_ok=True)
TIKTOK_HANDLER = DisableAbleCommandHandler("tiktok", tiktok, admin_ok=True)

dispatcher.add_handler(PRO_HANDLER)
dispatcher.add_handler(THANOS_HANDLER)
dispatcher.add_handler(CHU_HANDLER)
dispatcher.add_handler(PUBG_HANDLER)
dispatcher.add_handler(TIKTOK_HANDLER)
dispatcher.add_handler(RAPE_HANDLER)

__command_list__ = ["pro", "thanos", "chu", "rape", "pubg", "tiktok"]
__handlers__ = [PRO_HANDLER, THANOS_HANDLER, CHU_HANDLER, PUBG_HANDLER, TIKTOK_HANDLER, RAPE_HANDLER]
