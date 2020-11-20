from time import sleep
from pathlib import Path, PurePath
from qtpy import QtWidgets, QtCore, QtGui, QtMultimedia
import subprocess
import requests
import clipboard
from widgets import log_reader
from datetime import datetime

FONT_SIZE = 12
ANDROID_LOG_APP_PATH = PurePath.joinpath(Path.cwd(), r"scrcpy-win64/adb.exe").resolve(True)
print(ANDROID_LOG_APP_PATH)
IOS_LOG_APP_PATH = PurePath.joinpath(Path.cwd(), r"iOSLogInfo/sdsiosloginfo.exe").resolve(True)
print(IOS_LOG_APP_PATH)

# TODO Add export to Pastebin
# TODO Add copy pastebin link to the buffer
# TODO Add clear logs button
# TODO Relaunch the app on press of the Connect button
# TODO Add initiate Android button to reconnect the phone's WIFI to the ADB
# TODO Create marks of intereste while recording a video
# V — Verbose (lowest priority)
# D — Debug
# I — Info
# W — Warning
# E — Error
# F — Fatal
# S — Silent (highest priority, on which nothing is ever printed)


def send_to_pastebin(text):
    url = 'https://pastebin.com/api/api_post.php'
    params = {"api_dev_key": '2567264e6a62ce61ab94b9a9c1fa79a8',
              'api_option': 'paste',
              'api_paste_code': text,
              'api_paste_private': 1,
              'api_paste_expire_date': '6M'}
    req = requests.post(url, data=params)
    if req.ok:
        link = req.text
        link_raw = link.replace('pastebin.com/', 'pastebin.com/raw/')
    else:
        raise Exception("Can't get to the pastebin.com")

    return link, link_raw

