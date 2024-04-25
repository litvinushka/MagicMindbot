from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

class Rb:
    main=ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Обо мне'),
          KeyboardButton(text='Терапия')],
        [KeyboardButton(text='Обучение')]
        ],
        resize_keyboard=True)
    
    admin=ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Рассылка")]
        ],
        resize_keyboard=True)
    
class Ib:
    about=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
        text='Instagram', 
        url='https://github.com/litvinushka/t3DS')]
        ]) 
    
    education=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Кому это нужно?", callback_data="education_1")],
        [InlineKeyboardButton(text="Что вы приобретете?", callback_data="education_2")]
        ])
    
    education_1=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Что изменится в вашей жизни?",callback_data="education_3")],
        [InlineKeyboardButton(text="Назад", callback_data='back_1')]
        ])
    
    education_2=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Программа обучения ", callback_data="education_2_1")],
        [InlineKeyboardButton(text="Как проходит обучение?", callback_data="education_2_2")],
        [InlineKeyboardButton(text="Записаться", callback_data='app')],
        [InlineKeyboardButton(text="Назад", callback_data='back_1')]
        ])

    education_3=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Что вы приобретете?',callback_data='education_2')]])
    
    education_2_1=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Структура урока',callback_data='education_2_1_1')],
        [InlineKeyboardButton(text="Записаться",callback_data="app")],
        [InlineKeyboardButton(text="Назад", callback_data="back_1")]
    ])

    education_2_1_1=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Записаться",callback_data="app")],
        [InlineKeyboardButton(text="Назад", callback_data="back_1")]
    ])

    education_2_2=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Записаться",callback_data="app")],
        [InlineKeyboardButton(text="Назад", callback_data="back_1")]
    ])

    therapy=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Кому подойдет терапия?",callback_data='about_therapy')]
    ])

    about_therapy=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Записаться',callback_data='app')],
        [InlineKeyboardButton(text='Назад',callback_data='back_2')]
    ])