'''
Author: your name
Date: 2021-03-02 00:05:07
LastEditTime: 2021-03-02 00:05:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \nonebot-test\bot.py
'''
import nonebot

if __name__ == '__main__':
    nonebot.init()
    nonebot.load_builtin_plugins()
    nonebot.run(host='127.0.0.1', port=8083)