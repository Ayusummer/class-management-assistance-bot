'''
Author: your name
Date: 2021-03-02 00:05:07
LastEditTime: 2021-05-15 09:31:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \nonebot-test\bot.py
'''

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()                                  # 使用默认配置初始化 NoneBot
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)    # 加载 NoneBot 内置的 CQHTTP 协议适配组件
nonebot.load_builtin_plugins()                  # 加载 NoneBot 内置的插件

if __name__ == "__main__":
    nonebot.run(host='127.0.0.1', port=8083)
