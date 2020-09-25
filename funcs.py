# Functions...


def On(chat_id):
    import telepot
    from credentials import bot_token
    import stickers as st
    import time
        
    token = bot_token
    bot = telepot.Bot(token)

    bot.sendSticker(chat_id, st.sbot_offline)
    time.sleep(1.5)
    bot.sendMessage(chat_id, "*Online*", parse_mode= 'Markdown')


def Bot():
    
    import telepot
    from credentials import bot_token
        
    token = bot_token
    bot = telepot.Bot(token)
    
    return bot
  
def Start(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    
    global bot
    bot = Bot()

    
    bot.sendSticker(chat_id, st.sbot_back)
    time.sleep(3)
    
    bot.sendSticker(chat_id, st.sbot_hello)
    time.sleep(2)
    
    show_keyboard = ReplyKeyboardMarkup(keyboard=[["Português"],["English"]],
                                        resize_keyboard = True, one_time_keyboard = True)
    
    bot.sendMessage(chat_id, ms.lang, reply_markup=show_keyboard)



def Portuguese(chat_id, f_name):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    
    time.sleep(2)
    bot.sendSticker(chat_id, st.sbot_force)
    time.sleep(0.5)
    bot.sendMessage(chat_id, "Só um momento enquanto uso a força pra descobrir o seu nome...")
    time.sleep(5)
    
    # Welcome msg...
    bot.sendMessage(chat_id, ms.boasVindas.format(f_name), parse_mode= 'Markdown')
    time.sleep(6)
    show_keyboard = ReplyKeyboardMarkup(keyboard=[["Sim"],["Não"]],
                                        resize_keyboard = True, one_time_keyboard = True)
    
    bot.sendMessage(chat_id, ms.decisao, reply_markup=show_keyboard)

    
def Prosseguir(chat_id):

    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    

    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_looking)
    time.sleep(0.5)
    bot.sendMessage(chat_id, ms.looking, parse_mode= 'Markdown')
    time.sleep(4)
    show_keyboard = ReplyKeyboardMarkup(keyboard=[["WhatsApp"],
                                                  ["Telegram"],
                                                  ["Gmail"], 
                                                  ["Currículo"], 
                                                  ["LinkedIn"],
                                                  ["GitHub"],
                                                  ["Encerrar"]], resize_keyboard = True,
                                        one_time_keyboard = True)
        
    bot.sendMessage(chat_id, ms.opcao, parse_mode= 'Markdown', reply_markup=show_keyboard)

def PWhats(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="WhatsApp",
                                                                                     url="http://api.whatsapp.com/send?1=pt_BR&phone=5571988036786")]])
    bot.sendMessage(chat_id, ms.ptwhats, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def PTelegram(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Telegram",
                                                                                     url="https://t.me/FelipeSolares")]])
    bot.sendMessage(chat_id, ms.ptwhats, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def PGmail(chat_id):
    
    import time
    import msgs as ms
    import stickers as st

    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    bot.sendMessage(chat_id, ms.pgmail, parse_mode= 'Markdown')
    time.sleep(0.5)
    bot.sendMessage(chat_id, ms.email, parse_mode= 'Markdown')
    
def PCurriculo(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Currículo",
                                                                                     url="https://drive.google.com/file/d/1tFmMFN8obTXvZ3Bti_56zkKvP4xNTvIK/view?usp=sharing")]])
    bot.sendMessage(chat_id, ms.pcurriculo, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def PLinked(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="LinkedIn",
                                                                                     url="https://www.linkedin.com/in/felipesolares/")]])
    bot.sendMessage(chat_id, ms.plinked, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def PGit(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.pthreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="GitHub",
                                                                                     url="https://github.com/fsolares/professional-portfolio")]])
    bot.sendMessage(chat_id, ms.pgit, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)

def PEncerrar(chat_id):
    
    import time
    import msgs as ms
    import stickers as st

    
    bot.sendSticker(chat_id, st.sbot_conq)
    time.sleep(1.5)
    bot.sendMessage(chat_id, ms.pconquista, parse_mode= 'Markdown')
    time.sleep(2)
    bot.sendMessage(chat_id, ms.xau, parse_mode= 'Markdown')
    
