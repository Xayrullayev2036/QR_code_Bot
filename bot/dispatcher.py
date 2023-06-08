from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv()

API_Token = os.environ["Token"]
# PROXY = "http://proxy.server:3128"
bot = Bot(token=API_Token)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
