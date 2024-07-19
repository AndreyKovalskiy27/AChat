"""Обробка підключень та відключеннь користувачів"""


import translation


def user_connection_handler(data: dict, main_window) -> None:
    """Обробник підключення нового користувача"""
    text = (f"{data["nikname"]} {translation.TRANSLATION[
        main_window.design.language][
        "new_user_connected"]}")
    main_window.add_message(text)

    if not main_window.isActiveWindow():
        main_window.tray_icon.showMessage(
            text,
            "",
            main_window.tray_icon.MessageIcon.NoIcon,
            3000)

def user_exit_handler(data: dict, main_window) -> None:
    """Обробка відключення користувача"""
    text = (f"{data["nikname"]} "
        f"{translation.TRANSLATION[
            main_window.design.language][
            "user_exited"]}")
    was_error = data.get("was_error", False)

    if was_error:
        text = (f"{data["nikname"]} "
        f"{translation.TRANSLATION[
            main_window.design.language][
            "user_deleted_by_an_error"]}")

    main_window.add_message(text)

    if not main_window.isActiveWindow():
        main_window.tray_icon.showMessage(
            text,
            "",
            main_window.tray_icon.MessageIcon.NoIcon,
            3000)
