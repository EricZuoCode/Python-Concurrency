#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import multiprocessing as mp


def copy_file(file_name, sour_dir, dest_dir):
    '''
    复制文件的函数
        :param file_name: 文件名
        :param sour_dir: 源目录
        :param dest_dir: 目标目录
        :return: None
    '''
    sour_file_path = os.path.join(sour_dir, file_name)
    dest_file_path = os.path.join(dest_dir, file_name)

    with open(sour_file_path, 'rb') as f_sour:
        with open(dest_file_path, 'wb') as f_dest:
            while True:
                data = f_sour.read(1024)
                # 如果读取到的数据为空，则停止读取
                # 如果读取到的数据不为空，则写入到目标文件中
                if not data:
                    break
                f_dest.write(data)


if __name__ == "__main__":

    # 定义起始目录和目标目录
    sour_dir = "sour_directory"
    dest_dir = "dest_directory"

    # 创建目标目录
    try:
        os.mkdir(dest_dir)
    except FileExistsError:
        print(f"Directory '{dest_dir}' already exists.")
        exit(1)

    # 获取源目录下的所有文件
    files = os.listdir(sour_dir)

    # 定义复制文件的函数
    for file_name in files:
        p = mp.Process(target=copy_file, args=(file_name, sour_dir, dest_dir))
        p.start()
