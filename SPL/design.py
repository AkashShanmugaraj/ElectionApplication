# do `pip install PyQt5`
# do `pip install PyQt5`
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os

class MainScreenSPL(QWidget):
    global ref
    # Initializing Firebase connection
    import firebase_admin
    from firebase_admin import db
    cred_obj = firebase_admin.credentials.Certificate('electionvnps-firebase-adminsdk-3ypv5-52c9b529b4.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL': 'https://electionvnps-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    # Setting current working directory to "root"
    ref = db.reference("/")

    # Some variables to get started
    searchDirectory = '/maleCandidate'
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
        # Palette
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)

        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        self.setPalette(palette)
        self.setGeometry(0, 0, 1500, 847)
        self.setWindowTitle('Election Application - Vidhya Niketan')

        # Frame1
        self.textFrame = QFrame(self)
        self.textFrame.setGeometry(QRect(30, 30, 431, 791))
        self.textFrame.setFrameShape(QFrame.StyledPanel)
        self.textFrame.setFrameShadow(QFrame.Plain)

        self.mainText = QLabel(self.textFrame)
        self.mainText.setGeometry(QRect(10, 440, 431, 311))
        font = QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(39)
        self.mainText.setFont(font)
        self.mainText.setText('Choose your \nMale \nCandidate\n[SPL]')


        
        #Frame2
        self.CandidateFrame = QFrame(self)
        self.CandidateFrame.setGeometry(QRect(469, 29, 1011, 791))
        self.CandidateFrame.setFrameShape(QFrame.StyledPanel)
        self.CandidateFrame.setFrameShadow(QFrame.Plain)

        # Candidate
        self.CandiImg1 = QLabel(self.CandidateFrame)
        self.CandiImg1.setGeometry(QRect(80, 100, 261, 261))
        self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face1.png"))
        self.CandiImg1.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg1, index=1, subdir=self.searchDirectory)


        # Candidate
        self.CandiImg2 = QLabel(self.CandidateFrame)
        self.CandiImg2.setGeometry(QRect(400, 100, 261, 261))
        self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face2.png"))
        self.CandiImg2.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg2, index=2, subdir=self.searchDirectory)

        # Candidate
        self.CandiImg3 = QLabel(self.CandidateFrame)
        self.CandiImg3.setGeometry(QRect(720, 100, 261, 261))
        self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face3.png"))
        self.CandiImg3.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg3, index=3, subdir=self.searchDirectory)

        # Candidate
        self.CandiImg4 = QLabel(self.CandidateFrame)
        self.CandiImg4.setGeometry(QRect(80, 430, 261, 261))
        self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face4.png"))
        self.CandiImg4.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg4, index=4, subdir=self.searchDirectory)

        # Candidate
        self.CandiImg5 = QLabel(self.CandidateFrame)
        self.CandiImg5.setGeometry(QRect(400, 430, 261, 261))
        self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face5.png"))
        self.CandiImg5.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg5, index=5, subdir=self.searchDirectory)

        # Candidate
        self.CandiImg6 = QLabel(self.CandidateFrame)
        self.CandiImg6.setGeometry(QRect(720, 430, 261, 261))
        self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face6.png"))
        self.CandiImg6.setScaledContents(True)
        self.eventfilterassignment(object=self.CandiImg6, index=6, subdir=self.searchDirectory)

        # NamePlate
        self.namePlate = QLabel(self.CandidateFrame)
        self.namePlate.setGeometry(QRect(10, 19, 991, 31))
        font = QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(21)
        self.namePlate.setFont(font)
        self.namePlate.setAlignment(Qt.AlignHCenter)

        # CopyRights Banner
        self.cRights = QLabel(self)
        self.cRights.setGeometry(QRect(1200, 820, 291, 20))
        self.cRights.setText('?? Akash Shanmugaraj \'22 - Vidhya Niketan Public')

        # School Logo
        self.schoolLogo = QLabel(self.textFrame)
        self.schoolLogo.setGeometry(QRect(97, 60, 211, 211))
        self.schoolLogo.setPixmap(QPixmap('Logo_VNPS.png'))
        self.schoolLogo.setScaledContents(True)
        self.show()


    def shiftVoting(self, candidateindex):
        if self.searchDirectory == "/femaleCandidate":
            self.nominatedfemale = candidateindex
            prompt = QMessageBox(icon=QMessageBox.Question,
                                 text=f'You have choosen to nominate {self.candidict["maleSPL"][f"candidate{self.nominatedMale}"]["name"]} and {self.candidict["femaleSPL"][f"candidate{self.nominatedfemale}"]["name"]}\nContinue?')
            prompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returned = prompt.exec_()
            if returned == 16384:
                vote(self.candidict, self.nominatedfemale, 'femaleSPL')
                vote(self.candidict, self.nominatedMale, 'maleSPL')
                conf_prompt = QMessageBox(text='Vote Sucessfully Casted')
                conf_prompt.setStandardButtons(QMessageBox.Ok)
                r = conf_prompt.exec_()

                pass
            self.searchDirectory = '/maleCandidate'
            self.mainText.setText('Choose your \nMale \nCandidate\n[SPL]')
            self.mainText.adjustSize()
            self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face1.png"))
            self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face2.png"))
            self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face3.png"))
            self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face4.png"))
            self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face5.png"))
            self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face6.png"))

        else:
            self.nominatedMale = candidateindex
            self.searchDirectory = '/femaleCandidate'
            self.mainText.setText('Choose your \nFemale \nCandidate\n[SPL]')
            self.mainText.adjustSize()
            self.namePlate.setText('<hover again for name>')
            self.adjustSize()
            self.CandiImg1.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face1.png"))

            self.CandiImg2.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face2.png"))

            self.CandiImg3.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face3.png"))

            self.CandiImg4.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face4.png"))

            self.CandiImg5.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face5.png"))

            self.CandiImg6.setPixmap(QPixmap(os.getcwd() + self.searchDirectory + "/Face6.png"))

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            if self.searchDirectory == '/maleCandidate':
                if object == self.CandiImg1:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate1']['name'])
                elif object == self.CandiImg2:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate2']['name'])
                elif object == self.CandiImg3:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate3']['name'])
                elif object == self.CandiImg4:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate4']['name'])
                elif object == self.CandiImg5:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate5']['name'])
                elif object == self.CandiImg6:
                    self.namePlate.setText(self.candidict['maleSPL']['candidate6']['name'])
            elif self.searchDirectory == '/femaleCandidate':
                if object == self.CandiImg1:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate1']['name'])
                elif object == self.CandiImg2:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate2']['name'])
                elif object == self.CandiImg3:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate3']['name'])
                elif object == self.CandiImg4:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate4']['name'])
                elif object == self.CandiImg5:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate5']['name'])
                elif object == self.CandiImg6:
                    self.namePlate.setText(self.candidict['femaleSPL']['candidate6']['name'])
            self.namePlate.adjustSize()

        elif event.type() == QEvent.Leave:
            if self.searchDirectory == '/femaleCandidate':
                self.namePlate.setText(" ")
            else:
                self.namePlate.setText(" ")
            self.namePlate.adjustSize()

        elif event.type() == QEvent.MouseButtonPress:
            if object == self.CandiImg1:
                self.shiftVoting(1)
            elif object == self.CandiImg2:
                self.shiftVoting(2)
            elif object == self.CandiImg3:
                self.shiftVoting(3)
            elif object == self.CandiImg4:
                self.shiftVoting(4)
            elif object == self.CandiImg5:
                self.shiftVoting(5)
            elif object == self.CandiImg6:
                self.shiftVoting(6)
        return False

# VoteCasting Function
def vote(dict, candi_index, post):
    from firebase_admin import db
    ref = db.reference(f'/{post}')
    dict[post][f'candidate{candi_index}']['votes'] += 1
    ref.set(dict[post])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreenSPL()
    sys.exit(app.exec_())
