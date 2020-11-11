import urllib.request,urllib.parse, urllib.error
import json,ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


serviceurl = "https://aoe2.net/api/player/lastmatch?"
# You can try with mi personal Steam ID 76561198290273458
# 76561199036184522 another one
player_id = input('ID: ')
game_wanted = 'aoe2de'

#Constructing the URL
parameters = {"game": game_wanted, "steam_id": player_id}
paramsurl = urllib.parse.urlencode(parameters)
the_url = serviceurl.strip() + paramsurl.strip()
#print(the_url) to check if its working

#Handle data
data_read = urllib.request.urlopen(the_url).read()
data = data_read.decode()
jsondata = json.loads(data)
#print(data) to check if its working
#print(json.dumps(jsondata, indent=4)) to see the file

#Some details of the player and the game
print('Player:',jsondata['name'])
print('Country:',jsondata['country'])
try:
    print('Clan:',jsondata['clan'])
except:
    print('---Failure to retrieve clan---')

print('Number of players:',jsondata['last_match']['num_players'])

if jsondata['last_match']['ranked'] is True:
    print('Ranked game')
else:
    print('Unranked game')

count= 1

for player in jsondata['last_match']['players']:
    print('Player', count ,player['name'])
    count=count + 1

