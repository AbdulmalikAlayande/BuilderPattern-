import sys
from typing import Any, Iterable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QWidget, QApplication, QMessageBox


class Dialog(QWidget, QApplication, QInputDialog):

    def __init__(self):
        super().__init__()

    @staticmethod
    def abdulmalik_input_str(prompt: str, prompt_title: str):
        return QInputDialog.getText(None, prompt_title, prompt, defaultValue=None)

    @staticmethod
    def abdulmalik_input_int(prompt_title: str, prompt,  default_value: int, min=-2147483647, max=2147483647, step=1, Qt_WindowFlags=None, Qt_WindowType=None):
        return QInputDialog.getInt(None, prompt_title, prompt, default_value, min, max, step, )

    @staticmethod
    def abdulmalik_input_float(prompt_title: str, prompt: str, ok_text: Any, cancel_text: Any, default_value: float = 0.0, min=sys.float_info.min,
                               max=sys.float_info.max, decimal=1):
        app = QInputDialog()
        return QInputDialog.getDouble(app, prompt_title, prompt, ok_text, cancel_text, default_value, min, max, decimal)

    @staticmethod
    def abdulmalik_input_object(prompt_title: str, prompt: str, items_to_select_from: Iterable[str],
                                index_of_initially_selected_item: int, editable=False):
        return QInputDialog.getItem(None, prompt_title, prompt, items_to_select_from, index_of_initially_selected_item, editable)

    @staticmethod
    def abdulmalik_input_object2(prompt_title: str, prompt: str, items_to_select_from: Iterable[str],
                                 index_of_initially_selected_item: int, editable=False):
        dialog = QInputDialog()
        dialog.setWindowTitle(prompt_title)
        dialog.setLabelText(prompt)
        dialog.setComboBoxItems(items_to_select_from)
        dialog.setComboBoxEditable(editable)
        combo_box = dialog.comboBox()
        combo_box.setCurrentIndex(index_of_initially_selected_item)
        dialog.exec_()
        return dialog.textValue()

    @staticmethod
    def abdulmalik_message_display(value):
        message_box = QMessageBox()
        message_box.setText(value)
        message_box.exec()
