from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnWork = KeyboardButton(text="/Режим_работы")
btnLocation = KeyboardButton(text="/Расположение")
btnMenu = KeyboardButton(text="/Меню")

mainMenuClient = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
mainMenuClient.add(btnWork, btnLocation, btnMenu)
"""
варианты расположения кнопок в пользовательском окне
"""
# mainMenuClient.add(btnWork).add(btnLocation).add(btnMenu)
# mainMenu.row(btnWork, btnLocation, btnMenu)
# mainMenu.insert(btnWork, btnLocation, btnMenu)
# mainMenu.row(btnWork, btnLocation).insert(btnMenu)

"""
 from aiogram.types import ReplyKeyboardRemove - удаляет клавиатуру и вернуть не получится
вызов там где необходимо - reply_markup=ReplyKeyboardRemove
"""