#!/usr/bin/env python3
from clickshot import Keyboard, Key

from regions.connect_dialog import connect_dialog
from regions.main_window import main_window

keyboard = Keyboard()

connect_dialog.wait_until_visible()
connect_dialog.set_code_button.wait_until_visible()
keyboard.type("981891-wormholeui-test\n")
main_window.blank.wait_until_visible()

keyboard.type("Hello from transmit test\n")
main_window.tx_send_message.wait_until_visible()

main_window.tx_receive_message.wait_until_visible()