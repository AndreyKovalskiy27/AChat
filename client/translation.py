"""Переклад программи"""


from os.path import join
from json import load


with open(join("design", "translation.json"), "r", encoding="utf-8") as translation_file:
    TRANSLATION = load(translation_file)
