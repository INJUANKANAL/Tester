from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

mainmenu__button_1 = KeyboardButton('🛒 My stores')
mainmenu__button_2 = KeyboardButton('🔓 Personal Area')

mainmenu__kb = ReplyKeyboardMarkup(resize_keyboard=True).add(mainmenu__button_1, mainmenu__button_2)

account__button_1 = KeyboardButton('💰 Withdraw')
account__button_2 = KeyboardButton('◀ Back')

account__kb = ReplyKeyboardMarkup(resize_keyboard=True).add(account__button_1, account__button_2)

control_panel__button_1 = KeyboardButton('📦 Categories')
control_panel__button_2 = KeyboardButton('🎈 Goods')
control_panel__button_3 = KeyboardButton('⚙ Tech Support')
control_panel__button_4 = KeyboardButton('👥 Referral system')
control_panel__button_5 = KeyboardButton('📃 Current coupon')
control_panel__button_6 = KeyboardButton('❌ Delete store')
control_panel__button_7 = KeyboardButton('✏️ Change name')
control_panel__button_8 = KeyboardButton('⏯ Start/Stop')
control_panel__button_9 = KeyboardButton('✉️ Newsletter')
control_panel__button_10 = KeyboardButton('◀ Back')

control_panel__kb = ReplyKeyboardMarkup(resize_keyboard=True).add(control_panel__button_1, control_panel__button_2, control_panel__button_3, control_panel__button_4, control_panel__button_5, control_panel__button_6, control_panel__button_7, control_panel__button_8, control_panel__button_9, control_panel__button_10)
