import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QRadioButton, QComboBox, QButtonGroup, QHBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setGeometry(100,100, 300, 100)

        self.options_label = QLabel('Select an option:', self)

        self.option1_radio = QRadioButton('Option 1', self)
        self.option2_radio = QRadioButton('Option 2', self)
        self.option3_radio = QRadioButton('Option 3', self)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.option1_radio)
        self.button_group.addButton(self.option2_radio)
        self.button_group.addButton(self.option3_radio)

        self.dropdown_label = QLabel('Select an option:', self)

        self.dropdown_list = QComboBox(self)
        self.dropdown_list.addItem('Option 1')
        self.dropdown_list.addItem('Option 2')
        self.dropdown_list.addItem('Option 3')

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.options_label)
        layout.addWidget(self.option1_radio)
        layout.addWidget(self.option2_radio)
        layout.addWidget(self.option3_radio)
        layout.addWidget(self.dropdown_label)
        layout.addWidget(self.dropdown_list)

            # Create QHBoxLayout for horizontal alignment
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addLayout(layout)
        h_layout.addStretch(1)

        self.setLayout(h_layout)

        self.button_group.buttonClicked.connect(self.radioButtonClicked)

        self.dropdown_list.currentIndexChanged.connect(self.dropdownIndexChanged)

    def radioButtonClicked(self, button):
        selected_option = button.text()
        print('Selected option:', selected_option)

    def dropdownIndexChanged(self, index):
        selected_item = self.dropdown_list.currentText()
        print('Selected item:', selected_item)

if __name__ == '__main__':
    app = QApplication([])
    ex = MyApp()
    ex.show()
    app.exec_()


