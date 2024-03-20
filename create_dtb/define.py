DICT_ADDRESS = {
    'name_address': '',
    'street': '',
    'ward': '',
    'district': '',
    'provice': '',
    'country': ''
}

DICT_HOTEL = {
    'id': '',
    'name': '',
    'address': DICT_ADDRESS,
    'phone': '',
    'stars': '',
    'services': []
}

DICT_ROOM = {
    'id': '',
    'hotel_id': '',
    'type': '',
    'description': '',
    'price': '',   #VND
    'adult': '',
    'children': '',
    'availability': '',
    'img': [],
}

DICT = {
    'hotels': DICT_HOTEL,
    'rooms': DICT_ROOM
}


NAME_HOTEL_PATH = 'D:\RIKAI\DATN\project\create_dtb/name_hotel.txt'
TINH_THANH_PATH = 'D:\RIKAI\DATN\project\create_dtb\province.txt'
IMG_PATH = 'D:\RIKAI\DATN\project\create_dtb\img.txt'
ADDRESS_HOTEL = 'D:\RIKAI\DATN\project\create_dtb/address.txt'
SERVICE = ["Beachfront", "Swimming Pool", "Spa", "Restaurant"]
TYPE = ['Single Room', 'Double Room']
DESCRIBE = 'This luxurious beachfront resort offers stunning views of the ocean and tropical gardens. With modern design and top-notch amenities, it provides a serene retreat. Featuring spacious rooms, multiple dining options, a spa, and recreational activities, it caters to both leisure and business travelers.'
AVAILABLE = ['True', 'False']


FISRT_NUMBER_PHONE = '+84'