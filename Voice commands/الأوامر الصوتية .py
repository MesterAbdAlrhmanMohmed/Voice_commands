from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import speech_recognition as sr
import os,winsound,about
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("الأوامر الصوتية")
        self.التحدث=qt.QPushButton("بدء التحدث")
        self.التحدث.setDefault(True)
        self.التحدث.clicked.connect(self.ha)
        self.عن=qt.QPushButton("عن المطور")
        self.عن.setDefault(True)
        self.عن.clicked.connect(self.about)
        l=qt.QVBoxLayout()
        l.addWidget(self.التحدث)
        l.addWidget(self.عن)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)                
    def about(self):
        about.dialog(self).exec()
    def ha(self):
        self.command = self.recognize_speech_from_mic()
        if self.command:
            self.execute_command(self.command)
    def recognize_speech_from_mic(self):
        recognizer=sr.Recognizer()
        microphone=sr.Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            winsound.PlaySound("1.wav",1)
            audio=recognizer.listen(source)
        try:
            transcription=recognizer.recognize_google(audio, language="ar-SA")
            return transcription
        except sr.UnknownValueError:
            qt.QMessageBox.warning(self,"تنبيه","غير قاضر على التعرف على الأمر")
            return None
    def execute_command(self, command):
        if "المتجر" in command:
            os.system("start ms-windows-store:")
        elif "المتصفح" in command:
            os.system("start chrome")
        elif "المفكره" in command:
            os.system("notepad")
        elif "مستكشف الملفات" in command:
            os.system("explorer")
        elif "الآله الحاسبه" in command:
            os.system("calc")
        elif "مشغل الوسائط" in command:
            os.system("start wmplayer")
        elif "لوحه التحكم" in command:
            os.system("control")
        elif "مدير المهام" in command:
            os.system("taskmgr")
        elif "البريد الالكتروني" in command:
            os.system("start outlook")
        elif "التقويم" in command:
            os.system("start outlookcal:")
        elif "الاعدادات" in command:
            os.system("start ms-settings:")
        elif "الحمايه" in command:
            os.system("start windowsdefender:")
        elif "اعاده تشغيل الكمبيوتر" in command:
            os.system("shutdown /r /t 0")
        elif "ايقاف تشغيل الكمبيوتر" in command:
            os.system("shutdown /s /t 0")
        elif "قفل الكمبيوتر" in command:
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "ايدج" in command:
            os.system("start msedge")
        elif "الرسام" in command:
            os.system("mspaint")
        elif "ورد" in command:
            os.system("start winword")
        elif "اكسل" in command:
            os.system("start excel")
        elif "باوربوينت" in command:
            os.system("start powerpnt")
        elif "اكسس" in command:
            os.system("start msaccess")
        elif "الكاميرا" in command:
            os.system("start microsoft.windows.camera:")
        elif "خرائط" in command:
            os.system("start bingmaps:")
        elif "الساعه" in command:
            os.system("start ms-clock:")
        elif "الحاسوب" in command:
            os.system("explorer /select,\"C:\\\"")
        elif "التنزيلات" in command:
            os.system("explorer shell:Downloads")
        elif "المستندات" in command:
            os.system("start shell:DocumentsLibrary")
        elif "سطح المكتب" in command:
            os.system("explorer shell:Desktop")
        elif "الملفات المؤقته" in command:
            os.system("explorer shell:Cache")
        else:
            qt.QMessageBox.warning(self, "تنبيه", "هذا أمر غير معروف")            
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()