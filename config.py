# Get your Imgur client id from https://api.imgur.com/oauth2/addclient
imgurid = 'XXXX'

# Get your Reddit keys from https://www.reddit.com/prefs/apps/
client_id = 'XXXX-XXXX'
client_secret = 'XXXX'
reddit_user = 'XXXX'
reddit_pass = 'XXXX'
user_agent = 'Wordcloud generator for the very sidebar (by /u/impshum)'

# Subreddit to post to
target_sub = 'XXXX'

# Subreddit to pull data from
data_target = 'XXXX'

# Max number of posts to gather (100 max)
post_limit = 100

# Upload image to Imgur (needs to be on to post to sub and wiki)
post_to_imgur = 1

# Submit as a post to subreddit after generation
post_to_sub = 0

# Title of post
post_title = '/r/' + data_target

# Add image history to wiki page
post_to_wiki = 1

# Wiki page to edit
wiki_page = 'index'

# Insert text into wordcloud
insert_text = 0
insert_text_frequency = 8
insert_text_string = 'impshum'

# Word cloud colours
cloud_text_colour = 'hsl(0, 0%, 0%)'
cloud_background_colour = '#ffffff'
