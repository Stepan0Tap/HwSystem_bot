# <---------- Импорт функций Aiogram ---------->
from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


# <---------- Reply клавиатуры ---------->
btn_reply_CommandStartOrHelp_0 = KeyboardButton(text='📝 Домашнее задание')
btn_reply_CommandStartOrHelp_1 = KeyboardButton(text='📋 Расписание')
btn_reply_CommandStartOrHelp_2 = KeyboardButton(text='📌 События')
btn_reply_CommandStartOrHelp_3 = KeyboardButton(text='👥 Группа')
btn_reply_CommandStartOrHelp_4 = KeyboardButton(text='⚙️ Помощь')
kb_reply_CommandStartOrHelp = ReplyKeyboardMarkup(
	keyboard=[
		[btn_reply_CommandStartOrHelp_0],
		[btn_reply_CommandStartOrHelp_1, btn_reply_CommandStartOrHelp_2],
		[btn_reply_CommandStartOrHelp_3, btn_reply_CommandStartOrHelp_4]
	],
	resize_keyboard=True
)


btn_reply_CancelRegistration = KeyboardButton(text='❌ Отмена')
kb_reply_CancelRegistration = ReplyKeyboardMarkup(
	keyboard=[[btn_reply_CancelRegistration]],
	resize_keyboard=True
)


# <---------- Inline клавиатуры ---------->
btn_inline_GroupPanel = InlineKeyboardButton(text='👥 Группа', callback_data='GroupPanel')
kb_inline_GroupPanel = InlineKeyboardMarkup(
	inline_keyboard=[[btn_inline_GroupPanel]]
)


btn_inline_EnterGroup = InlineKeyboardButton(text='💼 Войти', callback_data='EnterGroup')
btn_inline_CreateGroup = InlineKeyboardButton(text='📝 Создать', callback_data='CreateGroup')
kb_inline_GroupNoMemberPanel = InlineKeyboardMarkup(
	inline_keyboard=[
		[btn_inline_EnterGroup],
		[btn_inline_CreateGroup]
	]
)


btn_inline_LeaveGroup = InlineKeyboardButton(text='🚪 Выйти', callback_data=f'LeaveGroup')
kb_inline_GroupMemberPanel = InlineKeyboardMarkup(
	inline_keyboard=[[btn_inline_LeaveGroup]]
)


btn_inline_DeleteGroup = InlineKeyboardButton(text='🚪 Удалить', callback_data=f'DeleteGroup')
btn_inline_ChangeOwner = InlineKeyboardButton(text='🔑 Передать права', callback_data=f'ChangeOwner')
kb_inline_GroupOwnerPanel = InlineKeyboardMarkup(
	inline_keyboard=[
		[btn_inline_DeleteGroup],
		[btn_inline_ChangeOwner]
	]
)
