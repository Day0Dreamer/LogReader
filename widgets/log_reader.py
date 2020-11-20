from widgets import log_reader_ui, stylesheet
from qtpy import QtWidgets


class UILogReader(QtWidgets.QWidget, log_reader_ui.Ui_log_reader_widget):
    def __init__(self):
        super(UILogReader, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(stylesheet.houdini)
        self.setWindowTitle('Log Reader')




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = UILogReader()
    ui.show()
    app.exec_()
