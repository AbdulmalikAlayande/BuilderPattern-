from PyQt5.QtWidgets import QApplication, QInputDialog, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt


class CustomInputDialog(QInputDialog):
    def __init__(self, parent=None, flags=None, window_type=None):
        super().__init__(parent)
        self.setWindowFlags(flags or Qt.WindowFlags())
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(window_type or Qt.WindowType())

    def get_int(self, title, label, value=0, min=-2147483647, max=2147483647, step=1, ok_text="OK", cancel_text="Cancel"):
        return self.getInt(self, title, label, value=value, min=min, max=max, step=step, textOk=ok_text, textCancel=cancel_text)


class App(QWidget):
    def __init__(self, flags=None, window_type=None):
        super().__init__()
        self.label = None
        self.flags = flags or Qt.WindowFlags()
        self.window_type = window_type or Qt.WindowType()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Click the button to enter a value")
        layout.addWidget(self.label)

        button = QPushButton("Enter Value")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle("Custom Input Dialog Example")
        self.show()

    def on_button_click(self):
        dialog = CustomInputDialog(flags=self.flags, window_type=self.window_type)
        value, ok_pressed = dialog.get_int("Enter Value", "Enter an integer value")
        if ok_pressed:
            self.label.setText(f"You entered: {value}")


if __name__ == '__main__':
    app = QApplication([])
    example = App(flags=Qt.WindowStaysOnTopHint, window_type=Qt.Dialog)
    app.exec_()
