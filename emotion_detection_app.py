import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction

class EmotionDetectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title and icon for the window
        self.setWindowTitle('Emotion_ Detection_ App')
        self.setWindowIcon(QIcon('icon.png'))

        # Create a button to start emotion detection
        self.startButton = QPushButton('Start Emotion Detection', self)
        self.startButton.clicked.connect(self.startEmotionDetection)

        # Create a layout and add the button
        layout = QVBoxLayout()
        layout.addWidget(self.startButton)
        self.setLayout(layout)

        # Set the size of the window
        self.setGeometry(100, 100, 300, 350)

        # Set up the system tray icon
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon('icon.png'))
        self.trayIcon.setVisible(True)

        # Create a menu for the system tray icon
        trayMenu = QMenu()
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(QCoreApplication.instance().quit)
        trayMenu.addAction(exitAction)
        self.trayIcon.setContextMenu(trayMenu)

    def startEmotionDetection(self):
        try:
            # Start the emotion detection script
            subprocess.Popen(["python","janishya.py"])
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to start emotion detection: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EmotionDetectionApp()
    ex.show()
    sys.exit(app.exec_())
