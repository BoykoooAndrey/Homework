import json


def parse_city_json(original_city_database):
    cities_py = None
    try:
        with open(f'{original_city_database}', 'r', encoding='utf-8') as f:
            cities_js = f
            cities_py = json.load(cities_js)
    except Exception as err:
        print(err)
        return None
    return [city['city'].lower() for city in cities_py]


def take_last_simbol(city_name):
    if (city_name[-1] not in ['ь', 'ъ', 'ы']):
        return city_name[-1]
    else:
        return city_name[-2]


def write_name_in_file(city_name, file_with_used_names):
    with open(f'{file_with_used_names}', 'a', encoding='utf-8') as f:
        f.writelines(f' {city_name}')


def get_city(user_city, file_with_used_names):
    formated_city_database = parse_city_json('russia')
    formatted_city_name = user_city.strip().lower()[1:]

    if (formatted_city_name in formated_city_database):
        names_cities_used = 0
        with open(file_with_used_names, 'r', encoding='utf-8') as f:
            names_cities_used = f.read().split(' ')
        if (len(names_cities_used) > 1) and not ((names_cities_used[-1])[-1] == formatted_city_name[0]):
            return 'Может стоит назвать город который начинается с последней буквы названного мною города, рак?'
        if formatted_city_name in names_cities_used:
            return 'Город уже пикнули, репикай!'

        last_simbol = take_last_simbol(formatted_city_name)
        for i in formated_city_database:
            if (i[0] == last_simbol) and (i not in names_cities_used):
                write_name_in_file(formatted_city_name,
                                   file_with_used_names)
                write_name_in_file(i, file_with_used_names)
                return i.capitalize()
        return 'Я не знаю, ты выиграл'
    else:
        return 'Я мб и из США, но уверен что в Рашке такого города нет!'


