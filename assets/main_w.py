from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_ui import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import threading
import time
import json
from googleapiclient.discovery import build

from core import Yengine
from settings import 

class MyMainWindow(QMainWindow, Yengine):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cycle = False
        self.ui.startBtn.clicked.connect(self.on_button_click_start)
        self.ui.stopBtn.clicked.connect(self.on_button_click_stop)
        self.ui.clearBtn.clicked.connect(self.on_button_click_clear)
        cash = self.cash_load()
        self.ui.first_audio_path.setText(cash["first"]["audio"])
        self.ui.first_script_path.setText(cash["first"]["script"])
        self.ui.second_audio_path.setText(cash["second"]["audio"]) 
        self.ui.second_script_path.setText(cash["second"]["script"])
        self.ui.lineEdit.setText(str(cash["interval"]))
        self.ui.editPromt.setPlainText(cash["promt"])
        self.stream_id = self.ui.streamid.text()
        self.promt_queue = []

    def load_cash(self):
        try:
            with open("path.json", "r", encoding='utf-8-sig') as file:
                data = json.load(file)
            self.ui.first_audio_path.setText(data["first"]["audio"])
            self.ui.first_script_path.setText(data["first"]["script"])
            self.ui.second_audio_path.setText(data["second"]["audio"])
            self.ui.second_script_path.setText(data["second"]["script"])
            self.ui.lineEdit.setText(str(data["interval"]))
            self.ui.editPromt.setPlainText(data["promt"])
            self.stream_id = self.ui.streamid.text()
            self.promt_queue = []
        except FileNotFoundError:
            self.ui.console.append("Не найден кэш-файл.")

    def save_cash(self):
        """
        Метод для сохранения кэша.
        """
        data = {
            "first": {
                "audio": self.ui.first_audio_path.text(),
                "script": self.ui.first_script_path.text()
            },
            "second": {
                "audio": self.ui.second_audio_path.text(),
                "script": self.ui.second_script_path.text()
            },
            "interval": self.ui.lineEdit.text(),
            "promt": self.ui.editPromt.toPlainText()
        }
        with open("path.json", "w", encoding='utf-8-sig') as file:
            json.dump(data, file)

    def yt_theme_request(self, stream_id):
        """
        Запрос на получение новых тем из чата Ютуба.
        """
        try:
            youtube = build('youtube', 'v3', developerKey=self.api_key)
            video_id = stream_id
            response = youtube.videos().list(part='liveStreamingDetails', id=video_id).execute()
            chat_id = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
            chat = youtube.liveChatMessages().list(part='snippet', liveChatId=chat_id)
            ms_list = self.load_donation_history()
            messages = chat.execute()
            for message in messages['items']:
                etag = message['etag']
                text = message['snippet']['displayMessage']
                if text.startswith("/тема") and etag not in ms_list:
                    theme = text[len('/тема'):]
                    res_list = [theme.strip(), etag]
                    return res_list
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        return False

    def generate_helper(self, dir_promt, theme=None, etag=None):
        """
        Метод для генерации ресурсов.
        """
        if self.folder_status("first"):
            self.ui.console.append("Первая папка доступна для приёма файлов.")
            self.ui.console.append("Начинаю генерацию.")
            self.generated("first", dir_promt, theme)
            self.ui.console.append("Генерация завершена успешно.")
            if etag:
                self.save_donation_history(etag)
        elif self.folder_status("second"):
            self.ui.console.append("Вторая папка доступна для приёма файлов.")
            self.ui.console.append("Начинаю генерацию.")
            self.generated("second", dir_promt, theme)
            self.ui.console.append("Генерация завершена успешно.")
            if etag:
                self.save_donation_history(etag)

    def startapp(self):
        """
        Запуск программы.
        """
        self.ui.console.append("Програма запущенна. Сохранение кэша.")
        self.save_cash()
        self.ui.console.append("Кэш сохранён.")
        self.stream_id = self.ui.streamid.text()
        dir_promt = self.ui.editPromt.toPlainText()
        while self.cycle:
            self.ui.console.append("Проверка статуса Unity.")
            if self.unity_status():
                self.ui.console.append("Unity готова.")
                yt_theme = self.yt_theme_request(self.stream_id)
                if yt_theme:
                    self.ui.console.append(f"Генерация диалога на тему: {yt_theme[0]}.")
                    self.generate_helper(dir_promt, yt_theme[0], yt_theme[1])
                else:
                    self.ui.console.append("Подготовка свободной темы.")
                    self.generate_helper(dir_promt)
            else:
                self.ui.console.append("Unity не готова к приёму файлов.")
                self.ui.console.append(f"Ожидаю {self.ui.lineEdit.text()} секунд(ы)")
                time.sleep(int(self.ui.lineEdit.text()))
                continue

    @pyqtSlot()
    def on_button_click_start(self):
        if not self.cycle:
            self.cycle = True
            threading.Thread(target=self.startapp).start()
        else:
            self.ui.console.append("Поток уже запущен.")

    @pyqtSlot()
    def on_button_click_stop(self):
        self.cycle = False
        self.ui.console.append("Поиск остановлен")

    @pyqtSlot()
    def on_button_click_clear(self):
        self.ui.console.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()