from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.client.bot import DefaultBotProperties
import asyncio
import os
from api import check_user,create_user,change_language
from keyboards import *

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

LANGUAGES = {'🇺🇿 O\'zbekcha': 'uz', '🇬🇧 English': 'en', '🇷🇺 Русский': 'ru'}

default_properties = DefaultBotProperties(parse_mode='HTML')
bot = Bot(token=TOKEN, default=default_properties)
dp = Dispatcher(storage=MemoryStorage())



TEXTS = {
    'uz': {
        'start': "Assalomu alaykum, siz murojaat botiga tashrif buyurdingiz! \nIltimos, tugmalardan birini tanlang:",
        'start_again': "Qaytganingizdan hursandmiz! \nIltimos, tugmalardan birini tanlang:",
        'enter_name': "Iltimos, F.I.Sh. ni kirting:",
        'enter_age': "Tug'ilgan kun oy yilingizni kiriting: ",
        'enter_contact': "Telefon raqamingizni yuboring:",
        'enter_region': "Qaysi tumandan murojaat yo'llayapsiz?",
        'enter_request': "Murojaatingizni kiriting:",
        'confirm': "Ma'lumotlarni tasdiqlaysizmi?",
        'data_submitted': "✅ Ma'lumotlaringiz muvaffaqiyatli yuborildi! \nIltimos, tugmalardan birini tanlang:",
        'data_cancelled': "Ma'lumotlaringiz bekor qilindi. \nIltimos, tugmalardan birini tanlang:",
        'process_cancelled': "Jarayon bekor qilindi. \nIltimos, tugmalardan birini tanlang:",
        'language_select': "Tilni tanlang:",
        'lang_buttons': ["O'zbekcha", "English", "Русский"],
        'full_name': 'F.I.Sh',
        'birth_date': "Tug'ilgan yil",
        'phone': 'Telefon',
        'region': 'Viloyat',
        'district':'Tuman',
        'request': 'Murojaat',
        'confirm': "Tasdiqlaysizmi?",
        'citizenship': "Chet el fuqarosi",
        'province':"Viloyatlardan birini tanlang. Agar siz tug'ilgan joy bu yerda yo'q bo'lsa, Boshqa tugmasini bosib kiritishingiz mumkin."
    },
    'en': {
        'start': "Hello, welcome to the inquiry bot! \nPlease choose one of the buttons:",
        'start_again': "We're glad you're back! \nPlease choose one of the buttons:",
        'enter_name': "Please enter your full name:",
        'enter_age': "Enter your birth date, month, and year: ",
        'enter_contact': "Please send your phone number:",
        'enter_region': "Which region are you submitting from?",
        'enter_request': "Enter your inquiry:",
        'confirm': "Do you confirm the details?",
        'data_submitted': "✅ Your information has been successfully submitted! \nPlease choose one of the buttons:",
        'data_cancelled': "Your information has been canceled. \nPlease choose one of the buttons:",
        'process_cancelled': "Process canceled. \nPlease choose one of the buttons:",
        'language_select': "Select your language:",
        'lang_buttons': ["O'zbekcha", "English", "Русский"],
        'full_name': 'Full Name',
        'birth_date': 'Year of birth',
        'phone': 'Phone',
        'region': 'Region',
        'district':'District',
        'request': 'Request',
        'confirm': "Do you confirm?",
        'citizenship':'Foreign citizen',
        'province':"Select one of the regions. If your place of birth is not listed here, you can press the 'Other' button to enter it."
        
    },
    'ru': {
        'start': "Здравствуйте, добро пожаловать в бот для запросов! \nПожалуйста, выберите одну из кнопок:",
        'start_again': "Мы рады, что вы вернулись! \nПожалуйста, выберите одну из кнопок:",
        'enter_name': "Пожалуйста, введите ваше полное имя:",
        'enter_age': "Введите вашу дату, месяц и год рождения:",
        'enter_contact': "Отправьте ваш номер телефона:",
        'enter_region': "Из какого региона вы отправляете запрос?",
        'enter_request': "Введите ваш запрос:",
        'confirm': "Подтверждаете ли вы информацию?",
        'data_submitted': "✅ Ваша информация успешно отправлена! \nПожалуйста, выберите одну из кнопок:",
        'data_cancelled': "Ваша информация отменена. \nПожалуйста, выберите одну из кнопок:",
        'process_cancelled': "Процесс отменен. \nПожалуйста, выберите одну из кнопок:",
        'language_select': "Выберите язык:",
        'lang_buttons': ["O'zbekcha", "English", "Русский"],
        'full_name': 'Ф.И.О',
        'birth_date': 'Год рождения',
        'phone': 'Телефон',
        'region': 'Регион',
        'district':'Округ',
        'request': 'Запрос',
        'confirm': "Вы подтверждаете?",
        'citizenship':'Иностранный гражданин',
        'province':"Выберите один из регионов. Если вашего места рождения здесь нет, вы можете нажать кнопку 'Другие' и ввести его."
    }
}

