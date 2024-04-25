from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import services.keyboard as kb
import services.data as data
from services.db import Database
from services import config

router=Router()
db=Database('services/database.db')
#Start
@router.message(CommandStart())    
async def cmd_start(message:Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        keyboard = kb.Rb.main
        if str(message.from_user.id)==config.admin_id:
            keyboard = kb.Rb.admin

        await message.reply(text=data.main_message, reply_markup=keyboard)

#About me
@router.message(F.text=='Обо мне') 
async def about(message: Message):

   
    await message.reply(
        text=data.about,
        reply_markup=kb.Ib.about
        )
    
#Therapy
@router.message(F.text=='Терапия') 
async def therapy(message: Message):
    await message.reply(text=data.therapy,reply_markup=kb.Ib.therapy)

#Education
@router.message(F.text=='Обучение') 
async def education(message: Message):

    
    await message.reply(
        text=data.education,
        reply_markup=kb.Ib.education) 

#Кому это нужно
@router.callback_query(lambda query: query.data == "education_1") 
async def education_1(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=data.education_1, 
        reply_markup=kb.Ib.education_1
        )

#Что вы приобретете?
@router.callback_query(lambda query: query.data == "education_2")
async def education_2(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=data.education_2,
        reply_markup=kb.Ib.education_2
        )
    
#Что изменится в вашей жизни?
@router.callback_query(lambda query: query.data=='education_3')
async def education_3(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=data.education_3,
        reply_markup=kb.Ib.education_3
    )

#   Программа обучения  
@router.callback_query(lambda query: query.data == "education_2_1")
async def education_2_1(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=data.education_2_1,
        reply_markup=kb.Ib.education_2_1
    )

#Как проходит обучение?
@router.callback_query(lambda query: query.data == "education_2_2")
async def education_2_2(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=data.education_2_2,
        reply_markup=kb.Ib.education_2_2
    )

#Назад Обучение
@router.callback_query(lambda query: query.data=="back_1")
async def back_1(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(text=data.education)
    await callback_query.message.edit_reply_markup(
        reply_markup=kb.Ib.education
        )

#Назад Терапия
@router.callback_query(lambda query: query.data=='back_2')
async def back_2(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(text=data.therapy)
    await callback_query.message.edit_reply_markup(reply_markup=kb.Ib.therapy)

#Кому подойдет терапия?
@router.callback_query(lambda query: query.data=='about_therapy')
async def about_therapy(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(text=data.about_therapy)
    await callback_query.message.edit_reply_markup(
        reply_markup=kb.Ib.about_therapy
    )

#Структура урока
@router.callback_query(lambda query: query.data=='education_2_1_1')
async def education_2_1_1(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(text=data.education_2_1_1)
    await callback_query.message.edit_reply_markup(reply_markup=kb.Ib.education_2_1_1)



#Записаться
class App(StatesGroup):
    name = State()
    number = State()

@router.callback_query(lambda query: query.data=='Записаться')
async def app_1(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(App.name)
    await callback_query.message.answer("Введите ваше имя")

@router.message(App.name)
async def app_2(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(App.number)
    await message.answer("Введите номер телефона")

@router.message(App.number)
async def app_3(message:Message, state: FSMContext):
    await state.update_data(number=message.text)
    data=await state.get_data()
    name = data.get("name")
    number = data.get("number")
    await message.answer(f"Благодарю, {name}, мы свяжемся с вами в ближайшее время")
    admin_message = f"Новая заявка!\n\nИмя: {name}\nНомер телефона: {number}"
    await state.clear()
    await message.bot.send_message(config.admin_id, admin_message)


#Рассылка
class Mailing(StatesGroup):
    mail=State()

@router.message(F.text=='Рассылка')
async def mailing(message: Message, state: FSMContext):
    await state.set_state(Mailing.mail) 
    await message.answer("Введите текст рассылки")

@router.message(Mailing.mail)
async def sending(message: Message, state: FSMContext):
    await state.update_data(mail=message.text)
    data = await state.get_data()
    print("Data from state:", data)
    mailing_message = data.get('mail')
    print("Mailing message:", mailing_message)

    users = db.get_users()

    for user_id, active in users:
        try:
            await message.bot.send_message(user_id, mailing_message)
            if int(active)!=1:
                db.set_active(user_id,1)

        except Exception as e:
            db.set_active(user_id,0)
            print(f"Ошибка при отправке сообщения пользователю: {e}")

    await message.answer("Рассылка успешно отправлена всем пользователям.")
    await state.clear()