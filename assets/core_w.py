import os
import requests
import g4f
import json
import portalocker
import time
from gradio_client import Client
from googleapiclient.discovery import build

from settings import HISTORY_FILE

class HistoryManager():
    """
    Менеджер обработки кэша приложения.
    """
    def load_history(self):
        """
        Метод для загрузки ранее обработанных тем.
        """
        while True:
            try:
                with open(HISTORY_FILE, "r") as file:
                    with portalocker.Lock(file, portalocker.LOCK_SH):
                        return set(line.strip() for line in file)
            except FileNotFoundError:
                print("Не обнаружен файл theme_history.txt")
                return False
            except Exception as e:
                print(f"Ошибка при чтении из файла: {str(e)}")
                time.sleep(1)

    def save_history(self, yid):
        """
        Метод для сохранения истории обработанных тем. 
        """
        while True:
            try:
                with open(HISTORY_FILE, "a") as file:
                    with portalocker.Lock(file, portalocker.LOCK_EX):
                        file.write(str(yid) + '\n')
                break
            except FileNotFoundError:
                print("Не обнаружен файл theme_history.txt")
                return False 
            except Exception as e:
                print(f"Ошибка при записи в файл: {str(e)}")
                time.sleep(1)


class RequestManager():
    """
    Менеджер обработки запросов.
    """
    def request_gpt(self, content):
        """
        Запрос генерации сценария к GPT
        """
        try:
            response = g4f.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                provider = g4f.Provider.Aichat,
                messages = [{"role": "user", "content": content}],
                auth = True,
            )
            return response
        
        except Exception as e:
            print(f"Возникла ошибка при обращении к GPT: {e}")
            return False

    def request_youtube(self, api_key, stream_id):
        """
        Запрос новых тем к YouTube
        """
        try:
            youtube = build('youtube', 'v3', developerKey=api_key)
            response = youtube.videos().list(part='liveStreamingDetails', id=stream_id).execute()
            
            if 'items' in response and response['items']:
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
            return False 

        except Exception as e:
            print(f"Возникла ошибка при обращении к YouTube: {e}")
            return False
        

class ScriptManager():
    """
    Менеджер обработки сценария.
    """
    def __init__(self):
        self.kayle_names = ["Кайл", "Kayle", "Каил", "**Кайл**"]
        self.cartman_names = ["Картман", "Kartman", "Cartman", "**Картман**"]
        self.stan_names = ["Стен", "Sten", "Стэн", "**Стен**", "**Стэн**"]
        self.kenny_names = ["Кени", "Кенни", "Кенний", "Kenny", "**Кенни**", "**Кени**"]
        self.characters_names = self.kayle_names + self.cartman_names + self.stan_names + self.kenny_names
        self.alphabet = " \nабвгдеёжзийклмнопрстуфхцшщьъэюя,!"
        
    def script_split(self, content):
        """
        Метод для форматирования сценария для создания аудио-файлов.
        Возвращает словарь проименованных реплик.
        0 - Кайл
        1 - Картман
        2 - Стен
        3 - Кенни
        """
        dialogue = {}
        i = 0

        for line in content.split('\n'):
            parts = line.split(':', 1)
            if len(parts) >= 2:
                role, reply = map(str.strip, parts)
                cur_reply = ''.join(filter(lambda y: y.lower() in self.alphabet, reply))

                role_names = [self.kayle_names, self.cartman_names, self.stan_names, self.kenny_names]
                for idx, names in enumerate(role_names):
                    if role in names:
                        dialogue[f"{i}_{idx}"] = cur_reply
                        break

                i += 1

        return dialogue

    def script_split_unity(self, content):
        """
        Метод форматирования сценария для Unity.
        Возвращает строку реплик, разделенных символом $.
        """
        result = "$".join(line.split(':', 1)[1].strip() for line in content.strip().split('\n') if line.split(':')[0].strip() in self.characters_names)
        return result
