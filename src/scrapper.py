import praw
import simplejson
from time import strftime,localtime
import re

def sekilyaz(yazi):
    print(strftime("%H:%M:%S",localtime())+' %s' % yazi)

class login:
    client_id = "aJzlBFiy8gBKcZChhCvuaw"
    client_secret = 'E2hUwBJVt6Br0IQ6RbN1NW37W3oxPA'
    username = 'yigidor'
    password = 'btc123456'
    user_agent = 'BTC info (by /u/<yigidor>)'
r = praw.Reddit(client_id=login.client_id,
client_secret=login.client_secret,
user_agent=login.user_agent,
)
class tarama:
    kelime = 'bitcoin'
    sub = 'Bitcoin' + 'btc' + 'CryptoCurrency' + ' BitcoinBeginners'
    sort = 'top'
    limit = '50'


yorumlar = []
subredditler = ['Bitcoin' , 'btc' , 'CryptoCurrency' , 'BitcoinBeginners']
try:
    for subreddit in subredditler:
        sekilyaz('Subreddit değişiyor: %s' % subreddit)
        sub = r.subreddit(subreddit)
        for submission in sub.top(time_filter="day",limit = 10):
            sekilyaz('Post değişiyor: %s' % submission.title)
            post = r.submission(submission.id)
            if post.stickied:
                sekilyaz("Post pinlendiği için geçiliyor")
                continue
            else:
                post.comments.replace_more(limit=None)
                for yorum in post.comments.list():
                    if re.search("btc",yorum.body,re.IGNORECASE):
                        yorumlar.append(yorum.body)
                    elif re.search("bitcoin",yorum.body,re.IGNORECASE):
                        yorumlar.append(yorum.body)
                    else:
                        continue
                sekilyaz('Yorumlar eklendi')
except KeyboardInterrupt:
    sekilyaz('Kullanıcı çıkışı yapıldı.')
    sekilyaz('Yorumlar kaydediliyor.')
    dosya = open('yorumlar.txt','w')
    simplejson.dump(yorumlar,dosya)
    dosya.close()

dosya = open('yorumlar.txt','w')
simplejson.dump(yorumlar,dosya)
dosya.close()