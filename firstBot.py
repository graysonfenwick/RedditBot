# A trial reddit bot, for learning purposes
# 

from bs4 import BeautifulSoup
from urllib.parse import urlparse

import praw
import time
import re
import requests
import bs4

path = '~/Documents/Fun/RedditBot/temp.txt'
#Location of something idk




def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('nuzzyfipplestestbot', user_agent='nuzzyfipplestestbot')
    print("Authenticated as {}\n".format(reddit.user.me()))
    return reddit


def fetchdata(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tag = soup.find('p')
    data = ' '
    while True:
        if isinstance(tag, bs4.element.Tag):
            if (tag.name == 'h2'):
                break
            if (tag.name == 'h3'):
                tag = tag.nextSibling
            else:
                data = data + '\n' + tag.text
                tag = tag.nextSibling
        else:
            tag = tag.nextSibling

    return data

def run_bot(reddit):
    print("Getting 250 comments...")

    for comment in reddit.subreddit('test').comments(limit = 250):
        match = re.findall("[a-z]*[A-Z]*[0-9]*https://www.xkcd.com/[0-9]+", comment.body)
        if match:
            print("Link found with comment id: " + comment.id)
            xkcd_url = match[0]
            url_obj = urlparse(xkcd_url)
            xkcd_id = int((url_obj.path.strip("/")))
            myurl = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)

            file_obj_r = open(path,'r')

            try:
                explanation = fetchdata(myurl)
            except:
                print('Exception!!! Possibly incorrect xkcd URL...\n')
                # Typical cause for this will be a URL for an xkcd that does not exist (Example: https://www.xkcd.com/772524318/)
            else:
                if comment.id not in file_obj_r.read().splitlines():
                    print('Link is unique...posting explanation\n')
                    comment.reply(header + explanation + footer) 
			
					file_obj_r.close()

	                file_obj_w = open(path,'a+')
    	            file_obj_w.write(comment.id + '\n')
        	        file_obj_w.close()
            	else:
                	print('Already visited link...No reply needed\n')


def main():
    reddit = authenticate()
	while True:
		run_bot(reddit)

if __name__ == '__main__':
        main()
