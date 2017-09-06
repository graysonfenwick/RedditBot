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




def authenicate():
    print("Authenticating...")
    reddit = praw.Reddit('nuzzyfipples', user_agent

