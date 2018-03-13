import os
import tweepy
import time

consumer_key ="U8tnRTs1PphsVbWjwrXz6yfwK"
consumer_secret ="NwwzXfFwnQkzMz86JxS4sFh4pGfK8Bfn1zqt8tjaYEcEo64Fvb"
access_token ="2989649799-FkC2d1YaqXkmb8ikKcYFYvu1lhFVGN0wiVCD9vc"
access_token_secret ="vM63wZomeC3zdoraJkePGoS7jHCSCxnhqDHjM7crmsvvU"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

a=1
while a<=2:
    
    cmd="fswebcam -F 3 --fps 20 -r 1200*700 /home/cs2017a109/Desktop/img.jpg"
    os.system(cmd)
    img="/home/cs2017a109/Desktop/img.jpg"
    print("pic taken")
    api.update_with_media(img, status="nice one")
    print("wait for five seconds")
    time.sleep(5)
    a+=1
    
    print("succees")
 
