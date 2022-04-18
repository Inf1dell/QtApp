import sys  # sys нужен для передачи argv в QApplication
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
from PyQt5 import uic


name = ''
answer = ''


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginView.ui', self)


        self.loginBtn.clicked.connect(self.login)
        self.exitBtn.clicked.connect(self.exit)



    def login(self):
        global name
        text = self.nameEdit.toPlainText()
        print(text)
        if (text != '' and text != ' '):
            name=text
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

    def one(self):
        self.close()
        self.Menu = OneWindow()
        self.Menu.show()

    def exit(self):
        self.close()


class OneWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('One.ui', self)

        global answer

        self.backBtn.clicked.connect(self.exit)

        self.answerOneOne.clicked.connect(self.check)
        self.answerOnTwo.clicked.connect(self.check)
        self.answerOneThree.clicked.connect(self.check)

        self.answerTwoOne.clicked.connect(self.check)
        self.answerTwoTwo.clicked.connect(self.check)
        self.answerTwoThree.clicked.connect(self.check)

        self.answerOneThree.clicked.connect(self.check)
        self.answerThreeTwo.clicked.connect(self.check)
        self.answerThreeThree.clicked.connect(self.check)


        self.label.setText('НЕР')
        self.label.adjustSize()

        btns = ['НАГ','РАГ','ДЕР',
                'НИЖ','ФЕЙ','РОП',
                'НИР','ШОР','МЕР',]

        answer = (random.choice(btns))

        for q in range(9):
            answers = (random.choice(btns))
            btns.remove(answers)
            self.gridLayout.itemAt(q).widget().setText(answers)







    def check(self):
        global answer
        if (self.sender().text()=='НИР'):
            print("Sucessfull")
        # if (self.sender().text()==answer):



    def exit(self):
        self.close()
        self.Menu = MainWindow()
        self.Menu.show()


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение




if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()