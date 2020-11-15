import urllib.request,urllib.parse, urllib.error
import json,ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl= 'https://aoe2.net/api/leaderboard?'
turn_on=input('Do you want to print top ten? (Y/N): ')
game_wanted='aoe2de'
leaderboard_ID='3' 
#This one to retrieve Ranked Random Map leaderboard#
count='10'
#Retrieve top ten
start='1'

if turn_on=='Y' or turn_on=='y':
    #Constructing the URL
    parameters = {"game": game_wanted, "leaderboard_ID": leaderboard_ID,"start":start,"count":count}
    paramsurl = urllib.parse.urlencode(parameters)
    the_url = serviceurl.strip() + paramsurl.strip()
    #print(the_url) to check if its working
    #Handle data
    data_read = urllib.request.urlopen(the_url).read()
    data = data_read.decode()
    jsondata = json.loads(data)
    #print(data) to check if its working
    #print(json.dumps(jsondata, indent=4)) to see the file

    for player in jsondata['leaderboard']:
        print('Rank: ', player['rank'])
        print('player name: ', player['name'])
        print('Rating: ', player['rating'])
        print()
else:
    print('----Program closed----')
