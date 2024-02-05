# DATE : 2024025
# FILE : test_36_pyqt.py
# DESC : PyQt5 기본 화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
## GUI : Graphic User Interface / CLI : Command Line Interface (명령 프롬프트)
from PyQt5.QtWidgets import QApplication, QWidget
#print(sys.argv) # 현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget): # QWidget 을 [상속] 받을거야. QWidget이 가진 모든 것을 사용할 수 있다(상속 개념)
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI()  # 화면 초기화 함수를 호출
        
    def initUI(self):  # 화면 초기화 함수
        self.setGeometry((1920 - 400) //2, (1080 - 300) //2, 400, 300) # x, y, width, height
        self.setWindowTitle('Qt5 Hello world!')
        self.text=''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) # RGB
        paint.setFont(QFont('NanumGothic', 15))
        paint.drawText(300//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text) #AlignLeft, AlignCenter, AlignRight

    def paintEvent(self, event) -> None: # 재정의(Override)
        paint = QPainter()
        paint.begin(self) # 열면
        self.drawText(event, paint)
        paint.end() # 닫는다

loop = QApplication(sys.argv) # 내 소스 위치로 앱을 생성할거야
instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성
loop.exec_()