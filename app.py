# DearPyGUI import
from dearpygui.core import *
from dearpygui.simple import *

# Sms Spam Filter Import
# import random
# import pandas as pd
# import string
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# Functions Import
from functions import categorize_words, predict, pre_process

pred = []

def check_spam(pred=[]):
    with window("Simple SMS Spam Filter"):
        print(pred)
        if pred == []:
            add_spacing(count=12)
            add_separator()
            add_spacing(count=12)
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            pred_text, text_color = predict(input_value)

            pred.append(pred_text)
            add_text (pred[-1], color=text_color)
        else: 
            hide_item(pred[-1])
            input_value = get_value("Input")
            input_value = pre_process(input_value)
            pred_text, text_color = predict(input_value)

            pred.append(pred_text)
            add_text (pred[-1], color=text_color)

    

# windown object setting
set_main_window_size(540, 720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30, 30)

with window("Simple SMS Spam Filter", width=520, height=677):
    print("GUI is running ...")
    set_window_pos("Simple SMS Spam Filter", 0, 0)
    #image logo
    add_drawing("logo", width=520, height=290) #create some space for the image
    add_separator()
    add_spacing(count=12)
    add_text("Please enter an SMS message of you choice to check if it's spam or not", color=[232, 163, 33])
    add_spacing(count=12)
    add_input_text("Input", width=415, default_value="type message here!")
    add_spacing(count=12)
    add_button("Check", callback=lambda x,y:check_spam(pred))

draw_image("logo", "logo_spamFilter.png", [0,0], [458,192])
start_dearpygui()
