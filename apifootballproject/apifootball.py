import requests
import json
import html
import re

from models.main_model import Command, History, Game, League


result = []
def html_to_txt(html_text):
    ## unescape html
    txt = html.unescape(html_text)
    tags = re.findall("<[^>]+>",txt)
    # print("found tags: ")
    # print(tags)
    for tag in tags:
        txt=txt.replace(tag,'')
    return txt

def get_data(text):
    main_json = ''
    new_json = re.findall(r'{.*}',text)
    j = 0
    for i in new_json:
        if j == len(new_json) - 1:
            main_json += f'{i}'
        else:
            main_json += f'{i},'
        j += 1

    new_data = main_json.replace('@', '')
    json_data = '{"data":' + '[' + new_data + ']' + '}'
    return json_data



# response = requests.get('https://soccer365.ru/competitions/18/')
# croud_block = response.text
# block = ''.join(croud_block)
# print(block.replace(' ', ''))
#
# with open('bundes_ligue.txt', 'w') as file:
#     file.write(response.text)

with open('bundes_ligue.txt', 'r') as f:
    crude_block = f.read()
    # print(crude_block[28900:32000])
    # print(crude_block[39000:41350])
    crude_json = html_to_txt(crude_block[28900:47350])

# print(get_data(crude_json))

# Запись json'a
with open(f'next_tour_json.json', 'w', encoding='utf8') as f:
    f.write(get_data(crude_json))

with open('next_tour_json.json', 'r') as f:
    json_schedule = json.load(f)

print(json_schedule['data'][0]['performer'][0]['name'])

NEAREST_SCHEDULE = League(
    league_id=1,
    game=Game(
        game=json_schedule['data'][0]['name'],
        date=json_schedule['data'][0]['startDate']
    )
)

LAST_RESULT = League(
    league_id=1,
    commands=Command(
        host='',
        guest='',
        history=History(
            score=-1,
            un_score=-1
        )
    ),
    game=Game(
        date=''
    ),


)
result.append(NEAREST_SCHEDULE)
print (LAST_RESULT)