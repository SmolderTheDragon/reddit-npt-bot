# Reddit NPT bot

This is a Python script intended to be run once every Thursday at 11 am EDT. I plan to use the bot to make a post on the /r/mylittlepony subreddit entitled "Pony stuff you want to talk about but isn’t worthy of a dedicated thread!" This kind of thread was originally started by /u/QABJAB, then later taken over by /u/Trerrysaur and has become somewhat of a tradition on the subreddit on "No Pics Thursday" (NPT).

In general, most posts on /r/mylittlepony tend to be images of fan art. On Thursdays, in order to encourage more discussion-style posts, the moderators of /r/mylittlepony have decided to ban image posts, hence the name "No Pics Thursday" or "NPT" for short.

## Technical implementation

The code that interacts with the Reddit API to submit the post lives in `reddit-npt-bot.py`. The script reads which number thread we are on from the `num.txt` file on the disk (e.g. if we are on the 153rd iteration of the thread, then `num.txt` should just contain `153`), as well as the url of the previous thread from the `prev_thread.txt` url on the disk. It also reads `quotes.json`, from which it pulls a quote from the show to include in the text post which it then submits. I created a subreddit at [/r/NPTtest](https://www.reddit.com/r/NPTtest/) in order to test this script.

All the Python script does is submit the post to Reddit. The actual scheduling of the post should be done on the server side via `cron` on either Linux or Mac. The crontab should look something like this:

```
0 15 * * 4 cd /home/USERRNAME/reddit-npt-bot; /usr/bin/python3 reddit-npt-bot.py
```

Under ideal conditions, this should run the Python script to submit the Reddit post at 15:00 UTC every Thursday (i.e. 11:00 am EDT). It assumes that this git repository is cloned to your home repository. Additionally, the `reddit-npt-bot` directory must also include a `praw.ini` file that includes login credentials. For more information on how to fill out the `praw.ini` file, see [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html).

## Step-by-step setup instructions

You have to be using either Linux (e.g. Ubuntu) or Mac.

1. [Install Python 3.7 or later](https://www.python.org/downloads/) if you don't have it
2. [Install pip](https://pip.pypa.io/en/stable/installing/) if you don't have it
3. Install PRAW using pip: `pip install praw`
4. Clone this repository: `git clone https://github.com/SmolderTheDragon/reddit-npt-bot.git`
5. Add a `praw.ini` file to the repository folder with your credentials. See [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html) for more info.
6. Ensure that `num.txt` and `prev_thread.txt` accurately reflect what the next thread number and previous thread URL should be.
7. Cron should be pre-installed if you're on Mac or Linux. Start up Cron by running `sudo systemctl enable cron` in your terminal.
8. Set up a crontab by running `crontab -e`. See the "Technical implementation" section above for an example of what the crontab should look like. This will schedule the Python script to be run every Thursday at 11:00 am EDT.

I also found it helpful to install `postfix` using the "local" installation option (on Linux: `sudo apt install postfix`). If for some reason the Python script throws an error that isn't logged, you can find the system print-out from Cron at `/var/mail/<username>`.