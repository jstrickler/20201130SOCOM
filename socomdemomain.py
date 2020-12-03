#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_socomdemo import Ui_SocomDemo


class SocomDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_SocomDemo()  # instantiate the generated user interface
        self.ui.setupUi(self)  # call the function to create all the widgets

        # Connect up menu actions
        # self.ui.actionQuit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)
        self.ui.button_doit.clicked.connect(self._button_pushed)

    def _button_pushed(self):
        self.ui.le_name.setText("wombat!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SocomDemoMain()
    main.show()
    result = app.exec_()
    sys.exit(result)
    # sys.exit(app.exec_())
