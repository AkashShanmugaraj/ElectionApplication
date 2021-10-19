from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import keyboard
import os
import json

class MainScreenSPL(QWidget):
    
    def save_firebase(self):
        global ref
        import firebase_admin
        from firebase_admin import db
        cred_obj = firebase_admin.credentials.Certificate('electionvnps-firebase-adminsdk-3ypv5-52c9b529b4.json')
        default_app = firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://electionvnps-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })
        ref = db.reference("/")

    save_firebase()
    searchdirectory = '/maleCandidate'
    nominatedMale = 0
    nominatedfemale = 0
    candidict = ref.get()

    def __init__(self):
        super().__init__()
        self.stop = False  # your 'stop' variable
        self.initUI()

    def eventfilterassignment(self, object, index, subdir):
        searchdirectory_Male = os.getcwd() + subdir
        male_faces = os.listdir(path=searchdirectory_Male)
        file = f'Face{index}.png'
        if file in male_faces:
            object.installEventFilter(self)

    
    def initUI(self):
        # Candidate Json

        # Palette
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)

        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)

        self.setPalette(palette)
        self.maintext = QLabel(self)
        self.maintext.setGeometry(QRect(58, 71, 1123, 177))
        self.maintext.setText("Choose your Male \nCandidate [SPL]")
        
        font = QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(40)
        self.maintext.setFont(font)
        self.maintext.setObjectName("label")
        self.maintext.adjustSize()

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(10, 240, 1461, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.CandidatePage1 = QWidget()
        self.CandidatePage1.setObjectName("CandidatePage1")

        font = QFont()
        font.setPointSize(20)

        # Candidate 1
        self.CandiImg1 = QLabel(self.CandidatePage1)
        self.CandiImg1.setGeometry(QRect(59, 70, 369, 369))
        self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face1.png"))
        self.CandiImg1.setObjectName("CandiImg1")
        self.CandiImg1.installEventFilter(self)
        self.eventfilterassignment(object=self.CandiImg1, index=1, subdir=self.searchdirectory)

        # Candidate 2
        self.CandiImg2 = QLabel(self.CandidatePage1)
        self.CandiImg2.setGeometry(QRect(480, 70, 320, 320))
        self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face2.png"))
        self.CandiImg2.setObjectName("CandiImg2")
        self.CandiImg2.adjustSize()
        self.eventfilterassignment(object=self.CandiImg2, index=2, subdir=self.searchdirectory)

        # Candidate 3
        self.CandiImg3 = QLabel(self.CandidatePage1)
        self.CandiImg3.setGeometry(QRect(900, 70, 369, 369))
        self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face3.png"))
        self.CandiImg3.setObjectName("CandiImg3")
        self.eventfilterassignment(object=self.CandiImg3, index=3, subdir=self.searchdirectory)

        # Move to Next Page
        self.buttonRight = QLabel(self.CandidatePage1)
        self.buttonRight.setGeometry(QRect(1340, 220, 91, 91))
        self.buttonRight.setText("")
        self.buttonRight.setPixmap(QPixmap("arrowRight.png"))
        self.buttonRight.setObjectName("buttonRight")
        self.buttonRight.installEventFilter(self)

        self.stackedWidget.addWidget(self.CandidatePage1)

        self.CandidatePage2 = QWidget()
        self.CandidatePage2.setObjectName("CandidatePage2")

        font = QFont()
        font.setPointSize(20)

        # Candidate 4
        self.CandiImg4 = QLabel(self.CandidatePage2)
        self.CandiImg4.setGeometry(QRect(250, 70, 369, 369))
        self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face4.png"))
        self.CandiImg4.setObjectName("CandiImg4")
        self.eventfilterassignment(object=self.CandiImg4, index=4, subdir=self.searchdirectory)

        # Candidate 5
        self.CandiImg5 = QLabel(self.CandidatePage2)
        self.CandiImg5.setGeometry(QRect(650, 70, 369, 369))
        self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face5.png"))
        self.CandiImg5.setObjectName("CangiImg5")
        self.eventfilterassignment(object=self.CandiImg5, index=5, subdir=self.searchdirectory)

        # Candidate 6
        self.CandiImg6 = QLabel(self.CandidatePage2)
        self.CandiImg6.setGeometry(QRect(1070, 70, 369, 369))
        self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face6.png"))
        self.CandiImg6.setObjectName("CandiImg6")
        self.eventfilterassignment(object=self.CandiImg6, index=6, subdir=self.searchdirectory)

        self.buttonLeft = QLabel(self.CandidatePage2)
        self.buttonLeft.setGeometry(QRect(20, 210, 91, 91))
        self.buttonLeft.setText("")
        self.buttonLeft.setPixmap(QPixmap("arrowLeft.png"))
        self.buttonLeft.setObjectName("buttonLeft")
        self.buttonLeft.installEventFilter(self)

        self.stackedWidget.addWidget(self.CandidatePage2)

        self.stackedWidget.setCurrentIndex(0)


        keyboard.add_hotkey('left', lambda: MainScreenSPL.movepage(self, index=0))
        keyboard.add_hotkey('right', lambda: MainScreenSPL.movepage(self, index=1))

        self.setGeometry(0, 0, 1500, 847)
        self.setWindowTitle('Election Application')
        icon = QIcon()
        icon.addPixmap(QPixmap("favi.jpg"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.show()

    def movepage(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def shit_voting(self, candidateindex):
        if self.searchdirectory == "/femaleCandidate":
            self.nominatedfemale = candidateindex
            prompt = QMessageBox(icon=QMessageBox.Question, text=f'You have choosen to nominate {self.candidict["maleSPL"][f"candidate{self.nominatedMale}"]["name"]} and {self.candidict["femaleSPL"][f"candidate{self.nominatedfemale}"]["name"]}\nContinue?')
            prompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returned = prompt.exec_()
            if returned == 16384:
                vote(self.candidict, self.nominatedfemale, 'femaleSPL')
                vote(self.candidict, self.nominatedMale, 'maleSPL')
                conf_prompt = QMessageBox(text = 'Vote Sucessfully Casted')
                conf_prompt.setStandardButtons(QMessageBox.Ok)
                r = conf_prompt.exec_()

                
                pass
            self.searchdirectory = '/maleCandidate'
            self.maintext.setText('Choose your Male \nCandidate [SPL]')
            self.maintext.adjustSize()
            self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face1.png"))
            self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face2.png"))
            self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face3.png"))
            self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face4.png"))
            self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face5.png"))
            self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face6.png"))

        else:
            self.nominatedMale = candidateindex
            self.searchdirectory = '/femaleCandidate'
            self.maintext.setText('Choose your Female \nCandidate [SPL]')
            self.maintext.adjustSize()

            self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face1.png"))

            self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face2.png"))

            self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face3.png"))

            self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face4.png"))

            self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face5.png"))

            self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchdirectory + "/Face6.png"))

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            if self.searchdirectory == '/maleCandidate':
                if object == self.CandiImg1:
                    self.maintext.setText(self.candidict['maleSPL']['candidate1']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg2:
                    self.maintext.setText(self.candidict['maleSPL']['candidate2']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg3:
                    self.maintext.setText(self.candidict['maleSPL']['candidate3']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg4:
                    self.maintext.setText(self.candidict['maleSPL']['candidate4']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg5:
                    self.maintext.setText(self.candidict['maleSPL']['candidate5']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg6:
                    self.maintext.setText(self.candidict['maleSPL']['candidate6']['name'])
                    self.maintext.adjustSize()
            elif self.searchdirectory == '/femaleCandidate':
                if object == self.CandiImg1:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate1']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg2:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate2']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg3:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate3']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg4:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate4']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg5:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate5']['name'])
                    self.maintext.adjustSize()
                elif object == self.CandiImg6:
                    self.maintext.setText(self.candidict['femaleSPL']['candidate6']['name'])
                    self.maintext.adjustSize()
                    
        elif event.type() == QEvent.Leave:
            if self.searchdirectory == '/femaleCandidate':
                self.maintext.setText(" ")
            else:
                self.maintext.setText("Choose your Male \nCandidate [SPL]")
            self.maintext.adjustSize()

        elif event.type() == QEvent.MouseButtonPress:
            if object == self.buttonLeft:
                self.movepage(0)
            elif object == self.buttonRight:
                self.movepage(1)
            elif object == self.CandiImg1:
                self.shit_voting(1)
            elif object == self.CandiImg2:
                self.shit_voting(2)
            elif object == self.CandiImg3:
                self.shit_voting(3)
            elif object == self.CandiImg4:
                self.shit_voting(4)
            elif object == self.CandiImg5:
                self.shit_voting(5)
            elif object == self.CandiImg6:
                self.shit_voting(6)
        return False


    


def vote(dict, candi_index, post):
    from firebase_admin import db
    ref = db.reference(f'/{post}')
    f2 = open('data.json', 'w')
    dict[post][f'candidate{candi_index}']['votes'] += 1
    ref.set(dict[post])
    json.dump(dict, f2, indent=4)
    f2.flush()


if __name__ == '__main__':
    
    try:
        f = open('data.json', 'r')
        d = json.load(f)
        f.close()
    except FileNotFoundError:
        d = {1:11,2:22,3:33}
        f = open('data.json', 'w')
        json.dump(d,f)
        f.close()

    app = QApplication(sys.argv)
    ex = MainScreenSPL()
    sys.exit(app.exec_())


