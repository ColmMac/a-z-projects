import praw
import urllib.request
from instagrapi import Client
import time
import random
import os
sleep = random.choice(range(80, 250))
username = input("Enter Instagram username here.:")
password = input("Enter Instagram password here.:")
client = Client()
caption = "'Glacier National Park, MT [OC] [6624x4416]' -u/Zach_Gibbons\nTags- #nature #photography #naturephotography #love #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
#FILL IN BELOW WITH YOUR OWN REDDIT BOT INFO
reddit = praw.Reddit(client_id="CLIENT ID HERE",
                     client_secret="CLIENT SECRET HERE",
                     user_agent="USER AGENT HERE")
sub = input("Which subreddit would you like to take posts from:")
subreddit = reddit.subreddit(sub)
titles = []
urls = []
users = []
for submission in subreddit.hot(limit=30):
    titles.append(submission.title)
    urls.append(submission.url)
    users.append(submission.author)
#THIS IS A FILE ONLY I WILL HAVE, MAKE YOUR OWN
urllib.request.urlretrieve(urls[0], "D:/instamemes/insta1.jpg")
urllib.request.urlretrieve(urls[1], "D:/instamemes/insta2.jpg")
urllib.request.urlretrieve(urls[2], "D:/instamemes/insta3.jpg")
urllib.request.urlretrieve(urls[3], "D:/instamemes/insta4.jpg")
urllib.request.urlretrieve(urls[4], "D:/instamemes/insta5.jpg")
urllib.request.urlretrieve(urls[5], "D:/instamemes/insta6.jpg")
urllib.request.urlretrieve(urls[6], "D:/instamemes/insta7.jpg")
urllib.request.urlretrieve(urls[7], "D:/instamemes/insta8.jpg")
urllib.request.urlretrieve(urls[8], "D:/instamemes/insta9.jpg")
urllib.request.urlretrieve(urls[9], "D:/instamemes/insta10.jpg")
urllib.request.urlretrieve(urls[10], "D:/instamemes/insta11.jpg")
urllib.request.urlretrieve(urls[11], "D:/instamemes/insta12.jpg")
urllib.request.urlretrieve(urls[12], "D:/instamemes/insta13.jpg")
urllib.request.urlretrieve(urls[13], "D:/instamemes/insta14.jpg")
urllib.request.urlretrieve(urls[14], "D:/instamemes/insta15.jpg")
urllib.request.urlretrieve(urls[15], "D:/instamemes/insta16.jpg")
urllib.request.urlretrieve(urls[16], "D:/instamemes/insta17.jpg")
urllib.request.urlretrieve(urls[17], "D:/instamemes/insta18.jpg")
urllib.request.urlretrieve(urls[18], "D:/instamemes/insta19.jpg")
urllib.request.urlretrieve(urls[19], "D:/instamemes/insta20.jpg")
urllib.request.urlretrieve(urls[20], "D:/instamemes/insta21.jpg")
urllib.request.urlretrieve(urls[21], "D:/instamemes/insta22.jpg")
urllib.request.urlretrieve(urls[22], "D:/instamemes/insta23.jpg")
urllib.request.urlretrieve(urls[23], "D:/instamemes/insta24.jpg")
urllib.request.urlretrieve(urls[24], "D:/instamemes/insta25.jpg")
urllib.request.urlretrieve(urls[25], "D:/instamemes/insta26.jpg")
urllib.request.urlretrieve(urls[26], "D:/instamemes/insta27.jpg")
urllib.request.urlretrieve(urls[27], "D:/instamemes/insta28.jpg")
urllib.request.urlretrieve(urls[28], "D:/instamemes/insta29.jpg")
urllib.request.urlretrieve(urls[29], "D:/instamemes/insta30.jpg")





