# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import re
import json

from define import NAME_HOTEL_PATH, TINH_THANH_PATH, FISRT_NUMBER_PHONE, IMG_PATH, ADDRESS_HOTEL, DICT_HOTEL, SERVICE, \
    DICT_ROOM, TYPE, DESCRIBE, AVAILABLE, DICT, DICT_ADDRESS


def get_name_hotel():
    with open(NAME_HOTEL_PATH, 'r+', encoding='utf-8') as f:
        list_name_hotel = [idx.replace('\n', '') for idx in f.readlines()]
        f.close()
    return list_name_hotel


def get_name_province():
    with open(TINH_THANH_PATH, 'r', encoding='utf-8') as f:
        list_province = [idx.replace('\n', '') for idx in f.readlines()]
        f.close()

    return list_province


def get_api_img():
    img_path = None
    pattern = re.compile(r'"largeImageURL":"([^"]+)"')
    with open(IMG_PATH, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            img_path = pattern.findall(line)
    f.close()
    return img_path


def random_number_phone():
    phone_numbers = []
    for num in range(100):
        random_number = FISRT_NUMBER_PHONE + ''.join([str(random.randint(0, 9)) for num in range(9)])
        phone_numbers.append(random_number)
    return phone_numbers


def get_address_hotel():
    list_address_arr = []
    list_address_dict = []
    list_name_hotel = get_name_hotel()
    with open(ADDRESS_HOTEL, 'r', encoding='utf-8') as f:
        list_address = [idx.replace('\n', '') for idx in f.readlines()]
    for idx, value in enumerate(list_address):
        address_arr = re.split(r',\s*', value)
        list_address_dict.extend(creat_dict_address(idx, list_name_hotel, address_arr))
    return list_address, list_address_dict


def creat_dict_hotel():
    list_name_hotel = get_name_hotel()
    list_address, list_address_dict = get_address_hotel()
    list_phone_number = random_number_phone()
    list_dict_hotel = []
    list_dict_room = []
    for i in range(100):
        new_dict_hotel = DICT_HOTEL.copy()
        new_dict_hotel['id'] = str(i + 1)
        new_dict_hotel['name'] = list_name_hotel[i]
        new_dict_hotel['address'] = list_address_dict[i]
        new_dict_hotel['phone'] = list_phone_number[i]
        new_dict_hotel['stars'] = random.randint(1, 5)
        new_dict_hotel['services'] = SERVICE
        list_dict_hotel.append(new_dict_hotel)
        list_dict_room.extend(creat_dict_room(i))
    return list_dict_hotel, list_dict_room


def creat_dict_room(idx_hotel):
    list_img_path = get_api_img()
    list_dict_room = []
    for i in range(10):
        new_dict_room = DICT_ROOM.copy()
        new_dict_room['id'] = str(i + 1)
        new_dict_room['hotel_id'] = str(idx_hotel + 1)
        new_dict_room['type'] = random.choice(TYPE)

        if new_dict_room['type'] == TYPE[0]:
            new_dict_room['adult'] = str(2)
            new_dict_room['children'] = str(0)
            new_dict_room['price'] = random.randint(300000, 1000000)
        else:
            new_dict_room['adult'] = str(2)
            new_dict_room['children'] = str(random.randint(1, 3))
            new_dict_room['price'] = random.randint(700000, 1500000)

        new_dict_room['description'] = DESCRIBE
        new_dict_room['availability'] = random.choice(AVAILABLE)
        new_dict_room['img'] = random.sample(list_img_path, 3)

        for idx in new_dict_room['img']:
            list_img_path.remove(idx)
        list_dict_room.append(new_dict_room)
    return list_dict_room


def creat_dict_address(idx, list_name_hotel, address_arr):
    list_address_arr = []

    new_dict_address = DICT_ADDRESS.copy()
    new_dict_address['name_address'] = list_name_hotel[idx]
    new_dict_address['street'] = address_arr[0]
    new_dict_address['ward'] = address_arr[1]
    new_dict_address['district'] = address_arr[2]
    new_dict_address['provice'] = address_arr[3]
    new_dict_address['country'] = address_arr[4]
    list_address_arr.append(new_dict_address)
    return list_address_arr

def create_dtb():
    list_dict_hotel, list_dict_room = creat_dict_hotel()
    list_dict_dtb = []
    dict_dtb = DICT.copy()
    dict_dtb['hotels'] = list_dict_hotel
    dict_dtb['rooms'] = list_dict_room
    list_dict_dtb.append(dict_dtb)
    return list_dict_dtb


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_dict_dtb = create_dtb()
    with open('D:\\ThanhMinh\\hotel_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(list_dict_dtb, json_file, indent=4, ensure_ascii=False)
