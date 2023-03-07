import os,  praw
from flask import Flask, render_template

my_secret = os.environ['SECRET']


reddit = praw.Reddit(
      client_id = "au6T0xDrwCVnFR1i-16pIA",
      client_secret = my_secret,
      user_agent = "my user agent",
      username = "",
      password = "",
  )
print(reddit.read_only)

def factMaker(reddit):
  redditFactRaw = (reddit.subreddit("todayilearned").random())
  factData = [redditFactRaw.title, redditFactRaw.url]
  return factData



app = Flask(__name__)
@app.route('/')
def index():
  postGenerator = factMaker(reddit)
  return render_template('index.html',factTitle = postGenerator[0],factLink = postGenerator[1])

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80)
  