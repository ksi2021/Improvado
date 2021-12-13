import datetime
from vk_ import Vkontakte
from storage import Storage

login = input("Введите логин: \t")

password = input('Введите пароль: ')

friends = list()

vk_user = Vkontakte(login, password)

types = ['json', 'csv', 'tsv']

vk_user.get_all_friends()

for i in vk_user.get_user_info():
    temp = {'first_name': i.get('first_name'), "last_name": i.get('last_name'),
            'country': i.get('country'), 'city': i.get('city'), 'sex': i.get('sex'),
            'bdate': i.get('bdate')
            }
    friends.append(temp)

print("=" * 72)
print(f"Привет {vk_user.User['first_name']}")
print("=" * 72)
print(f"Ваш id: {vk_user.User['id']}")
print("=" * 72)
print(f"Access token: {vk_user.access_token}")
print("=" * 72)


def sort_by_alphabet(element):
    return element['first_name'][0]


for i in range(len(friends)):
    if friends[i]['bdate']:
        date = friends[i]['bdate'].split('.')
        if(len(date) > 2):
            date_ = datetime.date(int(date[2]), int(date[1]), int(date[0]))
            iso_date = date_.isoformat()
            friends[i]['bdate'] = iso_date

friends.sort(key=sort_by_alphabet)

file_type = input(f"select one type of {types} \t")
print("=" * 72)
file_name = input("Введите путь к файлу или название файла для создания в этой директории \t")
print("=" * 72)

st = Storage(name=file_name, data=friends, _type=file_type)

st.store_friends()
# st.store_friends(data=friends)
# input('Exit [Enter]')
