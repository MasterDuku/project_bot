from aiogram.utils import executor
from create_bot import dp

from handlers import client, admin, other

client.register_heandlers_client(dp)
other.register_heandlers_other(dp)

async def on_startup(_):
    print('--'*4,'Bot started', '--'*4)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


print('--'*4, 'Отработал нормально', '--'*4)
