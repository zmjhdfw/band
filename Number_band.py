#导入随机数模块
import random
#导入tkinter库
import tkinter as tk
from tkinter import Label
from tkinter import messagebox as tm
#导入pillow库
from PIL import Image,ImageTk
#导入sys库
import sys
#导入pygame库
import pygame
#初始化band值
band=random.randrange(100)
# 测试代码
# band=10

#定义数字炸弹类
class band_game:

    #定义主菜单函数

    def band_game_menu():
        
        global root

        root=tk.Tk()
        #设置主菜单标题
        root.title(f'数字炸弹')
        #设置主菜单固定大小
        root.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_menu_backgroud()
        #设置主菜单的开始游戏按钮并自适应主菜单窗口大小
        menu_game=tk.Button(text='开始游戏',borderwidth=0,command=band_game.band_gane_menu_game)
        menu_game.place(x=75,y=900,width=108,height=81)
        #设置主菜单的退出按钮并自适应主菜单窗口大小
        menu_exit=tk.Button(text='退出',borderwidth=0,command=band_game.band_game_menu_exit)
        menu_exit.place(x=1500,y=900,width=108,height=81)
        #设置主菜单的设置按钮并自适应窗口大小
        menu_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_setup)
        menu_setup.place(x=450,y=900,width=108,height=81)
        #设置主菜单的存取游戏按钮并自适应窗口大小
        menu_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_save)
        menu_save.place(x=825,y=900,width=108,height=81)
        #设置主菜单的读取游戏按钮并自适应窗口大小
        menu_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_load)
        menu_load.place(x=1125,y=900,width=108,height=81)
        #消息循环
        root.mainloop()

    #定义主菜单游戏函数

    def band_gane_menu_game():
        
        global _menu_game,_menu_game_entry,_menu_game_count,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=0
        _menu_game_start_click_count=0
        root.destroy()
        _menu_game=tk.Tk()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义游戏选择难度函数

    def band_game_menu_game_choice():

        global _menu_game_choice

        _menu_game.destroy()
        _menu_game_choice=tk.Tk()
        
        #设置设置标题
        _menu_game_choice.title(f'数字炸弹')
        #设置设置固定大小
        _menu_game_choice.geometry('960x600+100+100')
        #设置设置背景自适应窗口大小
        band_game.set_game_choice_backgroud()
        #定义返回按钮及大小
        _menu_game_choice_option1=tk.Button(text='简单',borderwidth=0,command=band_game.band_game_menu_game_choice_option1)
        _menu_game_choice_option1.place(x=25,y=500,width=108,height=81)
        _menu_game_choice_option2=tk.Button(text='普通',borderwidth=0,command=band_game.band_game_menu_game_choice_option2)
        _menu_game_choice_option2.place(x=430,y=500,width=108,height=81)
        _menu_game_choice_option3=tk.Button(text='困难',borderwidth=0,command=band_game.band_game_menu_game_choice_option3)
        _menu_game_choice_option3.place(x=850,y=500,width=108,height=81)
        #消息循环
        _menu_game_choice.mainloop()

    #定义选项1函数
    
    def band_game_menu_game_choice_option1():

        global _menu_game_choice,_menu_game,_menu_game_count,_menu_game_entry,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=15
        _menu_game_start_click_count=0
        _menu_game_choice.destroy()
        _menu_game=tk.Tk()
        band_game.game_music_start()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义选项2函数
    
    def band_game_menu_game_choice_option2():

        global _menu_game_choice,_menu_game,_menu_game_count,_menu_game_entry,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=10
        _menu_game_start_click_count=0
        _menu_game_choice.destroy()
        _menu_game=tk.Tk()
        band_game.game_music_start()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义选项3函数
    
    def band_game_menu_game_choice_option3():

        global _menu_game_choice,_menu_game,_menu_game_count,_menu_game_entry,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=5
        _menu_game_start_click_count=0
        _menu_game_choice.destroy()
        _menu_game=tk.Tk()
        band_game.game_music_start()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()


    #定义游戏开始函数

    def band_game_menu_game_start():

        global number_choice,_menu_game_start_click_count,_menu_game_entry,_menu_game_count
        
        while _menu_game_start_click_count == 0:
            i=1
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 1:
            i=2
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 2:
            i=3
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 3:
            i=4
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 4:
            i=5
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 5:
            i=6
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 6:
            i=7
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 7:
            i=8
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 8:
            i=9
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 9:
            i=10
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 10:
            i=11
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 11:
            i=12
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 12:
            i=13
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 13:
            i=14
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1
        while _menu_game_start_click_count == 14:
            i=15
            number_input=int(_menu_game_entry.get().strip())
            number_choice=_menu_game_count-i
            number_choice_use=i
            game_choice=f'你还有{number_choice}次机会'
            game_choice_use=f'你已用了{number_choice_use}次机会'
            if number_input > band:
                game_result='猜大了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input < band:
                game_result='猜小了'
                _menu_game_text1.insert(tk.END,game_result + '\n')
                _menu_game_text2.insert(tk.END,game_choice + '\n')
                _menu_game_text3.insert(tk.END,game_choice_use + '\n')
                _menu_game_entry.delete(0,tk.END)
            elif number_input == band:
                game_result='恭喜你，猜对了'
                _menu_game_text1.delete('1.0',tk.END)
                _menu_game_text2.delete('1.0',tk.END)
                _menu_game_text3.delete('1.0',tk.END)
                _menu_game_entry.delete(0,tk.END)
                _menu_game.withdraw()
                game_result_info=tm.askquestion('选择',f'{game_result}\n是否继续游戏')
                if game_result_info == 'yes':
                    _menu_game.deiconify()
                    _menu_game_count=0
                    _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start,state=tk.DISABLED)
                    _menu_game_start.place(x=750,y=900,width=108,height=81)
                elif game_result_info == 'no':
                    sys.exit()
            if i == _menu_game_count:
                _menu_game.destroy()
                game_result=tm.showinfo('显示结果',f'机会用尽,游戏结束')
                sys.exit()
            _menu_game_start_click_count+=1


    #定义游戏返回函数

    def band_game_menu_game_back():

        _menu_game.destroy()
        band_game.band_game_menu()

    #定义游戏设置函数

    def band_game_menu_game_setup():

        global _menu_game_setup

        _menu_game.destroy()
        _menu_game_setup=tk.Tk()
        #设置设置标题
        _menu_game_setup.title(f'数字炸弹')
        #设置设置固定大小
        _menu_game_setup.geometry('1707x1044')
        #设置设置背景自适应窗口大小
        band_game.set_game_setup_backgroud()
        #定义返回按钮及大小
        _menu_game_setup_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_setuup_back)
        _menu_game_setup_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_game_setup.mainloop()

    #定义设置返回函数

    def band_game_menu_game_setuup_back():

        global _menu_game,_menu_game_setup,_menu_game_count,_menu_game_entry,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=0
        _menu_game_start_click_count=0
        _menu_game_setup.destroy()
        _menu_game=tk.Tk()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义游戏保存函数

    def band_game_menu_game_save():

        global _menu_game_save

        _menu_game.destroy()
        _menu_game_save=tk.Tk()
        #设置保存标题
        _menu_game_save.title('数字炸弹')
        #设置保存固定大小
        _menu_game_save.geometry('1707x1044')
        #设置保存背景自适应窗口大小
        band_game.set_game_save_backgroud()
        #设置返回按钮及大小
        _menu_game_save_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_save_back)
        _menu_game_save_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_game_save.mainloop()

    #定义保存返回函数

    def band_game_menu_game_save_back():

        global _menu_game,_menu_game_entry,_menu_game_count,_menu_game_save,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=0
        _menu_game_start_click_count=0
        _menu_game_save.destroy()
        _menu_game=tk.Tk()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义游戏读取函数

    def band_game_menu_game_load():

        global _menu_game_load

        _menu_game.destroy()
        _menu_game_load=tk.Tk()
        #设置保存标题
        _menu_game_load.title('数字炸弹')
        #设置保存固定大小
        _menu_game_load.geometry('1707x1044')
        #设置保存背景自适应窗口大小
        band_game.set_game_load_backgroud()
        #设置返回按钮及大小
        _menu_game_load_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_load_back)
        _menu_game_load_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_game_load.mainloop()

    #定义读取返回函数

    def band_game_menu_game_load_back():

        global _menu_game,_menu_game_entry,_menu_game_count,_menu_game_load,_menu_game_text1,_menu_game_text2,_menu_game_text3,_menu_game_start_click_count

        _menu_game_count=0
        _menu_game_start_click_count=0
        _menu_game_load.destroy()
        _menu_game=tk.Tk()
        #设置主菜单标题
        _menu_game.title(f'数字炸弹')
        #设置主菜单固定大小
        _menu_game.geometry('1707x1044')
        #设置背景自适应主菜单窗口大小
        band_game.set_game_backgroud()
        #设置游戏的返回按钮并自适应主菜单窗口大小
        _menu_game_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_game_back)
        _menu_game_back.place(x=1500,y=900,width=108,height=81)
        #设置游戏的设置按钮并自适应窗口大小
        _menu_game_setup=tk.Button(text='设置',borderwidth=0,command=band_game.band_game_menu_game_setup)
        _menu_game_setup.place(x=75,y=900,width=108,height=81)
        #设置游戏的存取游戏按钮并自适应窗口大小
        _menu_game_save=tk.Button(text='存取游戏',borderwidth=0,command=band_game.band_game_menu_game_save)
        _menu_game_save.place(x=450,y=900,width=108,height=81)
        #设置游戏的读取游戏按钮并自适应窗口大小
        _menu_game_load=tk.Button(text='读取游戏',borderwidth=0,command=band_game.band_game_menu_game_load)
        _menu_game_load.place(x=1125,y=900,width=108,height=81)
        #定义一个开始按钮并自适应窗口大小
        _menu_game_start=tk.Button(text='开始',borderwidth=0,command=band_game.band_game_menu_game_start)
        _menu_game_start.place(x=750,y=900,width=108,height=81)
        #定义一个输入框并自适应窗口大小
        _menu_game_entry=tk.Entry()
        _menu_game_entry.place(x=450,y=750,width=108,height=81)
        #定义一个提示输入标签并自适应窗口大小
        _menu_game_label=tk.Label(text='请输入数字:')
        _menu_game_label.place(x=343,y=750,width=108,height=81)
        #定义一个文本框作为结果输出,自适应窗口大小
        _menu_game_text1=tk.Text(wrap=tk.WORD)
        _menu_game_text1.place(x=1125,y=750,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_result=tk.Label(text='结果:')
        _menu_game_result.place(x=1018,y=750,width=108,height=81)
        #定义一个文本框作为剩余机会输出,自适应窗口大小
        _menu_game_text2=tk.Text(wrap=tk.WORD)
        _menu_game_text2.place(x=450,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice=tk.Label(text='剩余机会:')
        _menu_game_choice.place(x=343,y=600,width=108,height=81)
        #定义一个文本框作为已用机会输出,自适应窗口大小
        _menu_game_text3=tk.Text(wrap=tk.WORD)
        _menu_game_text3.place(x=1125,y=600,width=108,height=81)
        #定义一个结果标签并自适应窗口大小
        _menu_game_choice_use=tk.Label(text='已用机会:')
        _menu_game_choice_use.place(x=1018,y=600,width=108,height=81)
        #定义选择难度按钮并自适应窗口大小
        _menu_game_choice=tk.Button(text='选择难度',borderwidth=0,command=band_game.band_game_menu_game_choice)
        _menu_game_choice.place(x=750,y=750,width=108,height=81)
        _menu_game.mainloop()

    #定义主菜单设置函数

    def band_game_menu_setup():

        global _menu_setup

        root.destroy()
        _menu_setup=tk.Tk()
        #设置设置标题
        _menu_setup.title(f'数字炸弹')
        #设置设置固定大小
        _menu_setup.geometry('1707x1044')
        #设置设置背景自适应窗口大小
        band_game.set_setup_backgroud()
        #定义返回按钮及大小
        _menu_setup_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_setuup_back)
        _menu_setup_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_setup.mainloop()

    #定义设置返回函数

    def band_game_menu_setuup_back():
        _menu_setup.destroy()
        band_game.band_game_menu()

    #定义主菜单保存函数

    def band_game_menu_save():

        global _menu_save

        root.destroy()
        _menu_save=tk.Tk()
        #设置保存标题
        _menu_save.title('数字炸弹')
        #设置保存固定大小
        _menu_save.geometry('1707x1044')
        #设置保存背景自适应窗口大小
        band_game.set_save_backgroud()
        #设置返回按钮及大小
        _menu_save_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_save_back)
        _menu_save_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_save.mainloop()

    #定义保存返回函数

    def band_game_menu_save_back():
        _menu_save.destroy()
        band_game.band_game_menu()

    #定义主菜单读取函数

    def band_game_menu_load():

        global _menu_load

        root.destroy()
        _menu_load=tk.Tk()
        #设置保存标题
        _menu_load.title('数字炸弹')
        #设置保存固定大小
        _menu_load.geometry('1707x1044')
        #设置保存背景自适应窗口大小
        band_game.set_load_backgroud()
        #设置返回按钮及大小
        _menu_load_back=tk.Button(text='返回',borderwidth=0,command=band_game.band_game_menu_load_back)
        _menu_load_back.place(x=1500,y=900,width=108,height=81)
        #消息循环
        _menu_load.mainloop()

    #定义读取返回函数

    def band_game_menu_load_back():
        _menu_load.destroy()
        band_game.band_game_menu()


    #定义主菜单退出函数

    def band_game_menu_exit():
        root.withdraw()
        #弹出选择框
        _menu_exit=tm.askquestion('选择','游戏进度尚未保存\n是否继续')
        if _menu_exit=='yes':
            sys.exit()
        elif _menu_exit=='no':
            root.deiconify()

    #定义获取高度与宽度函数

    def get_width_height(windows):
        windows.update_idletasks()
        wi=windows.winfo_width()
        he=windows.winfo_height()
        return wi,he

    #定义主菜单背景函数

    def set_menu_backgroud():

        global menu_bgp

        wi,he=band_game.get_width_height(root)
        menu_image_path = './bg/band.jpg'
        menu_backgroud_image=Image.open(menu_image_path)
        menu_backgroud_image=menu_backgroud_image.resize((wi,he))
        menu_bgi=menu_backgroud_image
        menu_backgroud_photo=ImageTk.PhotoImage(menu_bgi)
        menu_bgp=menu_backgroud_photo
        menu_backgroud_label=Label(master=root,image=menu_bgp)
        menu_bgl=menu_backgroud_label
        menu_bgl.place(relwidth=1,relheight=1)

    #定义主菜单游戏背景函数

    def set_game_backgroud():

        global menu_game_bgp

        wi,he=band_game.get_width_height(_menu_game)
        menu_game_image_path = './bg/band.jpg'
        menu_game_backgroud_image=Image.open(menu_game_image_path)
        menu_game_backgroud_image=menu_game_backgroud_image.resize((wi,he))
        menu_game_bgi=menu_game_backgroud_image
        menu_game_backgroud_photo=ImageTk.PhotoImage(menu_game_bgi)
        menu_game_bgp=menu_game_backgroud_photo
        menu_game_backgroud_label=Label(master=_menu_game,image=menu_game_bgp)
        menu_game_bgl=menu_game_backgroud_label
        menu_game_bgl.place(relwidth=1,relheight=1)

    #定义主菜单设置背景函数

    def set_setup_backgroud():

        global setup_bgp

        wi,he=band_game.get_width_height(_menu_setup)
        setup_image_path = './bg/setup.jpg'
        setup_backgroud_image=Image.open(setup_image_path)
        setup_backgroud_image=setup_backgroud_image.resize((wi,he))
        setup_bgi=setup_backgroud_image
        setup_backgroud_photo=ImageTk.PhotoImage(setup_bgi)
        setup_bgp=setup_backgroud_photo
        setup_backgroud_label=Label(master=_menu_setup,image=setup_bgp)
        setup_bgl=setup_backgroud_label
        setup_bgl.place(relwidth=1,relheight=1)

    #定义主菜单保存背景函数

    def set_save_backgroud():

        global save_bgp

        wi,he=band_game.get_width_height(_menu_save)
        save_image_path='./bg/save.jpg'
        save_backgroud_image=Image.open(save_image_path)
        save_backgroud_image=save_backgroud_image.resize((wi,he))
        save_bgi=save_backgroud_image
        save_backgroud_photo=ImageTk.PhotoImage(save_bgi)
        save_bgp=save_backgroud_photo
        save_backgroud_label=Label(master=_menu_save,image=save_bgp)
        save_bgl=save_backgroud_label
        save_bgl.place(relwidth=1,relheight=1)

    #定义主菜单读取背景函数

    def set_load_backgroud():

        global load_bgp

        wi,he=band_game.get_width_height(_menu_load)
        load_image_path='./bg/load.jpg'
        load_backgroud_image=Image.open(load_image_path)
        load_backgroud_image=load_backgroud_image.resize((wi,he))
        load_bgi=load_backgroud_image
        load_backgroud_photo=ImageTk.PhotoImage(load_bgi)
        load_bgp=load_backgroud_photo
        load_backgroud_label=Label(master=_menu_load,image=load_bgp)
        load_bgl=load_backgroud_label
        load_bgl.place(relwidth=1,relheight=1)

    #定义游戏设置背景函数

    def set_game_setup_backgroud():

        global game_setup_bgp

        wi,he=band_game.get_width_height(_menu_game_setup)
        game_setup_image_path = './bg/setup.jpg'
        game_setup_backgroud_image=Image.open(game_setup_image_path)
        game_setup_backgroud_image=game_setup_backgroud_image.resize((wi,he))
        game_setup_bgi=game_setup_backgroud_image
        game_setup_backgroud_photo=ImageTk.PhotoImage(game_setup_bgi)
        game_setup_bgp=game_setup_backgroud_photo
        game_setup_backgroud_label=Label(master=_menu_game_setup,image=game_setup_bgp)
        game_setup_bgl=game_setup_backgroud_label
        game_setup_bgl.place(relwidth=1,relheight=1)

    #定义游戏保存背景函数

    def set_game_save_backgroud():

        global game_save_bgp

        wi,he=band_game.get_width_height(_menu_game_save)
        game_save_image_path = './bg/save.jpg'
        game_save_backgroud_image=Image.open(game_save_image_path)
        game_save_backgroud_image=game_save_backgroud_image.resize((wi,he))
        game_save_bgi=game_save_backgroud_image
        game_save_backgroud_photo=ImageTk.PhotoImage(game_save_bgi)
        game_save_bgp=game_save_backgroud_photo
        game_save_backgroud_label=Label(master=_menu_game_save,image=game_save_bgp)
        game_save_bgl=game_save_backgroud_label
        game_save_bgl.place(relwidth=1,relheight=1)

    #定义游戏读取背景函数

    def set_game_load_backgroud():

        global game_load_bgp

        wi,he=band_game.get_width_height(_menu_game_load)
        game_load_image_path = './bg/load.jpg'
        game_load_backgroud_image=Image.open(game_load_image_path)
        game_load_backgroud_image=game_load_backgroud_image.resize((wi,he))
        game_load_bgi=game_load_backgroud_image
        game_load_backgroud_photo=ImageTk.PhotoImage(game_load_bgi)
        game_load_bgp=game_load_backgroud_photo
        game_load_backgroud_label=Label(master=_menu_game_load,image=game_load_bgp)
        game_load_bgl=game_load_backgroud_label
        game_load_bgl.place(relwidth=1,relheight=1)

    #定义游戏选择难度背景函数

    def set_game_choice_backgroud():

        global game_choice_bgp

        wi,he=band_game.get_width_height(_menu_game_choice)
        game_choice_image_path = './bg/band.jpg'
        game_choice_backgroud_image=Image.open(game_choice_image_path)
        game_choice_backgroud_image=game_choice_backgroud_image.resize((wi,he))
        game_choice_bgi=game_choice_backgroud_image
        game_choice_backgroud_photo=ImageTk.PhotoImage(game_choice_bgi)
        game_choice_bgp=game_choice_backgroud_photo
        game_choice_backgroud_label=Label(master=_menu_game_choice,image=game_choice_bgp)
        game_choice_bgl=game_choice_backgroud_label
        game_choice_bgl.place(relwidth=1,relheight=1)

    #定义游戏音乐

    def game_music_start():

        pygame.init()
        music_start="./music/game.mp3"
        pygame.mixer.music.load(music_start)
        pygame.mixer.music.play(loops=-1)

band_game.band_game_menu()