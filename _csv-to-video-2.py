#!/usr/bin/env python3.7
import csv
from tkinter import *
from tkinter import filedialog
import subprocess
from tkinter import messagebox
import os
import sys

curr_folder = os.path.dirname(os.path.abspath(__file__))

root2 = Tk()
root2.withdraw()

root = Tk()
root.withdraw()

root3 = Tk()
root3.withdraw()

root1 = Tk()
root1.withdraw()


def open_file_csv():
    filename = filedialog.askopenfilename(parent=root)
    if filename:
        root.destroy()
    print('CSV')
    return filename


def open_file_video():
    filename1 = filedialog.askopenfilename(parent=root1)
    if filename1:
        root1.destroy()
    print('VIDEO')
    return filename1


def extract_video(time_out,time_in,url_video,url_outvideo):
    command = f"ffmpeg -t '{time_out}' -i '{url_video}' -ss '{time_in}' '{url_outvideo}'"
    subprocess.call(command,shell=True)


def msg_box_csv():
    root2.geometry("5x5")
    box1 = messagebox.showinfo("ファイルを開く","CSVファイルを開いてください")
    if box1:
        root2.destroy()


def msg_box_video():
    root3.geometry("5x5")
    box3 = messagebox.showinfo("ファイルを開く","ビデオファイルを開いてください")
    if box3:
        root3.destroy()


def create_clip_name_path_A(clip_counter, folder_to_save_in):
    clipName = '00' + str(clip_counter) + "." + 'mp4'
    clipPath = os.path.join(folder_to_save_in, clipName)
    return clipPath

def msg_box():
    messagebox.showerror("エラー","ファイルには互換性がありません。" "\r" "もう一度やり直してください。" "\r" "または、別のファイルを使用します。")


msg_box_csv()

input_file_csv = str(open_file_csv())

msg_box_video()


def main():

    input_file_video = str(open_file_video())

    with open(input_file_csv, 'r') as infile:
        reader = csv.DictReader(infile)

        for video_config in reader:

            split_start = video_config["スタート"] #START
            split_end = video_config["端"] #END
            video_name = video_config["ファイル名"] #FILE NAME
            extract_video(split_end, split_start, input_file_video, curr_folder + '/' + video_name)
            #print(split_end, ' ',split_start, ' ', input_file_video, ' ', curr_folder + '/' + video_name)


if __name__ == '__main__':
    try:
        main()
    except:
        msg_box()
        print("Error")
        sys.exit(1)
