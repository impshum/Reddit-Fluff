# Word Cloud Generator For Reddit Sidebar & Theme

### What is this?

Grabs the last 100 submissions of a subreddit, creates a wordcloud from the text and uploads it as a sidebar image on Reddit. Also writes the history to a wiki page along with uploading the image to Imgur and posting a new submission on chosen subreddit. Enjoy!

![Sidebar-Cloud](https://i.imgur.com/iyURIFQ.jpg)


### Install dependencies

    pip3 install -r requirements.txt

### Fill in the blanks     

Enter all your juicy details and set variables in config.py

### Run it

    python3 run.py

---

## Install to sidebar

* Add blank image link to the sidebar

      [](//recycledrobot.co.uk)

* Add CSS styles to stylesheet (edit to suit your theme)

        .side .md [href='//recycledrobot.co.uk'] {
          display: block;
          height: 318px;
          width: 318px;
          background: url(%%cloud%%);
          background-size: 318px;
          margin-left: -15px;
        }

* Upload cloud image placeholder

      data/cloud.jpg

---

## Install full theme

I've included a modified version of the popular theme [Naut](https://github.com/Axel--/Naut-for-reddit) that works nicely with the word cloud. Copy the contents of theme/styles.css over to the subreddit stylesheet and upload all the images in the theme folder. Take a look at the marvellous spangly [Live demo](https://www.reddit.com/r/recycledrobot/) if you like.

![Theme-Screenshot](https://i.imgur.com/lyBLFST.png)
