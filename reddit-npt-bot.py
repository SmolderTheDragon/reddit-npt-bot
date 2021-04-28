import praw
from random import randrange
import logging

# initialize logger
logging.basicConfig(filename='status.log', level=logging.DEBUG)

# configure praw; authentication details are in a separate praw.ini file
try:
	reddit =  praw.Reddit('bot1')
	reddit.validate_on_submit = True
	subreddit = reddit.subreddit("NPTtest")  # /r/NPTtest is a subreddit I made to test this bot
except Exception:
	logging.exception('An error occurred when attempting to configure praw')
	raise

def generate_random_emote():
	alphastring = 'abcefgh'
	table = alphastring[randrange(len(alphastring))]
	column = str(randrange(4))
	row = str(randrange(10))
	return '[](/{0}{1}{2})'.format(table, column, row)

def submit_new_NPT_post():
	# grabbing which number NPT thread we are on from the disk
	with open('num.txt') as f:
		num = f.read()

	# grabbing the link to the previous NPT thread from disk
	with open('prev_thread.txt') as p:
		prev_thread = p.read()

	# get the id of the "Discussion" flair from the subreddit's link flairs
	discussion_flair_id = None
	for flair_template in subreddit.flair.link_templates:
		if 'Discussion' in flair_template['text']:
			discussion_flair_id = flair_template['id']
			break
	if discussion_flair_id is None:
		logging.error('The discussion flair ID could not be found.')
		return

	# title of the NPT post
	title = 'Pony stuff you want to talk about but isn’t worthy of a dedicated thread! #{0}'.format(num)

	# text of the NPT post
	text = "[Previous thread]({0})\n\n{1}This is the thread for any pony-related topics, thoughts, and questions you can think of that are too small to deserve their own thread. That's all you need know.".format(prev_thread, generate_random_emote())
	text += "\n\n*This post was submitted automatically. [Source code](https://github.com/SmolderTheDragon/reddit-npt-bot).*"

	# submit the thread
	submission = subreddit.submit(title=title, selftext=text, flair_id=discussion_flair_id)

	# update next NPT thread number on the disk
	with open('num.txt', 'w') as f:
		f.write(str(int(num) + 1))

	# update previous thread on disk with current thread URL
	with open('prev_thread.txt', 'w') as p:
		p.write(submission.url)

try:
	submit_new_NPT_post()
except Exception:
	logging.exception('An error occurred when attempting to submit the post')
	raise
