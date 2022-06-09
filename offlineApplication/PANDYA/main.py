from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os,json

class MainScreenPANDYA(QWidget):
    f = open('../data.json')
    # Some variables to get started
    searchDirectory = '/maleCandidate'
    nominatedMale = 0
    nominatedfemale = 0
    candidict = json.load(f)
    f.close()

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
        self.mainText.setText('Choose your \nMale \nCandidate\n[PANDYA]')


        
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
        if 'Face3.png' in os.listdir(os.getcwd()+self.searchDirectory):
            print('Yes')
        else:
            print('No')
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
        self.cRights.setText('© Akash Shanmugaraj \'22 - Vidhya Niketan Public')

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
                                 text=f'You have choosen to nominate {self.candidict["malePANDYA"][f"candidate{self.nominatedMale}"]["name"]} and {self.candidict["femalePANDYA"][f"candidate{self.nominatedfemale}"]["name"]}\nContinue?')
            prompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returned = prompt.exec_()
            if returned == 16384:
                vote(self.candidict, self.nominatedfemale, 'femalePANDYA')
                vote(self.candidict, self.nominatedMale, 'malePANDYA')
                conf_prompt = QMessageBox(text='Vote Sucessfully Casted')
                conf_prompt.setStandardButtons(QMessageBox.Ok)
                r = conf_prompt.exec_()

                pass
            self.searchDirectory = '/maleCandidate'
            self.mainText.setText('Choose your \nMale \nCandidate\n[PANDYA]')
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
            self.mainText.setText('Choose your \nFemale \nCandidate\n[PANDYA]')
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
        try:
            if event.type() == QEvent.Enter:
                if self.searchDirectory == '/maleCandidate':
                    if object == self.CandiImg1:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate1']['name'])
                    elif object == self.CandiImg2:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate2']['name'])
                    elif object == self.CandiImg3:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate3']['name'])
                    elif object == self.CandiImg4:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate4']['name'])
                    elif object == self.CandiImg5:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate5']['name'])
                    elif object == self.CandiImg6:
                        self.namePlate.setText(self.candidict['malePANDYA']['candidate6']['name'])
                elif self.searchDirectory == '/femaleCandidate':
                    if object == self.CandiImg1:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate1']['name'])
                    elif object == self.CandiImg2:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate2']['name'])
                    elif object == self.CandiImg3:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate3']['name'])
                    elif object == self.CandiImg4:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate4']['name'])
                    elif object == self.CandiImg5:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate5']['name'])
                    elif object == self.CandiImg6:
                        self.namePlate.setText(self.candidict['femalePANDYA']['candidate6']['name'])
                self.namePlate.adjustSize()

            elif QEvent.Leave == event.type():
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
        except KeyError:
            return False

# VoteCasting Function
def vote(dict, candi_index, post):
    dict[post][f'candidate{candi_index}']['votes'] += 1
    f = open('../data.json', 'w')
    json.dump(dict,f)
    f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreenPANDYA()
    sys.exit(app.exec_())