def get_android_pid():
    path = f'{ANDROID_LOG_APP_PATH} shell pidof -s ai.mybuddy.talkingflashcards_new'
    print(path)
    android_pid = subprocess.Popen(path,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

    for line in android_pid.stdout:
        android_pid = line.strip()
        break
    return android_pid


class LogViewWidget(log_reader.UILogReader):
    def __init__(self):
        super(LogViewWidget, self).__init__()

        self.resize(754, 904-29)
        self.DATA_SOURCE_FLAG = None

        # QProcess object for external app
        self.process = QtCore.QProcess(self)
        # print('Process created')
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)
        # print('Process connected')

        self.btn_save_logs.setText('Send to pastebin')

        self.btn_connect_android.pressed.connect(self.get_logs_from_android)
        self.btn_connect_ios.pressed.connect(self.get_logs_from_ios)
        self.btn_save_logs.pressed.connect(self.pastebin_send_logs)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_time)
        # self.connect(timer, SIGNAL("timeout()"), self.update)
        timer.start(100)

    def update_time(self):
        self.label_current_time.setText(f'Current date-time: {str(datetime.now())[:-3]}')

    def closeEvent(self, QCloseEvent):
        self.process.kill()

    @staticmethod
    def clean_line_ios(line: str):
        line_split = line.split()
        del line_split[0]  # Del Month
        del line_split[0]  # Del Day
        try:
            del line_split[1]  # Del Device
        except IndexError:
            pass
        return ' '.join(line_split).replace('talkingflashcards', 'Ѡ').replace(' <Notice>', '')

    def dataReady(self):
        print('Data is ready')
        cursor = self.qtext_logscreen.textCursor()
        cursor.movePosition(cursor.End)
        x = self.process.readAll()
        print(x)
        x = str(x, 'utf-8')
        default_font = QtGui.QTextCharFormat()
        default_font.setFontPointSize(FONT_SIZE)
        white = QtGui.QTextCharFormat(default_font)
        red = QtGui.QTextCharFormat(default_font)
        red.setBackground(QtGui.QColor('#cf0000'))
        black = QtGui.QTextCharFormat(default_font)
        black.setBackground(QtGui.QColor('#000000'))
        orange = QtGui.QTextCharFormat(default_font)
        orange.setForeground(QtGui.QColor('#ff7354'))
        orange_bg = QtGui.QTextCharFormat(default_font)
        orange_bg.setBackground(QtGui.QColor('#b03b00'))
        green = QtGui.QTextCharFormat(default_font)
        green.setBackground(QtGui.QColor('#045c0f'))
        dark_blue = QtGui.QTextCharFormat(default_font)
        dark_blue.setBackground(QtGui.QColor('#00183d'))
        notice_clr = QtGui.QTextCharFormat(default_font)
        notice_clr.setForeground(QtGui.QColor('#ee9900'))
        UnityIAP = QtGui.QTextCharFormat(default_font)
        UnityIAP.setBackground(QtGui.QColor('#29004f'))
        color_dict_android = {'E': red, 'I': orange, 'D': black, 'V': black, 'W': black}
        color_dict_ios = {'<Error>:': red, '<placeholder>:': dark_blue, '[UNITY_IAP]': UnityIAP, 'UnityIAP': UnityIAP}
        color_dict_events = {'SpawnAttractedFish': green, 'NLU': orange}
        color_dict = color_dict_ios if self.DATA_SOURCE_FLAG == 'IOS' else color_dict_android

        line_color = None

        for line in x.splitlines():
            # print(f'DATA_SOURCE_FLAG IS SET TO {self.DATA_SOURCE_FLAG}')
            if self.DATA_SOURCE_FLAG == 'IOS':
                if 'searchpartyd' in line or 'ssert' in line or 'etwork' in line or 'mediaserverd' in line \
                        or 'rapportd' in line or 'kernel' in line or 'dasd' in line \
                        or 'symptomsd' in line or 'nsurlsessiond' in line or 'sharingd' in line \
                        or 'bluetoothd' in line \
                        or 'libusrtcp' in line \
                        or 'libboringssl' in line \
                        or 'corecapture' in line:
                    continue
                elif 'talkingflashcards' not in line:
                    continue
                elif 'CoreBrightness' in line:
                    continue
                elif 'renderDeadlineHistogram' in line:
                    continue
                elif 'mediaserverd' in line:
                    continue
                elif 'WiFiPolicy' in line:
                    continue
                elif 'Bucket count' in line:
                    continue
                elif '%' in line:
                    continue

            if self.DATA_SOURCE_FLAG == 'ANDROID':
                if 'Line: 51' in line:
                    continue
                elif line.endswith('Unity   :'):
                    continue
                elif line.endswith('Unity   : '):
                    continue
                elif line.endswith('Unity   :  '):
                    continue
                elif 'Unity' not in line:
                    continue
            #     elif '[Server Response]' not in line:
            #         continue
            #
            #     # line = line.split('<Notice>: ')[-1]
            #     # line_color = notice_clr

            for key in color_dict.keys():
                # if key in line.split():
                # print(key)
                # print(line.split()[:6])
                if len([s for s in line.split()[:6] if key in s]):
                    # print(key, line.split())
                    line_color = color_dict[key]
                    break
                else:
                    line_color = white

            for key in color_dict_events.keys():
                # print(key, line.split())
                if len([s for s in line.split()[6:] if key in s]):
                    line_color = color_dict_events[key]
                    break
                else:
                    line_color = white

            line = self.__class__.clean_line_ios(line)

            cursor.insertText(line+'\n', line_color or white)
        self.qtext_logscreen.ensureCursorVisible()

    def get_logs_from_android(self):
        self.DATA_SOURCE_FLAG = 'ANDROID'
        # run the process
        # `start` takes the exec and a list of arguments
        # self.process.start('ping',['127.0.0.1'])
        if self.process.isOpen():
            self.process.kill()
            self.qtext_logscreen.clear()
            print('process is open',self.process.isOpen())
        exe_line = f'"{ANDROID_LOG_APP_PATH}" logcat --pid={get_android_pid()}'
        print(exe_line)
        print(self.process.start(exe_line))

    def get_logs_from_ios(self):
        # run the process
        # `start` takes the exec and a list of arguments
        # self.process.start('ping',['127.0.0.1'])
        self.DATA_SOURCE_FLAG = 'IOS'
        if self.process.isOpen():
            self.process.kill()
            self.qtext_logscreen.clear()
            print('process is open', self.process.isOpen())
        self.process.start(str(IOS_LOG_APP_PATH))

    def pastebin_send_logs(self):
        if self.qtext_logscreen.toPlainText():
            link = send_to_pastebin(self.qtext_logscreen.toPlainText())
            raw_link = link[1]
            print(raw_link)
            clipboard.copy(raw_link)

        else:
            import sys
            print('No text to send')
            # alert = QtMultimedia.QMediaPlayer()
            # alert.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile('ok.wav')))
            # # print(alert.isLoaded())
            # print(alert.volume())
            # # print(alert.source())
            # # alert.setLoopCount(1)
            # # alert.setVolume(1)
            # alert.play()
            # # print(alert.isLoaded())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
import sys
sys.excepthook = except_hook
app = QtWidgets.QApplication([])
widget = LogViewWidget()
widget.show()
app.exec()
