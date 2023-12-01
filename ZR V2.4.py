from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
import os
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu
import threading
from win10toast import ToastNotifier
import requests
from ctypes import windll
import tempfile
import configparser
from PyQt5.QtWidgets import QColorDialog


def download_icon(url, save_path):
    if os.path.exists(save_path):
        print(f"The file already exists at {save_path}. Skipping download.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  


        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, 'temp_icon.ico')

        with open(temp_path, 'wb') as file:
            file.write(response.content)


        os.rename(temp_path, save_path)

        print(f"File downloaded successfully and saved at {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


icon_url = "https://cdn.discordapp.com/attachments/1139623869632757972/1177447657363488878/ZR.ico?ex=65728a95&is=65601595&hm=042e18174f92bd6fb7cbdf11be3a20de93dcd40001570f7ee044d4de7620ee82&"


save_path = os.path.join(tempfile.gettempdir(), 'ZR_icon.ico')

download_icon(icon_url, save_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Z7LLres")
        MainWindow.setWindowTitle("Z7LLres")
        MainWindow.resize(294, 351)
        MainWindow.setMinimumSize(QtCore.QSize(294, 351))
        MainWindow.setMaximumSize(QtCore.QSize(294, 351))
        MainWindow.setBaseSize(QtCore.QSize(294, 351))
        MainWindow.setStyleSheet("border-radius:6px;\n"
"background-color: rgb(94, 24, 155)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        tryicon = QSystemTrayIcon (QIcon(save_path), parent=MainWindow)
        tryicon.setToolTip('Z7LLres')
        tryicon.show()

        menu = QMenu()

        ShowAction = menu.addAction('Show')
        exitAction = menu.addAction('Quit ZR')
        exitAction.triggered.connect(lambda: MainWindow.exit())
        ShowAction.triggered.connect(lambda: MainWindow.showNormal())
        


        menu_style = """
        QMenu {
        background-color: rgb(41, 42, 45);
        border: 1px rgb(41, 42, 45);
        border-radius:3px;
        box-shadow: 3px rgba(41, 42, 45, 0.5);
    }

     QMenu::item:selected {
        background-color: rgba(255, 255, 255, 0.15); /* Gray color when hovering */
    }
        QMenu::item {
        color: white;
    }
"""

        menu.setStyleSheet(menu_style)

        tryicon.setContextMenu(menu)


        tryicon.activated.connect(lambda reason: MainWindow.showNormal() if reason == QSystemTrayIcon.Trigger else None)

        MainWindow.setWindowIcon(QIcon(save_path))

        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.MainExit = QtWidgets.QPushButton(self.centralwidget)
        self.MainExit.setGeometry(QtCore.QRect(270, 10, 21, 20))
        self.MainExit.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: #FF605C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c84a48;\n"
"}")
        self.MainExit.setText("")
        self.MainExit.setObjectName("MainExit")
        self.minimize = QtWidgets.QPushButton(self.centralwidget)
        self.minimize.setGeometry(QtCore.QRect(240, 10, 21, 20))
        self.minimize.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: #FFBD44;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c89235;\n"
"}")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.Width = QtWidgets.QLabel(self.centralwidget)
        self.Width.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.Width.setStyleSheet("font: 81 15pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.Width.setObjectName("Width")
        self.Height = QtWidgets.QLabel(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(110, 40, 71, 31))
        self.Height.setStyleSheet("font: 81 15pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.Height.setObjectName("Height")
        self.FPS = QtWidgets.QLabel(self.centralwidget)
        self.FPS.setGeometry(QtCore.QRect(210, 40, 41, 31))
        self.FPS.setStyleSheet("font: 81 15pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.FPS.setObjectName("FPS")
        self.Width_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Width_LineEdit.setGeometry(QtCore.QRect(20, 80, 61, 20))
        self.Width_LineEdit.setMouseTracking(True)
        self.Width_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 16, 103);")
        self.Width_LineEdit.setInputMask("")
        self.Width_LineEdit.setText("")
        self.Width_LineEdit.setMaxLength(4)
        self.Width_LineEdit.setFrame(True)
        self.Width_LineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Width_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Width_LineEdit.setDragEnabled(False)
        self.Width_LineEdit.setClearButtonEnabled(False)
        self.Width_LineEdit.setObjectName("Width_LineEdit")
        self.Height_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Height_LineEdit.setGeometry(QtCore.QRect(110, 80, 61, 20))
        self.Height_LineEdit.setMouseTracking(True)
        self.Height_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 16, 103);")
        self.Height_LineEdit.setInputMask("")
        self.Height_LineEdit.setText("")
        self.Height_LineEdit.setMaxLength(4)
        self.Height_LineEdit.setFrame(True)
        self.Height_LineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Height_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_LineEdit.setDragEnabled(False)
        self.Height_LineEdit.setClearButtonEnabled(False)
        self.Height_LineEdit.setObjectName("Height_LineEdit")
        self.FPS_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FPS_LineEdit.setGeometry(QtCore.QRect(200, 80, 61, 20))
        self.FPS_LineEdit.setMouseTracking(True)
        self.FPS_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 16, 103);")
        self.FPS_LineEdit.setInputMask("")
        self.FPS_LineEdit.setText("")
        self.FPS_LineEdit.setMaxLength(4)
        self.FPS_LineEdit.setFrame(True)
        self.FPS_LineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.FPS_LineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FPS_LineEdit.setDragEnabled(False)
        self.FPS_LineEdit.setClearButtonEnabled(False)
        self.FPS_LineEdit.setObjectName("FPS_LineEdit")
        self.Window_Mode = QtWidgets.QLabel(self.centralwidget)
        self.Window_Mode.setGeometry(QtCore.QRect(70, 140, 151, 31))
        self.Window_Mode.setStyleSheet("font: 81 15pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.Window_Mode.setObjectName("Window_Mode")
        self.Fullscreen = QtWidgets.QRadioButton(self.centralwidget)
        self.Fullscreen.setGeometry(QtCore.QRect(30, 180, 91, 20))
        self.Fullscreen.setStyleSheet("font: 87 10pt \"Montserrat Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.Fullscreen.setObjectName("Fullscreen")
        self.Fullscreen_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.Fullscreen_2.setGeometry(QtCore.QRect(30, 210, 171, 20))
        self.Fullscreen_2.setStyleSheet("font: 87 10pt \"Montserrat Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.Fullscreen_2.setObjectName("Fullscreen_2")
        self.Fullscreen_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.Fullscreen_3.setGeometry(QtCore.QRect(30, 240, 101, 20))
        self.Fullscreen_3.setStyleSheet("font: 87 10pt \"Montserrat Black\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.Fullscreen_3.setObjectName("Fullscreen_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 300, 71, 17))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.Change_Menu = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Menu.setGeometry(QtCore.QRect(10, 320, 271, 21))
        self.Change_Menu.setStyleSheet("QPushButton {\n"
"background-color: #4c1283;\n"
"font: 81 12pt \"Muli ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #350d5a\n"
"\n"
"}")
        self.Change_Menu.setObjectName("Change_Menu")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 150, 51, 5))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(230, 150, 51, 5))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 150, 5, 140))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(280, 150, 5, 140))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 290, 275, 5))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Help = QtWidgets.QPushButton(self.centralwidget)
        self.Help.setGeometry(QtCore.QRect(210, 10, 21, 20))
        self.Help.setStyleSheet("\n"
"QPushButton{\n"
"    border-radius:10px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #e2e2e2;\n"
"}")
        self.Help.setObjectName("Help")
        self.RGB = QtWidgets.QPushButton(self.centralwidget)
        self.RGB.setGeometry(QtCore.QRect(10, 10, 21, 20))
        self.RGB.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")
        self.RGB.setText("")
        self.RGB.setObjectName("RGB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Z7LLres"))
        self.Width.setText(_translate("MainWindow", "Width"))
        self.Height.setText(_translate("MainWindow", "Height"))
        self.FPS.setText(_translate("MainWindow", "FPS"))
        self.Width_LineEdit.setPlaceholderText(_translate("MainWindow", "1920"))
        self.Height_LineEdit.setPlaceholderText(_translate("MainWindow", "1080"))
        self.FPS_LineEdit.setPlaceholderText(_translate("MainWindow", "165"))
        self.Window_Mode.setText(_translate("MainWindow", "Window Mode"))
        self.Fullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.Fullscreen_2.setText(_translate("MainWindow", "Windowed Fullscreen"))
        self.Fullscreen_3.setText(_translate("MainWindow", "Windowed"))
        self.checkBox.setText(_translate("MainWindow", "Read-only"))
        self.Change_Menu.setText(_translate("MainWindow", "Apply"))
        self.Help.setText(_translate("MainWindow", "?"))

        self.Change_Menu.clicked.connect(self.show_message)
        self.minimize.clicked.connect(self.show_notification)
        self.minimize.clicked.connect(lambda: MainWindow.hide())
        self.MainExit.clicked.connect(lambda: MainWindow.exit())
        self.Change_Menu.clicked.connect(self.save_config)
        self.Help.clicked.connect(self.showInstructions)
        self.RGB.clicked.connect(self.showColorDialog)

        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = True
            self.dragPosition = event.globalPos() - MainWindow.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.isDragging:
            MainWindow.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = False

    def darkenColor(self, color, factor):

        h, s, l, a = color.getHslF()
        new_l = max(0, l - factor / 100.0)
        darker_color = QColor.fromHslF(h, s, new_l, a)
        return darker_color
    
    def showColorDialog(self):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()

        if color.isValid():
            MainWindow.setStyleSheet("border-radius:6px;\n"
                                    "background-color: {}".format(color.name()))
            
            darker_color = self.darkenColor(color, 25)
            
            self.Width_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            f"background-color: {darker_color.name()};")
            self.Height_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            f"background-color: {darker_color.name()};")
            self.FPS_LineEdit.setStyleSheet("font: 81 10pt \"Muli ExtraBold\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            f"background-color: {darker_color.name()};")
            
            self.Change_Menu.setStyleSheet("QPushButton {\n"
                                        f"background-color: {darker_color.name()};\n"
                                        "font: 81 12pt \"Muli ExtraBold\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                            f"background-color: {darker_color.name()};\n"
                                        "}\n")
        else:
            print("Invalid color selected.")

    def showInstructions(self):
        windll.user32.MessageBoxW(0, "Recommended Stretch Resolutions:\n"
                                      "1411X1070\n"
                                      "1280X1080\n"
                                      "1680X1050 or 1680X1080\n"
                                      "1720X1080 or 1722X1080", "Instructions", 0x40)
        
    def show_message(self):

        windll.user32.MessageBoxW(0, "The resolution is Successfully set", "Success", 64)

    def show_notification(self):
        notification_title = "Z7LLres"
        notification_message = "ZR now hidden."

        icon_path = save_path
        

        notification_thread = threading.Thread(target=self.show_notification_thread, args=(notification_title, notification_message, icon_path))
        notification_thread.start()

    def show_notification_thread(self, title, message, icon_path):
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5, icon_path=icon_path)

    def save_config(self):

        resolution_size_x = self.Width_LineEdit.text()
        resolution_size_y = self.Height_LineEdit.text()
        frame_rate_limit = self.FPS_LineEdit.text()


        if self.Fullscreen.isChecked():
            window_mode = '0'
        elif self.Fullscreen_2.isChecked():
            window_mode = '1'
        elif self.Fullscreen_3.isChecked():
            window_mode = '2'
        else:
            self.result_label.setText("Please select a window mode.")
            return


        self.edit_ini_file(resolution_size_x, resolution_size_y, frame_rate_limit, resolution_size_x, resolution_size_y, window_mode)



    def edit_ini_file(self, resolution_size_x, resolution_size_y, frame_rate_limit, desired_screen_width, desired_screen_height, window_mode):

        ini_file_path = os.path.join(os.getenv('LOCALAPPDATA'), 'FortniteGame', 'Saved', 'Config', 'WindowsClient', 'GameUserSettings.ini')


        os.chmod(ini_file_path, os.stat(ini_file_path).st_mode | 0o222)


        config = configparser.ConfigParser(interpolation=None)


        config.optionxform = lambda option: option  
        config.read(ini_file_path)


        section = '/Script/FortniteGame.FortGameUserSettings'
        config.set(section, 'ResolutionSizeX', str(resolution_size_x))
        config.set(section, 'ResolutionSizeY', str(resolution_size_y))
        config.set(section, 'LastUserConfirmedResolutionSizeX', str(resolution_size_x))
        config.set(section, 'LastUserConfirmedResolutionSizeY', str(resolution_size_y))
        config.set(section, 'FrameRateLimit', str(frame_rate_limit))
        config.set(section, 'DesiredScreenWidth', str(desired_screen_width))
        config.set(section, 'DesiredScreenHeight', str(desired_screen_height))
        config.set(section, 'LastUserConfirmedDesiredScreenWidth', str(desired_screen_width))
        config.set(section, 'LastUserConfirmedDesiredScreenHeight', str(desired_screen_height))
        config.set(section, 'LastConfirmedFullscreenMode', window_mode)
        config.set(section, 'PreferredFullscreenMode', window_mode)
        config.set(section, 'FullscreenMode', window_mode)

        with open(ini_file_path, 'w') as config_file:
            config.write(config_file, space_around_delimiters=False)


        os.chmod(ini_file_path, os.stat(ini_file_path).st_mode & ~0o222)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
