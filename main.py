import discord
from discord.ext import commands
import time
import os
import asyncio
from host.server import server

server()

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
async def main():
    print(bcolors.WARNING + '                      MODULE' + bcolors.ENDC)
    print('═══════════════════════════════════════════════════')
    commands = os.listdir('command')
    for command in commands:
        if (command == '__pycache__' or command == 'random_list' or command == "data.json" or command == "cache"):
            pass
        else:
            try:
                await bot.load_extension(f"command.{command[:-3]}")
                print(bcolors.OKGREEN +f'[HỆ THỐNG]'+bcolors.FAIL+f"[✅]"+bcolors.OKBLUE + f' Load thành công module {command[:-3]}'+bcolors.ENDC)
                time.sleep(0.025)
            except Exception as e:
                print(bcolors.OKGREEN +f'[HỆ THỐNG]'+bcolors.FAIL+f"[❌]"+bcolors.OKBLUE + f' Load thất bại module {command[:-3]}'+bcolors.FAIL+f"["+bcolors.WARNING+f"{e}"+bcolors.FAIL+"]"+bcolors.ENDC)
    print('═════════════════════════════════════════════════════')
    print(bcolors.WARNING + '                      EVENT' + bcolors.ENDC)
    print('═════════════════════════════════════════════════════')
    for command in os.listdir("./event"):
        if (command == '__pycache__' or command == 'random_list' or command == "data.json"):
            pass
        else:
            try:
                await bot.load_extension(f"event.{command[:-3]}")
                print(bcolors.OKGREEN +f'[HỆ THỐNG]'+bcolors.FAIL+f"[✅]"+bcolors.OKBLUE + f' Load thành công module {command[:-3]}'+bcolors.ENDC)
            except Exception as e:
                print(bcolors.OKGREEN +f'[HỆ THỐNG]'+bcolors.FAIL+f"[❌]"+bcolors.OKBLUE + f' Load thất bại module {command[:-3]}'+bcolors.FAIL+f"["+bcolors.WARNING+f"{e}"+bcolors.FAIL+"]"+bcolors.ENDC)
            time.sleep(0.025)
    print('═════════════════════════════════════════════════════')
    print(bcolors.OKGREEN + '''

 █████╗ ███████╗██╗   ██╗███████╗    ██████╗  ██████╗ ████████╗
██╔══██╗╚══███╔╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
███████║  ███╔╝ ██║   ██║███████╗    ██████╔╝██║   ██║   ██║   
██╔══██║ ███╔╝  ██║   ██║╚════██║    ██╔══██╗██║   ██║   ██║   
██║  ██║███████╗╚██████╔╝███████║    ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                       
''' + bcolors.ENDC)
    await bot.start('MTAwMjIwOTc5MTMwNjg5OTQ5Ng.GNLjbC.MT-MkNM8ZHQcXmo5HSajFQzaDQe0bkbEmQat8w')
    print(bcolors.OKGREEN +f'[HỆ THỐNG] '+bcolors.OKCYAN+f"Bắt đầu khời tạo bot"+bcolors.ENDC)

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except Exception as e:
    
    print(e)