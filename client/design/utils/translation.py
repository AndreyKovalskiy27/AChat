"""Переклад программи"""

from os.path import join
from json import load
from loguru import logger


with open(
    join("design", "utils", "translation.json"), "r", encoding="utf-8"
) as translation_file:
    TRANSLATION = load(translation_file)
    logger.debug(f"Завантажений переклад: {TRANSLATION}")