def NProsseguir(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    
    
    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_spit)
    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_nope)
    time.sleep(4)
    bot.sendMessage(chat_id, ms.brincadeira, parse_mode= 'Markdown')
    time.sleep(6)
    bot.sendSticker(chat_id, st.sbot_thumbsup)
    time.sleep(3)
    bot.sendMessage(chat_id, ms.xau, parse_mode= 'Markdown')



def English(chat_id, f_name):

    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    
    time.sleep(2)
    bot.sendSticker(chat_id, st.sbot_force)
    time.sleep(0.5)
    bot.sendMessage(chat_id, "Just a moment while I use the Force to discover your name...")
    time.sleep(5)
    
    # Welcome msg...
    bot.sendMessage(chat_id, ms.welcome.format(f_name), parse_mode= 'Markdown')
    time.sleep(6)
    show_keyboard = ReplyKeyboardMarkup(keyboard=[["Yes"],["No"]],
                                        resize_keyboard = True, one_time_keyboard = True)
    
    bot.sendMessage(chat_id, ms.decision, reply_markup=show_keyboard)

def Proceed(chat_id):

    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    

    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_looking)
    time.sleep(0.5)
    bot.sendMessage(chat_id, ms.searching, parse_mode= 'Markdown')
    time.sleep(4)
    show_keyboard = ReplyKeyboardMarkup(keyboard=[["Msg to WhatsApp"],
                                                  ["Msg to Telegram"],
                                                  ["Msg to Gmail"], 
                                                  ["Open Resume"], 
                                                  ["Open LinkedIn"],
                                                  ["Open GitHub"],
                                                  ["End"]], resize_keyboard = True,
                                        one_time_keyboard = True)
        
    bot.sendMessage(chat_id, ms.option, parse_mode= 'Markdown', reply_markup=show_keyboard)

def EWhats(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="WhatsApp",
                                                                                     url="http://api.whatsapp.com/send?1=pt_BR&phone=5571988036786")]])
    bot.sendMessage(chat_id, ms.ewhats, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def ETelegram(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Telegram",
                                                                                     url="https://t.me/FelipeSolares")]])
    bot.sendMessage(chat_id, ms.ewhats, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def EGmail(chat_id):
    
    import time
    import msgs as ms
    import stickers as st

    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    bot.sendMessage(chat_id, ms.egmail, parse_mode= 'Markdown')
    time.sleep(0.5)
    bot.sendMessage(chat_id, ms.email, parse_mode= 'Markdown')
    
def ECurriculo(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Resume",
                                                                                     url="https://drive.google.com/file/d/1K0Ax5bFcQOcPNVzEs8fRFubcYdD2FlxV/view?usp=sharing")]])
    bot.sendMessage(chat_id, ms.ecurriculo, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def ELinked(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="LinkedIn",
                                                                                     url="https://www.linkedin.com/in/felipesolares/")]])
    bot.sendMessage(chat_id, ms.elinked, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)
    
def EGit(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    
    time.sleep(0.5)
    bot.sendSticker(chat_id, st.sbot_threat)
    time.sleep(1)
    bot.sendMessage(chat_id, ms.ethreat, parse_mode= 'Markdown')
    
    time.sleep(1.5)
    show_inlinekeyboard =InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="GitHub",
                                                                                     url="https://github.com/fsolares/professional-portfolio")]])
    bot.sendMessage(chat_id, ms.egit, parse_mode= 'Markdown', reply_markup=show_inlinekeyboard)

def End(chat_id):
    
    import time
    import msgs as ms
    import stickers as st

    
    bot.sendSticker(chat_id, st.sbot_conq)
    time.sleep(1.5)
    bot.sendMessage(chat_id, ms.conquer, parse_mode= 'Markdown')
    time.sleep(2)
    bot.sendMessage(chat_id, ms.bye, parse_mode= 'Markdown')
    
def NProceed(chat_id):
    
    import time
    import msgs as ms
    import stickers as st
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    
    
    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_spit)
    time.sleep(1)
    bot.sendSticker(chat_id, st.sbot_nope)
    time.sleep(4)
    bot.sendMessage(chat_id, ms.kidding, parse_mode= 'Markdown')
    time.sleep(6)
    bot.sendSticker(chat_id, st.sbot_thumbsup)
    time.sleep(3)
    bot.sendMessage(chat_id, ms.bye, parse_mode= 'Markdown')
