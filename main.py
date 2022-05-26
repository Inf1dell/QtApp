import math
import sys
import random
import threading
import time

import massiv

from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic, QtTest

name = ''
answer = ''

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginView.ui', self)
        self.loginBtn.clicked.connect(self.login)
        self.nameEdit.returnPressed.connect(self.loginBtn.click)
        self.exitBtn.clicked.connect(self.exit)

    def login(self):
        global name
        text = self.nameEdit.text()
        print(text)
        if text != '' and text != ' ':
            name = text
            self.close()
            self.Menu = MainWindow()
            self.Menu.show()
    def exit(self):
        self.close()


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainView.ui', self)
        self.backBtn.clicked.connect(self.exit)
        self.oneBtn.clicked.connect(self.one)
        self.twoBtn.clicked.connect(self.two)
        self.threeBtn.clicked.connect(self.three)

    def one(self):
        self.close()
        self.Menu = OneWindow()
        self.Menu.show()

    def two(self):
        self.close()
        self.Menu = TwoWindow()
        self.Menu.show()

    def three(self):
        self.close()
        self.Menu = ThreeWindow()
        self.Menu.show()

    def exit(self):
        self.close()


class OneWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('One.ui', self)
        # add score
        global answer

        self.backBtn.clicked.connect(self.exit)

        self.answerOneOne.clicked.connect(self.check)
        self.answerOneTwo.clicked.connect(self.check)
        self.answerOneThree.clicked.connect(self.check)

        self.answerTwoOne.clicked.connect(self.check)
        self.answerTwoTwo.clicked.connect(self.check)
        self.answerTwoThree.clicked.connect(self.check)

        self.answerOneThree.clicked.connect(self.check)
        self.answerThreeTwo.clicked.connect(self.check)
        self.answerThreeThree.clicked.connect(self.check)

        self.label.adjustSize()
        self.labelScore.adjustSize()

        self.answer = ''
        self.score = 0
        self.start()

    def start(self):
        mm=massiv.mm
        print(mm)
        btns = []
        for i in range(9):
            item = (random.choice(mm))
            btns.append(item)
        print(btns)
        self.answer = (random.choice(btns))
        print(self.answer)
        self.label.setText(str(self.answer))

        for q in range(9):
            self.answers = (random.choice(btns))
            btns.remove(self.answers)
            self.gridLayout.itemAt(q).widget().setText(self.answers)

    def check(self):
        if self.sender().text()==self.answer:
            print("Sucessfull")
            self.score+=5
            self.labelScore.setText("Очков: " + str(self.score))
            self.start()
        else:
            print("Error")
            self.score -= 1
            self.labelScore.setText("Очков: " + str(self.score))
            self.start()

        if self.score < 0:
            self.close()
            self.Menu = Lose()
            self.Menu.show()
        elif self.score >= 25:
            self.close()
            self.Menu = Win()
            self.Menu.show()

    def exit(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


class TwoWindow(QDialog):
    global timer

    def __init__(self):
        super().__init__()
        uic.loadUi('Two.ui', self)

        self.text = massiv.text2_2
        self.label_2.setText("Нажмите Start что-бы начать")
        self.word = 1
        for i in self.text:
            if(i==" "):
                self.word += 1

        self.backBtn.clicked.connect(self.exit)

        self.Osec = 0
        self.sec = 0  # 2
        self.min = 0  # 2

        self.timer = QTimer(self)  # 3
        self.timer.timeout.connect(self.update_func)

        self.stBtn.clicked.connect(self.start_stop_func)

    def start_stop_func(self):
        if not self.timer.isActive():
            self.stBtn.setText('Stop')
            self.Osec = 0
            self.sec = 0
            self.min = 0
            self.label.setText('Время: 00:00')
            self.timer.start(1000)
            self.label_2.setText(str(self.text))
        else:
            self.stBtn.setText('Start')
            self.timer.stop()
            V = self.word / (self.Osec/60)
            print(self.word)
            self.label_2.setText(str(math.ceil(V))+" слов/минут")


    def update_func(self):
        self.Osec += 1

        self.sec += 1
        if self.sec >+ 60:
            self.min += 1
            self.sec = 0
        if self.min < 10:
            if self.sec < 10:
                self.label.setText('Время: 0'+str(self.min)+':0'+str(self.sec))
            else:
                self.label.setText('Время: 0'+str(self.min)+':'+str(self.sec))
        else:
            if self.sec < 10:
                self.label.setText('Время: ' + str(self.min) + ':0' + str(self.sec))
            else:
                self.label.setText('Время: ' + str(self.min) + ':' + str(self.sec))

    def exit(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


class ThreeWindow(QDialog):
    global timer

    def __init__(self):
        super().__init__()
        uic.loadUi('Three.ui', self)

        self.backBtn.clicked.connect(self.exit)

        self.text = massiv.text1_3
        self.label_2.setText("Нажмите Start что-бы начать")


        self.sec = 0  # 2
        self.min = 0  # 2

        self.timer = QTimer(self)  # 3
        self.timer.timeout.connect(self.update_func)

        self.stBtn.clicked.connect(self.start_stop_func)

    def start_stop_func(self):
        if not self.timer.isActive():
            self.stBtn.setText('Stop')
            self.stBtn.setEnabled(False)
            self.sec = 0
            self.min = 0
            self.label.setText('Время: 00:00')
            self.timer.start(1000)
            self.label_2.setText("")
            t = threading.Thread(target=self.loop, args=())
            t.start()
        else:
            self.stBtn.setText('Start')
            self.stBtn.setEnabled(True)
            self.timer.stop()


    def update_func(self):
        self.sec += 1
        if self.sec >+ 60:
            self.min += 1
            self.sec = 0
        if self.min < 10:
            if self.sec < 10:
                self.label.setText('Время: 0'+str(self.min)+':0'+str(self.sec))
            else:
                self.label.setText('Время: 0'+str(self.min)+':'+str(self.sec))
        else:
            if self.sec < 10:
                self.label.setText('Время: ' + str(self.min) + ':0' + str(self.sec))
            else:
                self.label.setText('Время: ' + str(self.min) + ':' + str(self.sec))

    def loop(self):
        tt=''
        for i in self.text:
            if (i=="*"):
                self.start_stop_func()
            else:
                time.sleep(0.05)
                print(i)
                tt+=i
                self.label_2.setText(str(tt))


    def exit(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


class Win(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('Win.ui', self)

        self.backBtn.clicked.connect(self.back)

    def back(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


class Lose(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('Lose.ui', self)

        self.backBtn.clicked.connect(self.back)

    def back(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