caption1 = f"'{titles[0]}' -u/{users[0]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily"
caption2 = f"'{titles[1]}' -u/{users[1]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption3 = f"'{titles[2]}' -u/{users[2]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption4 = f"'{titles[3]}' -u/{users[3]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption5 = f"'{titles[4]}' -u/{users[4]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption6 = f"'{titles[5]}' -u/{users[5]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption7 = f"'{titles[6]}' -u/{users[6]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily"
caption8 = f"'{titles[7]}' -u/{users[7]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption9 = f"'{titles[8]}' -u/{users[8]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption10 = f"'{titles[9]}' -u/{users[9]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption11 = f"'{titles[10]}' -u/{users[10]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption12 = f"'{titles[11]}' -u/{users[11]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption13 = f"'{titles[12]}' -u/{users[12]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily"
caption14 = f"'{titles[13]}' -u/{users[13]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption15 = f"'{titles[14]}' -u/{users[14]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption16 = f"'{titles[15]}' -u/{users[15]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption17 = f"'{titles[16]}' -u/{users[16]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption18 = f"'{titles[17]}' -u/{users[17]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption19 = f"'{titles[18]}' -u/{users[18]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily"
caption20 = f"'{titles[19]}' -u/{users[19]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption21 = f"'{titles[20]}' -u/{users[20]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption22 = f"'{titles[21]}' -u/{users[21]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption23 = f"'{titles[22]}' -u/{users[22]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption24 = f"'{titles[23]}' -u/{users[23]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption25 = f"'{titles[24]}' -u/{users[24]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily"
caption26 = f"'{titles[25]}' -u/{users[25]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption27 = f"'{titles[26]}' -u/{users[26]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption28 = f"'{titles[27]}' -u/{users[27]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption29 = f"'{titles[28]}' -u/{users[28]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
caption30 = f"'{titles[29]}' -u/{users[29]} \nTags- #nature #photography #naturephotography #travel #photooftheday #instagood #beautiful #picoftheday #photo #instagram #naturelovers #art #landscape #travelphotography #bhfyp #happy #sunset #ig #wildlife #summer #life #sky #beauty #mountains #flowers #photographer #instadaily "
client.login(username, password)
time.sleep(26)
client.photo_upload(path="D:/instamemes/insta1.jpg", caption=caption1)
print("Photo 1 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta2.jpg", caption=caption2)
print("Photo 2 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta3.jpg", caption=caption3)
print("Photo 3 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta4.jpg", caption=caption4)
print("Photo 4 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta5.jpg", caption=caption5)
print("Photo 5 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta6.jpg", caption=caption6)
print("Photo 6 posted")
client.photo_upload(path="D:/instamemes/insta7.jpg", caption=caption7)
print("Photo 7 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta8.jpg", caption=caption8)
print("Photo 8 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta9.jpg", caption=caption9)
print("Photo 9 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta10.jpg", caption=caption10)
print("Photo 10 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta11.jpg", caption=caption11)
print("Photo 11 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta12.jpg", caption=caption12)
print("Photo 12 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta13.jpg", caption=caption13)
print("Photo 13 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta14.jpg", caption=caption14)
print("Photo 14 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta15.jpg", caption=caption15)
print("Photo 15 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta16.jpg", caption=caption16)
print("Photo 16 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta17.jpg", caption=caption17)
print("Photo 17 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta18.jpg", caption=caption18)
print("Photo 18 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta19.jpg", caption=caption19)
print("Photo 19 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta20.jpg", caption=caption20)
print("Photo 20 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta21.jpg", caption=caption21)
print("Photo 21 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta22.jpg", caption=caption22)
print("Photo 22 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta23.jpg", caption=caption23)
print("Photo 23 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta24.jpg", caption=caption24)
print("Photo 24 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta25.jpg", caption=caption25)
print("Photo 25 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta26.jpg", caption=caption26)
print("Photo 26 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta27.jpg", caption=caption27)
print("Photo 27 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta28.jpg", caption=caption28)
print("Photo 28 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta29.jpg", caption=caption29)
print("Photo 29 posted")
time.sleep(sleep)
client.photo_upload(path="D:/instamemes/insta30.jpg", caption=caption30)
print("Photo 30 posted")

os.remove("D:/instamemes/insta1.jpg")
os.remove("D:/instamemes/insta2.jpg")
os.remove("D:/instamemes/insta3.jpg")
os.remove("D:/instamemes/insta4.jpg")
os.remove("D:/instamemes/insta5.jpg")
os.remove("D:/instamemes/insta6.jpg")
os.remove("D:/instamemes/insta7.jpg")
os.remove("D:/instamemes/insta8.jpg")
os.remove("D:/instamemes/insta9.jpg")
os.remove("D:/instamemes/insta10.jpg")
os.remove("D:/instamemes/insta11.jpg")
os.remove("D:/instamemes/insta12.jpg")
os.remove("D:/instamemes/insta13.jpg")
os.remove("D:/instamemes/insta14.jpg")
os.remove("D:/instamemes/insta15.jpg")
os.remove("D:/instamemes/insta16.jpg")
os.remove("D:/instamemes/insta17.jpg")
os.remove("D:/instamemes/insta18.jpg")
os.remove("D:/instamemes/insta19.jpg")
os.remove("D:/instamemes/insta20.jpg")
os.remove("D:/instamemes/insta21.jpg")
os.remove("D:/instamemes/insta22.jpg")
os.remove("D:/instamemes/insta23.jpg")
os.remove("D:/instamemes/insta24.jpg")
os.remove("D:/instamemes/insta25.jpg")
os.remove("D:/instamemes/insta26.jpg")
os.remove("D:/instamemes/insta27.jpg")
os.remove("D:/instamemes/insta28.jpg")
os.remove("D:/instamemes/insta29.jpg")
os.remove("D:/instamemes/insta30.jpg")
print("All deleted")

