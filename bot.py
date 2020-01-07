import webbrowser
import time
import random

while True:
    sites = random.choice(
        [
            "google.com",
            "youtube.com",
            "pornhub.com",
            "twitter.com",
            "linkedin.com",
            "facebook.com",
        ]
    )
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 3)
    time.sleep(seconds)
