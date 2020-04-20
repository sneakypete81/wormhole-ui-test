#!/usr/bin/env python3
from clickshot import Keyboard, Key

from regions.connect_dialog import connect_dialog
from regions.main_window import main_window

keyboard = Keyboard()

connect_dialog.wait_until_visible()
keyboard.type("981891-wormholeui-test")
connect_dialog.set_code_button.click()
main_window.blank.wait_until_visible()

main_window.rx_receive_message.wait_until_visible()

keyboard.type("Hello from receive test")
main_window.send_message_button.click()
main_window.rx_send_message.wait_until_visible()