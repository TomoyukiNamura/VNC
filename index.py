# -*- coding: utf-8 -*-
import os
import configparser
import json
import MeCab
from bottle import route, run, request
from bottle import TEMPLATE_PATH, jinja2_template as template

inifile = configparser.SafeConfigParser()
inifile.read("./config.ini")
select = {"type":json.loads(inifile["SELECT"]["type"]),
          "case":json.loads(inifile["SELECT"]["case"]),
          "language":json.loads(inifile["SELECT"]["language"]),
          "acronym":json.loads(inifile["SELECT"]["acronym"]),}

# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

@route("/")
def top():
    return template("top", select=select, sentence="", result="")

@route("/convert", method="POST")
def convert():

    input_data = dict(request.forms)
    input_data["sentence"] = _split_word(request.forms.sentence)
    print(input_data)
    result = "ワイ、ガイジ"

    return template("top", result=result)


def _split_word(sentence):

    mecab = MeCab.Tagger("-Owakati")
    wakati = mecab.parse(sentence).split(" ")

    return wakati


if __name__ == "__main__":
    run(host="192.168.100.111", port=8080, debug=True, reloader=True)
