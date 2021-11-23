# FROM: ベースのイメージをpull
FROM ubuntu:20.04

# RUN: コンテナ生成時に実行
RUN apt-get update && apt-get -y upgrade
RUN apt install -y openslide-tools
RUN apt-get install -y python3-pip
RUN pip3 install opencv-python \
 opencv-contrib-python \
 numpy \
 matplotlib \
 openslide-python

# ADD(COPY): コンテナ内にファイルを追加
RUN mkdir /foo
RUN mkdir /hoge
ADD hello /hoge

VOLUME ["/hoge"]
