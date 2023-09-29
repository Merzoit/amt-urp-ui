import os
import requests
import g4f
import json
from gtts import gTTS
from gradio_client import Client


from settings import DA_TOKEN, HISTORY_FILE

class Yengine():
    """
    Вспомогательный класс с методами движка программы. 
    """
    def __init__(self):
        self.kayle_names = ["Кайл", "Kayle", "Каил", "**Кайл**"]
        self.cartman_names = ["Картман", "Kartman", "Cartman", "**Картман**"]
        self.stan_names = ["Стен", "Sten", "Стэн", "**Стен**", "**Стэн**"]
        self.kenny_names = ["Кени", "Кенни", "Кенний", "Kenny", "**Кенни**", "**Кени**"]
        self.characters_names = self.kayle_names + self.cartman_names + self.stan_names + self.kenny_names
        self.alphabet = " \nабвгдеёжзийклмнопрстуфхцшщьъэюя,!"
    
    def load_donation_history(self):
        """
        Метод для загрузки ранее обработанных донатов.
        Возвращает список с id всех сохранённых донатов.
        """
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                return set(file.read().splitlines())
        else:
            return set()

    def save_donation_history(self, yid):
        """
        Метод для сохранения истории обработанных донатов. 
        """
        with open(HISTORY_FILE, "a") as file:
            file.write(str(yid) + '\n')

    def request_for_donate_pay(self):
        """
        Метод запроса к сервису Donate Pay, для получения информации по
        ранее не обработанным донатам. Возвращает словарь с данными одного нового доната.
        """
        history = self.load_donation_history()
        url = f'https://donatepay.ru/api/v1/transactions?access_token={DA_TOKEN}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for transaction in data["data"]:
                transaction_id = transaction.get("id", "")

                if str(transaction_id) not in history:
                    transaction_data = {
                        "id": transaction.get("id", ""),
                        "comment": transaction.get("comment", ""),
                        "user": transaction.get("what", ""),
                        "sum": transaction.get("sum", 0)
                    }
                    #save_history()?
                    return transaction_data
                else:
                    continue
        else:
            return False

    def request_for_gpt(self, promt):
        """
        Метод отправки запроса к gpt.
        Возвращает строку сценария.
        """
        response = g4f.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            provider = g4f.Provider.Aichat,
            messages = [{"role": "user", "content": promt}],
            auth = True,
            #stream = True,
        )

        script = ""
        for words in response:
            script += words
        return script

    def script_split(self, content):
        """
        Метод для форматирования сценария для создания аудио-файлов.
        Возвращает словарь проименованных реплик.
        0 - Кайл
        1 - Картман
        2 - Стен
        3 - Кенни
        """
        lines = content.strip().split('\n')
        dialogue = {}
        i = 0
        for line in lines:
            parts = line.split(':')
            if len(parts) >= 2:
                role = parts[0].strip()
                reply = ':'.join(parts[1:]).strip()
                cur_reply = ""
                for y in reply:
                    if y.lower() in self.alphabet:
                        cur_reply += y

                if role in self.kayle_names:
                    dialogue[f"{i}_0"] = cur_reply
                elif role in self.cartman_names:
                    dialogue[f"{i}_1"] = cur_reply
                elif role in self.stan_names:
                    dialogue[f"{i}_2"] = cur_reply
                elif role in self.kenny_names:
                    dialogue[f"{i}_3"] = cur_reply
                i += 1
        return dialogue

    def script_split_unity(self, content):
        """
        Метод форматирования сценария для Unity.
        Возвращает строку реплик, разъеденённых символом $.
        """
        lines = content.strip().split('\n')
        result = ""
        for line in lines:
            parts = line.split(':')
            if len(parts) >= 2:
                role = parts[0].strip()
                if role in self.characters_names:
                    result += f"{line}$"
        return result

    def script_import(self, content, path):
        """
        Метод для импорта сценария.
        """
        file_path = os.path.join(path, 'dialog.txt')
        with open(file_path, 'w', encoding='utf-8-sig') as file:
            file.write(content)

    def audio_changed(self, text, model, dire, name):
        """
        Изменение голоса.
        """
        print("asdasd")
        client = Client("http://127.0.0.1:7860/")
        result = client.predict(
                        f"{model}",	# str (Option from: ['cartman', 'test']) in 'Model' Dropdown component
                        0,	# int | float (numeric value between -100 and 100) in 'Speech speed (%)' Slider component
                        f"{text}",	# str in 'Input Text' Textbox component
                        "ru-RU-SvetlanaNeural-Female",	# str (Option from: ['af-ZA-AdriNeural-Female', 'af-ZA-WillemNeural-Male', 'sq-AL-AnilaNeural-Female', 'sq-AL-IlirNeural-Male', 'am-ET-AmehaNeural-Male', 'am-ET-MekdesNeural-Female', 'ar-DZ-AminaNeural-Female', 'ar-DZ-IsmaelNeural-Male', 'ar-BH-AliNeural-Male', 'ar-BH-LailaNeural-Female', 'ar-EG-SalmaNeural-Female', 'ar-EG-ShakirNeural-Male', 'ar-IQ-BasselNeural-Male', 'ar-EG-BasselArIQNeural-Male', 'ar-IQ-RanaNeural-Female', 'ar-JO-SanaNeural-Female', 'ar-EG-TaimArJONeural-Male', 'ar-JO-TaimNeural-Male', 'ar-KW-FahedNeural-Male', 'ar-KW-NouraNeural-Female', 'ar-LB-LaylaNeural-Female', 'ar-LB-RamiNeural-Male', 'ar-LY-ImanNeural-Female', 'ar-LY-OmarNeural-Male', 'ar-EG-OmarArLYNeural-Male', 'ar-MA-JamalNeural-Male', 'ar-MA-MounaNeural-Female', 'ar-OM-AbdullahNeural-Male', 'ar-EG-AbdullahArOMNeural-Male', 'ar-OM-AyshaNeural-Female', 'ar-EG-AyshaArOMNeural-Female', 'ar-QA-AmalNeural-Female', 'ar-QA-MoazNeural-Male', 'ar-EG-MoazArQANeural-Male', 'ar-SA-HamedNeural-Male', 'ar-SA-ZariyahNeural-Female', 'ar-SY-AmanyNeural-Female', 'ar-EG-AmanyArSYNeural-Female', 'ar-EG-LaithArSYNeural-Male', 'ar-SY-LaithNeural-Male', 'ar-EG-HediArTNNeural-Male', 'ar-TN-HediNeural-Male', 'ar-TN-ReemNeural-Female', 'ar-EG-ReemArTNNeural-Female', 'ar-AE-FatimaNeural-Female', 'ar-AE-HamdanNeural-Male', 'ar-YE-MaryamNeural-Female', 'ar-EG-SalehArYENeural-Male', 'ar-YE-SalehNeural-Male', 'az-AZ-BabekNeural-Male', 'az-AZ-BanuNeural-Female', 'bn-BD-NabanitaNeural-Female', 'bn-BD-PradeepNeural-Male', 'bn-IN-BashkarNeural-Male', 'bn-IN-TanishaaNeural-Female', 'bs-BA-GoranNeural-Male', 'bs-BA-VesnaNeural-Female', 'bg-BG-BorislavNeural-Male', 'bg-BG-KalinaNeural-Female', 'my-MM-NilarNeural-Female', 'my-MM-ThihaNeural-Male', 'ca-ES-EnricNeural-Male', 'ca-ES-JoanaNeural-Female', 'zh-HK-HiuGaaiNeural-Female', 'zh-HK-HiuMaanNeural-Female', 'zh-HK-WanLungNeural-Male', 'zh-CN-XiaoxiaoNeural-Female', 'zh-CN-XiaoyiNeural-Female', 'zh-CN-YunjianNeural-Male', 'zh-CN-YunxiNeural-Male', 'zh-CN-YunxiaNeural-Male', 'zh-CN-YunyangNeural-Male', 'zh-CN-liaoning-XiaobeiNeural-Female', 'zh-CN-XiaobeiNeural-Female', 'zh-TW-HsiaoChenNeural-Female', 'zh-TW-YunJheNeural-Male', 'zh-TW-HsiaoYuNeural-Female', 'zh-CN-shaanxi-XiaoniNeural-Female', 'zh-CN-XiaoniNeural-Female', 'hr-HR-GabrijelaNeural-Female', 'hr-HR-SreckoNeural-Male', 'cs-CZ-AntoninNeural-Male', 'cs-CZ-VlastaNeural-Female', 'da-DK-ChristelNeural-Female', 'da-DK-JeppeNeural-Male', 'nl-BE-ArnaudNeural-Male', 'nl-BE-DenaNeural-Female', 'nl-NL-ColetteNeural-Female', 'nl-NL-FennaNeural-Female', 'nl-NL-MaartenNeural-Male', 'en-AU-NatashaNeural-Female', 'en-AU-WilliamNeural-Male', 'en-CA-ClaraNeural-Female', 'en-CA-LiamNeural-Male', 'en-HK-SamNeural-Male', 'en-HK-YanNeural-Female', 'en-IN-NeerjaExpressiveNeural-Female', 'en-IN-NeerjaNeural-Female', 'en-IN-PrabhatNeural-Male', 'en-IE-ConnorNeural-Male', 'en-IE-EmilyNeural-Female', 'en-KE-AsiliaNeural-Female', 'en-US-AsiliaEnKENeural-Female', 'en-US-ChilembaEnKENeural-Male', 'en-KE-ChilembaNeural-Male', 'en-NZ-MitchellNeural-Male', 'en-NZ-MollyNeural-Female', 'en-NG-AbeoNeural-Male', 'en-US-AbeoEnNGNeural-Male', 'en-US-EzinneEnNGNeural-Female', 'en-NG-EzinneNeural-Female', 'en-US-JamesEnPHNeural-Male', 'en-PH-JamesNeural-Male', 'en-US-RosaEnPHNeural-Female', 'en-PH-RosaNeural-Female', 'en-US-LunaEnSGNeural-Female', 'en-SG-LunaNeural-Female', 'en-SG-WayneNeural-Male', 'en-US-WayneEnSGNeural-Male', 'en-US-LeahEnZANeural-Female', 'en-ZA-LeahNeural-Female', 'en-US-LukeEnZANeural-Male', 'en-ZA-LukeNeural-Male', 'en-TZ-ElimuNeural-Male', 'en-US-ElimuEnTZNeural-Male', 'en-TZ-ImaniNeural-Female', 'en-US-ImaniEnTZNeural-Female', 'en-GB-LibbyNeural-Female', 'en-GB-MaisieNeural-Female', 'en-GB-RyanNeural-Male', 'en-GB-SoniaNeural-Female', 'en-GB-ThomasNeural-Male', 'en-US-AriaNeural-Female', 'en-US-AnaNeural-Female', 'en-US-ChristopherNeural-Male', 'en-US-EricNeural-Male', 'en-US-GuyNeural-Male', 'en-US-JennyNeural-Female', 'en-US-MichelleNeural-Female', 'en-US-RogerNeural-Male', 'en-US-SteffanNeural-Male', 'et-EE-AnuNeural-Female', 'et-EE-KertNeural-Male', 'fil-PH-AngeloNeural-Male', 'fil-PH-BlessicaNeural-Female', 'fi-FI-HarriNeural-Male', 'fi-FI-NooraNeural-Female', 'fr-BE-CharlineNeural-Female', 'fr-BE-GerardNeural-Male', 'fr-CA-AntoineNeural-Male', 'fr-CA-JeanNeural-Male', 'fr-CA-SylvieNeural-Female', 'fr-FR-DeniseNeural-Female', 'fr-FR-EloiseNeural-Female', 'fr-FR-HenriNeural-Male', 'fr-CH-ArianeNeural-Female', 'fr-CH-FabriceNeural-Male', 'gl-ES-RoiNeural-Male', 'gl-ES-SabelaNeural-Female', 'ka-GE-EkaNeural-Female', 'ka-GE-GiorgiNeural-Male', 'de-AT-IngridNeural-Female', 'de-AT-JonasNeural-Male', 'de-DE-AmalaNeural-Female', 'de-DE-ConradNeural-Male', 'de-DE-KatjaNeural-Female', 'de-DE-KillianNeural-Male', 'de-CH-JanNeural-Male', 'de-CH-LeniNeural-Female', 'el-GR-AthinaNeural-Female', 'el-GR-NestorasNeural-Male', 'gu-IN-DhwaniNeural-Female', 'gu-IN-NiranjanNeural-Male', 'he-IL-AvriNeural-Male', 'he-IL-HilaNeural-Female', 'hi-IN-MadhurNeural-Male', 'hi-IN-SwaraNeural-Female', 'hu-HU-NoemiNeural-Female', 'hu-HU-TamasNeural-Male', 'is-IS-GudrunNeural-Female', 'is-IS-GunnarNeural-Male', 'id-ID-ArdiNeural-Male', 'id-ID-GadisNeural-Female', 'ga-IE-ColmNeural-Male', 'ga-IE-OrlaNeural-Female', 'it-IT-DiegoNeural-Male', 'it-IT-ElsaNeural-Female', 'it-IT-IsabellaNeural-Female', 'ja-JP-KeitaNeural-Male', 'ja-JP-NanamiNeural-Female', 'jv-ID-DimasNeural-Male', 'jv-ID-SitiNeural-Female', 'kn-IN-GaganNeural-Male', 'kn-IN-SapnaNeural-Female', 'kk-KZ-AigulNeural-Female', 'kk-KZ-DauletNeural-Male', 'km-KH-PisethNeural-Male', 'km-KH-SreymomNeural-Female', 'ko-KR-InJoonNeural-Male', 'ko-KR-SunHiNeural-Female', 'lo-LA-ChanthavongNeural-Male', 'lo-LA-KeomanyNeural-Female', 'lv-LV-EveritaNeural-Female', 'lv-LV-NilsNeural-Male', 'lt-LT-LeonasNeural-Male', 'lt-LT-OnaNeural-Female', 'mk-MK-AleksandarNeural-Male', 'mk-MK-MarijaNeural-Female', 'ms-MY-OsmanNeural-Male', 'ms-MY-YasminNeural-Female', 'ml-IN-MidhunNeural-Male', 'ml-IN-SobhanaNeural-Female', 'mt-MT-GraceNeural-Female', 'mt-MT-JosephNeural-Male', 'mr-IN-AarohiNeural-Female', 'mr-IN-ManoharNeural-Male', 'mn-MN-BataaNeural-Male', 'mn-MN-YesuiNeural-Female', 'ne-NP-HemkalaNeural-Female', 'ne-NP-SagarNeural-Male', 'nb-NO-FinnNeural-Male', 'nb-NO-PernilleNeural-Female', 'ps-AF-GulNawazNeural-Male', 'ps-AF-LatifaNeural-Female', 'fa-IR-DilaraNeural-Female', 'fa-IR-FaridNeural-Male', 'pl-PL-MarekNeural-Male', 'pl-PL-ZofiaNeural-Female', 'pt-BR-AntonioNeural-Male', 'pt-BR-FranciscaNeural-Female', 'pt-PT-DuarteNeural-Male', 'pt-PT-RaquelNeural-Female', 'ro-RO-AlinaNeural-Female', 'ro-RO-EmilNeural-Male', 'ru-RU-DmitryNeural-Male', 'ru-RU-SvetlanaNeural-Female', 'sr-RS-NicholasNeural-Male', 'sr-RS-SophieNeural-Female', 'si-LK-SameeraNeural-Male', 'si-LK-ThiliniNeural-Female', 'sk-SK-LukasNeural-Male', 'sk-SK-ViktoriaNeural-Female', 'sl-SI-PetraNeural-Female', 'sl-SI-RokNeural-Male', 'so-SO-MuuseNeural-Male', 'so-SO-UbaxNeural-Female', 'es-AR-ElenaNeural-Female', 'es-ES-ElenaEsARNeural-Female', 'es-AR-TomasNeural-Male', 'es-ES-TomasEsARNeural-Male', 'es-BO-MarceloNeural-Male', 'es-BO-SofiaNeural-Female', 'es-CL-CatalinaNeural-Female', 'es-CL-LorenzoNeural-Male', 'es-MX-LorenzoEsCLNeural-Male', 'es-ES-GonzaloEsCONeural-Male', 'es-CO-GonzaloNeural-Male', 'es-ES-SalomeEsCONeural-Female', 'es-CO-SalomeNeural-Female', 'es-CR-JuanNeural-Male', 'es-CR-MariaNeural-Female', 'es-CU-BelkysNeural-Female', 'es-ES-ManuelEsCUNeural-Male', 'es-CU-ManuelNeural-Male', 'es-DO-EmilioNeural-Male', 'es-DO-RamonaNeural-Female', 'es-EC-AndreaNeural-Female', 'es-EC-LuisNeural-Male', 'es-SV-LorenaNeural-Female', 'es-SV-RodrigoNeural-Male', 'es-GQ-JavierNeural-Male', 'es-ES-JavierEsGQNeural-Male', 'es-GQ-TeresaNeural-Female', 'es-GT-AndresNeural-Male', 'es-GT-MartaNeural-Female', 'es-HN-CarlosNeural-Male', 'es-HN-KarlaNeural-Female', 'es-MX-DaliaNeural-Female', 'es-MX-JorgeNeural-Male', 'es-NI-FedericoNeural-Male', 'es-NI-YolandaNeural-Female', 'es-PA-MargaritaNeural-Female', 'es-PA-RobertoNeural-Male', 'es-PY-MarioNeural-Male', 'es-PY-TaniaNeural-Female', 'es-PE-AlexNeural-Male', 'es-PE-CamilaNeural-Female', 'es-PR-KarinaNeural-Female', 'es-PR-VictorNeural-Male', 'es-ES-AlvaroNeural-Male', 'es-ES-ElviraNeural-Female', 'es-US-AlonsoNeural-Male', 'es-US-PalomaNeural-Female', 'es-UY-MateoNeural-Male', 'es-UY-ValentinaNeural-Female', 'es-VE-PaolaNeural-Female', 'es-VE-SebastianNeural-Male', 'su-ID-JajangNeural-Male', 'su-ID-TutiNeural-Female', 'sw-KE-RafikiNeural-Male', 'sw-KE-ZuriNeural-Female', 'sw-TZ-DaudiNeural-Male', 'sw-TZ-RehemaNeural-Female', 'sv-SE-MattiasNeural-Male', 'sv-SE-SofieNeural-Female', 'ta-IN-PallaviNeural-Female', 'ta-IN-ValluvarNeural-Male', 'ta-MY-KaniNeural-Female', 'ta-MY-SuryaNeural-Male', 'ta-SG-AnbuNeural-Male', 'ta-SG-VenbaNeural-Female', 'ta-LK-KumarNeural-Male', 'ta-LK-SaranyaNeural-Female', 'te-IN-MohanNeural-Male', 'te-IN-ShrutiNeural-Female', 'th-TH-NiwatNeural-Male', 'th-TH-PremwadeeNeural-Female', 'tr-TR-AhmetNeural-Male', 'tr-TR-EmelNeural-Female', 'uk-UA-OstapNeural-Male', 'uk-UA-PolinaNeural-Female', 'ur-IN-GulNeural-Female', 'ur-IN-SalmanNeural-Male', 'ur-PK-AsadNeural-Male', 'ur-PK-UzmaNeural-Female', 'uz-UZ-MadinaNeural-Female', 'uz-UZ-SardorNeural-Male', 'vi-VN-HoaiMyNeural-Female', 'vi-VN-NamMinhNeural-Male', 'cy-GB-AledNeural-Male', 'cy-GB-NiaNeural-Female', 'zu-ZA-ThandoNeural-Female', 'zu-ZA-ThembaNeural-Male']) in 'Edge-tts speaker (format: language-Country-Name-Gender)' Dropdown component
                        5,	# int | float in 'Transpose (the best value depends on the models and speakers)' Number component
                        "pm",	# str in 'Pitch extraction method (pm: very fast, low quality, rmvpe: a little slow, high quality)' Radio component
                        0,	# int | float (numeric value between 0 and 1) in 'Index rate' Slider component
                        0,	# int | float (numeric value between 0 and 0.5) in 'Protect' Slider component
                        fn_index=0,
        )

        import shutil
        # Copy the generated MP3 audio to the specified output directory
        output_path_mp3 = f"{dire}/{name}.wav"
        shutil.copy(result[2], output_path_mp3)

    def audio_import(self, script, path):
        """
        Метод импортирующий аудио по сценарию в указанную папку.
        Сценарий в формате словаря.
        """
        for role, reply in script.items():
            print(role[-1])
            if role[-1] == "0":
                self.audio_changed(reply, "kayle", path, role)
            elif role[-1] == "1":
                self.audio_changed(reply, "cartman", path, role)
            elif role[-1] == "2":
                self.audio_changed(reply, "stan", path, role)
            
    def unity_status(self):
        """
        Проверка готовности Unity.
        """
        with open("path.json", "r", encoding='utf-8-sig') as file:
            mai = json.load(file)
        
        first_folder = mai["first"]["ready"]
        second_folder = mai["second"]["ready"]

        if first_folder == "true" or second_folder == "true":
            return True
        else:
            return False

    def folder_status(self, folder):
        """
        Проверка готовности папки.
        Атрибут folder принимает значения first/second.
        """
        with open("path.json", "r", encoding='utf-8-sig') as file:
            mai = json.load(file)

        status = mai[f"{folder}"]["ready"]
        if status == "true":
            return True
        else:
            return False 

    def cash_load(self):
        """
        Загрузка кэша.
        Возвращает словарь.
        """
        with open("path.json", "r", encoding='utf-8-sig') as file:
            mai = json.load(file)

        return mai

    def generated(self, folder, dir_promt, promt=""):
        """
        Метод для генерации конечного результата.
        """
        if not promt:
            promt = "сатива или индика?"

        with open("path.json", "r", encoding='utf-8-sig') as file:
            mai = json.load(file)

        print("Запрос жпт")
        content = self.request_for_gpt(f"{dir_promt}: {promt}")
        print(content)
        script = self.script_split(content)
        if script:
            print("Юнити")
            unity_content = self.script_split_unity(content)
            print("Сценарий")
            self.script_import(unity_content, mai[f"{folder}"]["script"])
            print("Аудио")
            self.audio_import(script, mai[f"{folder}"]["audio"])
            mai[f"{folder}"]["ready"] = "false"
            with open("path.json", "w", encoding='utf-8-sig') as file:
                json.dump(mai, file)
        else:
            self.generated(folder, dir_promt, promt="любая смешная тема")

if __name__ == "__main__":
    a = Yengine()
    """print(a.request_for_donate_pay())
    for i in a.load_donation_history():
        print(i)
    script = a.request_for_gpt("Напиши сценарий диалога из 15 реплик на русском языке между Кайл, Картман, Стен и Кени из южного парка, на тему сатива или индика?")
    print(script)
    print(a.script_split(script))
    print(a.script_split_unity(script))

    dir_promt = "Напиши сценарий диалога из 15 реплик на русском языке между Кайл, Картман, Стен и Кени из южного парка, на тему"
    a.generated("first", dir_promt, "импатенция Картмана")"""
    print(a.folder_status("second"))