
# Form implementation generated from reading ui file 'Ui.ui'

# Created by: PyQt5 UI code generator 5.15.10

import os
import sys
NOVA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, NOVA_DIR)
from config import GUI_DIR
from PyQt5 import QtCore, QtGui, QtWidgets


def _asset_path(name):
    return os.path.join(GUI_DIR, name).replace(os.sep, "/")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1910, 950)
        MainWindow.setStyleSheet("background-color: black;")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_asset_path("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1910,950))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(_asset_path("gifloader.gif")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 580, 221, 181))  # Push button location
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(f"image: url({_asset_path('play.jpg')});\n"
"border:none;")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(56, 56))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 40, 211, 101))    # Exit button location
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet(f"image: url({_asset_path('exit.jpg')});\n"
"border:none;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -40, 421, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(_asset_path("initiating.gif")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 570, 281, 51))
        self.textBrowser.setStyleSheet("background: transparent; border:none;\n"
"font: 12pt \"Eras Demi ITC\";\n"
"text-align: center;\n"
"color:rgb(255, 255, 255)")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 690, 261, 51))
        self.textBrowser_2.setStyleSheet("background: transparent; border:none;\n"
"font: 12pt \"Eras Demi ITC\";\n"
"text-align: center;\n"
"color:rgb(255, 255, 255)")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 530, 371, 121))
        self.label_3.setStyleSheet(f"image: url({_asset_path('tuse.png')});\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-attachment: fixed;\n"
"background-size: cover;\n"
"border:none;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(_asset_path("tuse.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 650, 371, 121))
        self.label_4.setStyleSheet(f"image: url({_asset_path('tuse.png')});\n"
"border:none;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(_asset_path("tuse.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# ----------------------------------------------------------------------------------------------------------------

        # Create a label for the moving text
        self.Label = QtWidgets.QLabel(self.centralwidget)
        self.Label.setGeometry(QtCore.QRect(0, 830, 1910, 120))  # Adjust position and size as needed
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)  # Make the text bold
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)  # Align text as center
        self.Label.setText("""
        <table border="0" cellpadding="8" cellspacing="8" width="100%">
            <tr>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Image Generation</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Check battery</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Dictionary</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Graph Visualizer</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Information Retrieval</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Change Wallpaper</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Conversational Interactions</div>
                </td>
            </tr>
            <tr>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Music Playback</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Latest News</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">PDF Reader</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">System Control</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Code & Poem Generation</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Weather Forecasts</div>
                </td>
                <td style="border: 2px solid white; border-radius: 10px;">
                    <div style="font-family: 'Segoe UI'; font-size: 14pt; color: #87CEEB;">Additional Features</div>
                </td>
            </tr>
        </table>
        """)

        self.Label.setVisible(True)

# ----------------------------------------------------------------------------------------------------------------

        self.logs_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.logs_textEdit.setGeometry(QtCore.QRect(1270, 0, 640, 830))
        self.logs_textEdit.setStyleSheet("background-color: black; color: yellow;")
        self.logs_textEdit.setObjectName("logs_textEdit")
        
        # Setting font size
        font = QtGui.QFont()
        font.setPointSize(16)  
        # Setting font family
        font.setFamily("Times New Roman")  
        # Applying the font to the QTextEdit widget
        self.logs_textEdit.setFont(font)
        
        self.auto_scroll = True
        self.logs_textEdit.verticalScrollBar().valueChanged.connect(self.on_scroll)
        self.scroll_bar = QtWidgets.QScrollBar(self.centralwidget)
        self.scroll_bar.setGeometry(QtCore.QRect(1910, 0, 300, 830))  # Adjust width and height as needed
        
    def on_scroll(self):
        # Get the scrollbar object
        scroll_bar = self.logs_textEdit.verticalScrollBar()
        # Determine if the user is scrolling manually
        if scroll_bar.value() == scroll_bar.maximum():
            self.auto_scroll = True
        else:
            self.auto_scroll = False

    def scroll_to_bottom(self):
        # Ensure cursor visibility and set scrollbar value to maximum
        self.logs_textEdit.ensureCursorVisible()
        self.logs_textEdit.verticalScrollBar().setValue(self.logs_textEdit.verticalScrollBar().maximum())

    def add_log(self, text):
        # Append new text to the QTextEdit
        self.logs_textEdit.append(text)
        # Scroll to the bottom if auto-scroll is enabled
        if self.auto_scroll:
            self.scroll_to_bottom()

# ----------------------------------------------------------------------------------------------------------------------
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nova AI"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.875pt;\"><br /></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
