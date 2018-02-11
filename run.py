import re
import os
import praw
import pyimgur
import datetime
import numpy as np
from halo import Halo
from PIL import Image
from wordcloud import WordCloud
from config import *


class Colour:
    Green, Red, Purple, White, Yellow = '\033[92m', '\033[91m', '\033[95m', '\033[0m', '\033[93m'

script_dir = os.path.dirname(__file__)
block_file = 'data/block.jpg'
block_path = os.path.join(script_dir, block_file)
cloud_file = 'data/cloud.jpg'
cloud_path = os.path.join(script_dir, cloud_file)
wiki_file = 'data/wiki.txt'
wiki_path = os.path.join(script_dir, wiki_file)
font_file = 'data/nexa.otf'
font_path = os.path.join(script_dir, font_file)


def generator():
    try:
        spinner = Halo(spinner='dots')
        spinner.start()

        now = datetime.datetime.now()
        timelogd = now.strftime('%d/%m/%Y')
        timelogh = now.strftime('%H:%M')

        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent,
                             username=reddit_user,
                             password=reddit_pass)

        def strip_urls(s):
            s = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b',
                       '', s, flags=re.MULTILINE)
            return(''.join(s))

        def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
            return cloud_text_colour

        cloud_fuel = []

        for submission in reddit.subreddit(data_target).new(limit=post_limit):
            title = submission.title
            bodytext = submission.selftext
            cloud_fuel.extend([title, bodytext])

        text_in = ' '.join(cloud_fuel)
        text = strip_urls(text_in)

        mask = np.array(Image.open(block_path))
        wc = WordCloud(background_color=cloud_background_colour, max_words=9999,
                       font_path=font_path, collocations=False, mask=mask, margin=30)

        if insert_text:
            fix = ' ' + insert_text_string
            me = fix * insert_text_frequency
            wc.generate(text + me)
        else:
            wc.generate(text)

        wc.recolor(color_func=color_func, random_state=3)
        wc.to_file(cloud_path)

        styles = reddit.subreddit(target_sub).stylesheet()
        css_refresh = styles.stylesheet

        reddit.subreddit(target_sub).stylesheet.delete_image('cloud')
        reddit.subreddit(target_sub).stylesheet.upload('cloud', cloud_path)
        reddit.subreddit(target_sub).stylesheet.update(css_refresh)

        if post_to_imgur:
            imgur = pyimgur.Imgur(imgurid)
            upload_image = imgur.upload_image(cloud_path, title=post_title)

        if post_to_sub:
            reddit.subreddit(target_sub).submit(
                post_title, url=upload_image.link)

        if post_to_wiki:
            get_wiki = reddit.subreddit(target_sub).wiki[wiki_page]
            old_wiki = get_wiki.content_md
            wiki = '* ' + timelogh + ' ' + timelogd + ' ' + upload_image.link
            new_wiki = old_wiki + '\n' + wiki
            get_wiki.edit(new_wiki)

        spinner.stop()
        print(Colour.Yellow + timelogh, Colour.Purple +
              timelogd, Colour.Green + 'Success ✓')

    except Exception as e:
        print(Colour.Yellow + timelogh, Colour.Purple +
              timelogd, Colour.Red + 'Fail ✘')
        print(Colour.Red + str(e))


if __name__ == '__main__':
    generator()
