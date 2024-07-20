"""Обробка нажаття на стікер"""


def setup_stickers(self) -> None:
    """Налаштувати стікери"""
    self.stickers = {
        1: self.design.sticker1,
        2: self.design.sticker2,
        3: self.design.sticker3,
        4: self.design.sticker4,
        5: self.design.sticker5,
        6: self.design.sticker6,
        7: self.design.sticker7,
        8: self.design.sticker8,
        9: self.design.sticker9,
        10: self.design.sticker10,
        11: self.design.sticker11,
        12: self.design.sticker12,
        13: self.design.sticker13,
        14: self.design.sticker14,
        15: self.design.sticker15,
    }

    self.selected_sticker = None

    # Натискання на стікери
    for sticker in range(1, len(self.stickers) + 1):
        self.stickers[sticker].clicked.connect(
            lambda _, current_sticker=sticker: select_sticker(self, current_sticker)
        )


def select_sticker(self, sticker_number: int) -> None:
    """Вибрати стікер"""
    if self.selected_sticker == sticker_number:
        self.stickers[sticker_number].setStyleSheet("")
        self.selected_sticker = None

    else:
        if self.selected_sticker:
            self.stickers[self.selected_sticker].setStyleSheet("")

        self.stickers[sticker_number].setStyleSheet(
            "border-radius: 50%; border: 2px solid white;"
        )
        self.selected_sticker = sticker_number
