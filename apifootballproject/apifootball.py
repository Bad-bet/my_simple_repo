import requests
#

response = requests.get('https://apiv3.apifootball.com/?action=get_statistics&match_id=86392&APIkey=8c784854f431e4a65dac136c706ddd2c59e505274a223b4a5b0401ddb95b8066')

print(response.json())