import os
import  requests

sitename =["http://api.open-notify.org/astros.json"]
t  = os.environ ['t']
total = 0 #initialization#
for k in range(len(sitename)):
    if total < t:
    g = requests.get(sitename[k])
    total = g.elasped
    print('sitename:' ,sitename[k])
    print("time: ", g.elasped)
    print('hits:', t)