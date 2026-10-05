# Built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel
import os, sys
NOVA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, NOVA_DIR)
from config import GUI_DIR
import speech_recognition as sr
from PyQt5.QtWidgets import QWidget
from MainBuddy.Buddy import MainExe
from Body.Speak.Speak import Speak

# GUI Libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI.Ui import Ui_MainWindow


# GUI part here
import pygame

class EmittingStream(QObject):
    text_written = pyqtSignal(str)
    def write(self, text):
        self.text_written.emit(str(text))
    def flush(self):
        pass

class MainThread(QThread):        
    def __init__(self):
        super(MainThread,self).__init__()
 
    def run(self):
        self.wakeup_command()


    def Listen(self): #listeninig...
        # take microphone input from the user and return string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5 #less the number, more it hears
            audio = r.listen(source,0,7) # 0,7 means cut and listen after every 6 SECONDS 
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='eng-in') #for English
            print(f'Me:"{str(query)}"\n')
        except Exception as e:
            # print(e) #show full error
            print(">>>")
            return "None"
        return query

    def wakeup_command(self):
        sys.stdout = EmittingStream()
        sys.stdout.text_written.connect(nova_window.text_written)
        Speak("Nova AI, ready to use. Built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel. System is in sleep mode.")

        while True:
            self.query = self.Listen()

            if 'wake up' in self.query.lower() or 'nova' in self.query.lower():
                print('"Wake Up" Detected...')
                MainExe()                
            else:
                print("I am sleeping...")



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.credit_label = QtWidgets.QLabel(
            "Built by Muhammad Abdullah Rasheed, Adil Hayyat and Jabran Adeel",
            self.ui.centralwidget,
        )
        self.credit_label.setGeometry(0, 920, 1910, 24)
        self.credit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.credit_label.setStyleSheet("color: white; font-size: 10pt;")

        # for gifloader.gif
        self.ui.movie = QtGui.QMovie(os.path.join(GUI_DIR, "gifloader.gif"))
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        # for initiating.jpeg
        self.ui.movie = QtGui.QMovie(os.path.join(GUI_DIR, "initiating.gif"))
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        # Time date time bars
        self.current_time = QTime.currentTime() 
        self.current_date = QDate.currentDate()
        # self.label_time = self.current_time.toString('hh:mm:ss') # if you want to show 'seconds' as well 
        self.label_time = self.current_time.toString('TIME: ' + 'hh:mm')
        self.lable_date = self.current_date.toString("dd:MM:yyyy")
        self.ui.textBrowser.setText(self.label_time)
        self.ui.textBrowser_2.setText(self.lable_date)
        self.ui.pushButton.clicked.connect(self.startTask) # Start Button
        self.ui.pushButton_2.clicked.connect(self.close) # Exit Button

    def text_written(self, text):
        self.ui.logs_textEdit.append(text)

    def startTask(self):
        startExecution.start()

    def showTime(self):
        self

# # GUI + System run...
app = QApplication(sys.argv)
nova_window = Main()
nova_window.show()
exit(app.exec_())
