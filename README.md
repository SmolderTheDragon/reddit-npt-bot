# Reddit NPT bot

This is a Python script intended to be run once every Thursday at 11 pm. I plan to use the bot to make a post on the /r/mylittlepony subreddit entitled "Pony stuff you want to talk about but isn’t worthy of a dedicated thread!" This kind of thread was originally started by /u/QABJAB, then later taken over by /u/Trerrysaur and has become somewhat of a tradition on the subreddit on "No Pics Thursday" (NPT).

In general, most posts on /r/mylittlepony tend to be images of fan art. On Thursdays, in order to encourage more discussion-style posts, the moderators of /r/mylittlepony have decided to ban image posts, hence the name "No Pics Thursday" or "NPT" for short.

## Technical implementation

The code that interacts with the Reddit API to submit the post lives in `reddit-npt-bot.py`. The script reads which number thread we are on from the `num.txt` file on the disk (e.g. if we are on the 153rd iteration of the thread, then `num.txt` should just contain `153`), as well as the url of the previous thread from the `prev_thread.txt` url on the disk. It also generates a random emote to include in the text post which it then submits. I created a subreddit at [/r/NPTtest](https://www.reddit.com/r/NPTtest/) in order to test this script.

All the Python script does is submit the post to Reddit. The actual scheduling of the post should be done on the server side via `cron` on either Linux or Mac. The crontab should look something like this:

```
0 15 * * 4 cd /home/USERRNAME/reddit-npt-bot; /usr/bin/python3 reddit-npt-bot.py
```

Under ideal conditions, this should run the Pythons script to submit the Reddit post at 15:00 UTC every Thursday. It assumes that this git repository is cloned to your home repository. Additionally, the `reddit-npt-bot` directory must also include a `praw.ini` file that includes login credentials. For more information on how to fill out the `praw.ini` file, see [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

