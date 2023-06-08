from aiogram import executor
from dispatcher import dp
from handler.start import *
from handler.create_qrcod import *
import logging



if __name__ == '__main__':
    logging.basicConfig(level =logging.INFO )
    executor.start_polling(dp,skip_updates=True)