HELP_TEXTS = {
    'birth_date': {
        'uz': "Namuna: 15.05.2000",
        'en': "Example: 15.05.2000",
        'ru': "Пример: 15.05.2000"
    }}


class Form(StatesGroup):
    language = State()
    full_name = State()
    birth_date = State()
    contact = State()
    province = State()
    region = State()
    region = State()
    request = State()
    confirm = State()
    
class ChangeLanguageForm(StatesGroup):
    language_change = State() 
    
@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    result = check_user(telegram_id=telegram_id)
    if result.status_code == 200:
        language = result.json()['language']
        if language=='uz':
            main_button = main_button_uz
        elif language=='en':
            main_button = main_button_en
        else:
            main_button = main_button_ru
        await message.answer(TEXTS[result.json()['language']]['start_again'],reply_markup=main_button)
    else:
        await state.set_state(Form.language)
        await message.answer(TEXTS['uz']['language_select'], reply_markup=language_keyboard)

@dp.message(Form.language)
async def set_language(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    selected_lang = message.text
    lang_code = LANGUAGES.get(selected_lang)
    result = create_user(telegram_id=telegram_id,language=lang_code)
    if result==201:
        if lang_code:
            await state.update_data(language=lang_code)
            if lang_code=='uz':
                main_button = main_button_uz
            elif lang_code=='en':
                main_button = main_button_en
            else:
                main_button = main_button_ru
            await message.answer(TEXTS[lang_code]['start'], reply_markup=main_button)
            await state.set_state(Form.full_name)
        else:
            await message.answer(TEXTS['uz']['language_select'])
    else:
        await message.answer("Xatolik")
    
    
@dp.message(F.text.in_(["📋 Murojaat yo'llash", "📋 Submit Inquiry","📋 Отправить запрос"]))
async def cmd_murojaat(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    result = check_user(telegram_id=telegram_id)
    
    if result.status_code == 200:
        await state.update_data(language=result.json().get('language', 'uz'))
        
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    
    await state.set_state(Form.full_name)
    await message.answer(TEXTS[language]['enter_name'], reply_markup=ReplyKeyboardRemove())

@dp.message(Form.full_name)
async def enter_full_name(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    await state.update_data(full_name=message.text)
    await state.set_state(Form.birth_date)
    await message.answer(f"{TEXTS[language]['enter_age']}\n<i>{HELP_TEXTS['birth_date'][language]}</i>")

@dp.message(Form.birth_date)
async def enter_age(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    await state.update_data(birth_date=message.text)
    await state.set_state(Form.contact)
    if language == 'uz':
        contact_keyboard = contact_keyboard_uz
    elif language == 'en':
        contact_keyboard = contact_keyboard_en
    else:
        contact_keyboard = contact_keyboard_ru
    await message.answer(TEXTS[language]['enter_contact'], reply_markup=contact_keyboard)

@dp.message(Form.contact, F.content_type == "contact")
async def enter_contact(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    await state.update_data(contact=message.contact.phone_number)
    await state.set_state(Form.province)
    if language == 'uz':
        province_buttons = province_buttons_uz
    elif language == 'en':
        province_buttons = province_buttons_en
    else:
        province_buttons = province_buttons_ru
    await message.answer(TEXTS[language]['province'], reply_markup=province_buttons)

@dp.message(Form.province)
async def enter_province(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    others = {
        'uz':"Boshqa",
        'en':"Other",
        'ru':"Другой"
    }
    if  message.text == others[language]:
        await state.update_data(province=TEXTS[language]['citizenship'])
    else:
        await state.update_data(province=message.text)
    
    namangan_names = {
        'uz': "Namangan viloyati",
        'en': "Namangan region",
        'ru': "Наманганская область"
    }
    
    if message.text == namangan_names[language]:
        await state.set_state(Form.region)
        region_buttons = region_keyboard_uz if language == 'uz' else region_keyboard_en if language == 'en' else region_keyboard_ru
        await message.answer(TEXTS[language]['enter_region'], reply_markup=region_buttons)
        
    else:
        await state.set_state(Form.request)
        await message.answer(TEXTS[language]['enter_request'], reply_markup=ReplyKeyboardRemove())


@dp.message(Form.region, F.text.in_(region_buttons_uz + region_buttons_en + region_buttons_ru))
async def enter_region(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    await state.update_data(region=message.text)
    await state.set_state(Form.request)
    await message.answer(TEXTS[language]['enter_request'], reply_markup=ReplyKeyboardRemove())

    
@dp.message(Form.request)
async def enter_request(message: types.Message, state: FSMContext):
    await state.update_data(request=message.text)
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    if 'region' in user_data:
        confirmation_text = (
        f"👨‍💼 {TEXTS[language]['full_name']}: {user_data.get('full_name', 'N/A')}\n"
        f"🕑 {TEXTS[language]['birth_date']}: {user_data.get('birth_date', 'N/A')}\n"
        f"📞 {TEXTS[language]['phone']}: {user_data.get('contact', 'N/A')}\n"
        f"🌐 {TEXTS[language]['region']}: {user_data.get('province', 'N/A')}\n"
        f"📌 {TEXTS[language]['district']}: {user_data.get('region', 'N/A')}\n"
        f"📋 {TEXTS[language]['request']}: {user_data.get('request', 'N/A')}\n\n"
        f"{TEXTS[language]['confirm']}"
        )
    else:
        confirmation_text = (
        f"👨‍💼 {TEXTS[language]['full_name']}: {user_data.get('full_name', 'N/A')}\n"
        f"🕑 {TEXTS[language]['birth_date']}: {user_data.get('birth_date', 'N/A')}\n"
        f"📞 {TEXTS[language]['phone']}: {user_data.get('contact', 'N/A')}\n"
        f"🌐 {TEXTS[language]['region']}: {user_data.get('province', 'N/A')}\n"
        f"📋 {TEXTS[language]['request']}: {user_data.get('request', 'N/A')}\n\n"
        f"{TEXTS[language]['confirm']}"
        )
    await state.set_state(Form.confirm)
    if language == 'uz':
        confirm_keyboard = ReplyKeyboardMarkup(keyboard=confirm_buttons_uz, resize_keyboard=True)
    elif language == 'en':
        confirm_keyboard = ReplyKeyboardMarkup(keyboard=confirm_buttons_en, resize_keyboard=True)
    else:
        confirm_keyboard = ReplyKeyboardMarkup(keyboard=confirm_buttons_ru, resize_keyboard=True)
    await message.answer(confirmation_text, reply_markup=confirm_keyboard)



@dp.message(Form.confirm, F.text.in_(["✅ Ha", "✅ Yes","✅ Да"]))
async def process_confirm(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    telegram_username = message.from_user.username
    if 'region' in user_data:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=(f"<b>Yangi murojaat:</b>\n\n"
                f"👨‍💼 F.I.Sh: {user_data['full_name']}\n"
                f"🕑 Tug'ilgan yil: {user_data['birth_date']}\n"
                f"📞Telefon: {user_data['contact']}\n"
                f"📪 Telegram: @{telegram_username}\n"
                f"🌐 Viloyat: {user_data['province']}\n"
                f"📌 Tuman: {user_data['region']}\n"
                f"📋 Murojaat: {user_data['request']}"
                ),
        )
    else:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=(f"<b>Yangi murojaat:</b>\n\n"
                f"👨‍💼 F.I.Sh: {user_data['full_name']}\n"
                f"🕑 Tug'ilgan yil: {user_data['birth_date']}\n"
                f"📞Telefon: {user_data['contact']}\n"
                f"📪 Telegram: @{telegram_username}\n"
                f"🌐 Viloyat: {user_data['province']}\n"
                f"📋 Murojaat: {user_data['request']}"
                ),
            )
    if language=='uz':
            main_button = main_button_uz
    elif language=='en':
            main_button = main_button_en
    else:
            main_button = main_button_ru
    await message.answer(TEXTS[language]['data_submitted'], reply_markup=main_button)
    await state.clear()
 
 
@dp.message(Form.confirm, F.text.in_(["❌ Yo'q", "❌ No", "❌ Нет"]))
async def process_cancel(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    if language=='uz':
            main_button = main_button_uz
    elif language=='en':
            main_button = main_button_en
    else:
            main_button = main_button_ru
    await message.answer(TEXTS[language]['data_cancelled'], reply_markup=main_button)
    await state.clear()


@dp.message(F.text.in_(["❌ Bekor qilish", "❌ Cancel", "❌ Отмена"]))
async def cancel_process(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    result = check_user(telegram_id=telegram_id)
    
    language = 'uz'
    
    if result.status_code == 200:
        language = result.json().get('language', 'uz')
    if language=='uz':
            main_button = main_button_uz
    elif language=='en':
            main_button = main_button_en
    else:
            main_button = main_button_ru
    user_data = await state.get_data()
    language = user_data.get('language', 'uz')
    await message.answer(TEXTS[language]['process_cancelled'], reply_markup=main_button)
    await state.clear()


@dp.message(F.text.in_(["🇺🇿 Tilni o'zgartirish", "🇬🇧 Change Language", "🇷🇺 Изменить язык"]))
async def prompt_language_change(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    result = check_user(telegram_id=telegram_id)
    
    current_language = 'uz'
    
    if result.status_code == 200:
        current_language = result.json().get('language', 'uz')

    await message.answer(TEXTS[current_language]['language_select'], reply_markup=language_keyboard)
    await state.set_state(ChangeLanguageForm.language_change)

    
@dp.message(ChangeLanguageForm.language_change, F.text.in_(["🇺🇿 O'zbekcha", "🇬🇧 English", "🇷🇺 Русский"]))
async def handle_language_selection(message: types.Message, state: FSMContext):
    selected_language = None
    if message.text == "🇺🇿 O'zbekcha":
        selected_language = 'uz'
    elif message.text == "🇬🇧 English":
        selected_language = 'en'
    elif message.text == "🇷🇺 Русский":
        selected_language = 'ru'
    
    if selected_language=='uz':
        main_button = main_button_uz
    elif selected_language=='en':
        main_button = main_button_en
    else:
        main_button = main_button_ru
        
    if selected_language:
        telegram_id = message.from_user.id
        response = change_language(telegram_id, selected_language)
        
        if response.status_code == 200:
            await state.update_data(language=selected_language)
            
            confirmation_message = {
                'uz': "Til o'zgartirildi. \nTugmalardan birini tanlang!",
                'en': "Language changed. \nPlease choose one of the buttons!",
                'ru': "Язык изменен. \nПожалуйста, выберите одну из кнопок!"
            }.get(selected_language, "Language changed. Please choose one of the buttons!")
            
            
            await message.answer(confirmation_message, reply_markup=main_button)
        else:
            error_messages = {
                'uz': "Tilni o'zgartirishda xato yuz berdi. \nTugmalardan birini tanlang!",
                'en': "An error occurred while changing the language. \nPlease choose one of the buttons!",
                'ru': "Произошла ошибка при изменении языка. \nПожалуйста, выберите одну из кнопок!"
            }.get(selected_language,"An error occurred while changing the language. \nPlease choose one of the buttons!")

            await message.answer(error_messages, reply_markup=main_button)
    
    await state.clear()


@dp.message()
async def echo(message:types.Message):
    telegram_id = message.from_user.id
    result = check_user(telegram_id=telegram_id)
    if result.status_code == 200:
        language = result.json()['language']
        error_message = {
            'uz': 'Kechirasiz, bunday buyruq bizda mavjud emas. \nIltimos, tugmalardan birini tanlang!',
            'en': 'Sorry, this command does not exist in our system. \nPlease select one of the buttons!',
            'ru': 'Извините, такая команда у нас не существует. \nПожалуйста, выберите одну из кнопок!'
        }

        if language=='uz':
            main_button = main_button_uz
        elif language=='en':
            main_button = main_button_en
        else:
            main_button = main_button_ru
        await message.answer(error_message[language],reply_markup=main_button)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
