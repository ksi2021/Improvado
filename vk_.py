import os
import json
from time import sleep

import vk_api
from vk_api import AuthError


class Vkontakte:

    def __init__(self, login, password):
        self.access_token = ''
        self.friends = ''
        self.login = login
        self.password = password
        vk = vk_api.VkApi(login, password)

        try:
            vk.auth()
        except AuthError:
            print('Ошибка авторизации ( incorrect data )')
            print('Перезапуск через 2 секунды')
            sleep(2)
            print("\n")
            os.system("python main.py")
            exit()

        self.vk = vk.get_api()
        self.User = self.vk.users.get()[0]
        self.get_access_token()

    def get_access_token(self):
        with open('vk_config.v2.json', 'r') as data_file:
            data = json.load(data_file)

        for i in data[self.login]['token'].keys():
            for j in data[self.login]['token'][i].keys():
                self.access_token = data[self.login]['token'][i][j]['access_token']

        os.remove('vk_config.v2.json')

    def get_all_friends(self):
        self.friends = self.vk.friends.get()

    def get_user_info(self):
        return self.vk.users.get(user_ids=self.friends.get('items'), fields=['country', 'city', 'bdate', 'sex'])
