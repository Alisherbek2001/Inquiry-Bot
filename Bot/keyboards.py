from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Til lug'ati
LANGUAGES = {'🇺🇿 O\'zbekcha': 'uz', '🇬🇧 English': 'en', '🇷🇺 Русский': 'ru'}

# Tugmalar ro'yxatini yaratamiz
buttons = [
    KeyboardButton(text='🇺🇿 O\'zbekcha'),
    KeyboardButton(text='🇬🇧 English'),
    KeyboardButton(text='🇷🇺 Русский')
]

# Tugmalarni ReplyKeyboardMarkup ichida bir qatorda joylashtiramiz
language_keyboard = ReplyKeyboardMarkup(
    keyboard=[buttons],  # bu yerda keyboard maydoni to'ldirildi
    resize_keyboard=True,
    row_width=len(LANGUAGES)
)


region_buttons_uz = [
    "Chortoq tumani", "Chust tumani", "Kosonsoy tumani", "Mingbuloq tumani",
    "Namangan shahri", "Namangan tumani", "Norin tumani", "Pop tumani",
    "To'raqo'rg'on tumani", "Uchqo'rg'on tumani", "Uychi tumani", "Yangiqo'rgon tumani"
]
region_buttons_en = [
    "Chortoq district", "Chust district", "Kosonsoy district", "Mingbuloq district",
    "Namangan city", "Namangan district", "Norin district", "Pop district",
    "To'raqo'rg'on district", "Uchqo'rg'on district", "Uychi district", "Yangiqo'rgon district"
]
region_buttons_ru = [
    "Чартакский район", "Чустский район", "Косонсайский район", "Мингбулокский район",
    "город Наманган", "Наманганский район", "Нарынский район", "Папский район",
    "Туракурганский район", "Учкурганский район", "Уйчинский район", "Янгикурганский район"
]

province_buttons_uz = [
    "Andijon viloyati", "Buxoro viloyati", "Farg'ona viloyati", "Jizzax viloyati",
    "Xorazm viloyati", "Namangan viloyati", "Navoiy viloyati", "Qashqadaryo viloyati",
    "Qoraqalpog'iston Respublikasi", "Samarqand viloyati", "Sirdaryo viloyati", 
    "Surxondaryo viloyati", "Toshkent viloyati", "Toshkent shahri"
]


province_buttons_en = [
    "Andijan region", "Bukhara region", "Fergana region", "Jizzakh region",
    "Khorezm region", "Namangan region", "Navoi region", "Kashkadarya region",
    "Republic of Karakalpakstan", "Samarkand region", "Syrdarya region", 
    "Surkhandarya region", "Tashkent region", "Tashkent city"
]

province_buttons_ru = [
    "Андижанская область", "Бухарская область", "Ферганская область", "Джизакская область",
    "Хорезмская область", "Наманганская область", "Навоийская область", "Кашкадарьинская область",
    "Республика Каракалпакстан", "Самаркандская область", "Сырдарьинская область", 
    "Сурхандарьинская область", "Ташкентская область", "город Ташкент"
]

contact_button_uz = KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)
cancel_button_uz = KeyboardButton(text="❌ Bekor qilish")
another_button_uz = KeyboardButton(text="Boshqa")

contact_button_en = KeyboardButton(text="📞 Send phone number", request_contact=True)
cancel_button_en = KeyboardButton(text="❌ Cancel")
another_button_en = KeyboardButton(text="Another")

contact_button_ru = KeyboardButton(text="📞 Отправить номер телефона", request_contact=True)
cancel_button_ru = KeyboardButton(text="❌ Отмена")
another_button_ru = KeyboardButton(text="Другой")


contact_keyboard_uz = ReplyKeyboardMarkup(keyboard=[[contact_button_uz], [cancel_button_uz]], resize_keyboard=True)
region_keyboard_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=region_buttons_uz[i]), KeyboardButton(text=region_buttons_uz[i + 1])]
        for i in range(0, len(region_buttons_uz) - 1, 2)
    ] + [[cancel_button_uz]],
    resize_keyboard=True
)
province_buttons_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=province_buttons_uz[i]), KeyboardButton(text=province_buttons_uz[i + 1])]
        for i in range(0, len(province_buttons_uz) - 1, 2)
    ] + [[another_button_uz]],
    resize_keyboard=True
)


contact_keyboard_en = ReplyKeyboardMarkup(keyboard=[[contact_button_en], [cancel_button_en]], resize_keyboard=True)
region_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=region_buttons_en[i]), KeyboardButton(text=region_buttons_en[i + 1])]
        for i in range(0, len(region_buttons_en) - 1, 2)
    ] + [[cancel_button_en]],
    resize_keyboard=True
)
province_buttons_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=province_buttons_en[i]), KeyboardButton(text=province_buttons_en[i + 1])]
        for i in range(0, len(province_buttons_en) - 1, 2)
    ] + [[another_button_en]],
    resize_keyboard=True
)


contact_keyboard_ru = ReplyKeyboardMarkup(keyboard=[[contact_button_ru], [cancel_button_ru]], resize_keyboard=True)
region_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=region_buttons_ru[i]), KeyboardButton(text=region_buttons_ru[i + 1])]
        for i in range(0, len(region_buttons_ru) - 1, 2)
    ] + [[cancel_button_ru]],
    resize_keyboard=True
)
province_buttons_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=province_buttons_ru[i]), KeyboardButton(text=province_buttons_ru[i + 1])]
        for i in range(0, len(province_buttons_ru) - 1, 2)
    ] + [[another_button_ru]],
    resize_keyboard=True
)


confirm_buttons_uz = [[KeyboardButton(text="✅ Ha"), KeyboardButton(text="❌ Yo'q")]]
confirm_buttons_en = [[KeyboardButton(text="✅ Yes"), KeyboardButton(text="❌ No")]]
confirm_buttons_ru = [[KeyboardButton(text="✅ Да"), KeyboardButton(text="❌ Нет")]]


main_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📋 Murojaat yo\'llash'), KeyboardButton(text='🇺🇿 Tilni o\'zgartirish')]
    ],
    resize_keyboard=True
)

main_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📋 Submit Inquiry'), KeyboardButton(text='🇬🇧 Change Language')]
    ],
    resize_keyboard=True
)

main_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📋 Отправить запрос'), KeyboardButton(text='🇷🇺 Изменить язык')]
    ],
    resize_keyboard=True
)
