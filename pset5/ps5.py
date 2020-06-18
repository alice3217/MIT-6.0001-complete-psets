# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    """
    Stores information on
    Guid: Global Unique Identifier (String)
    Title (String)
    Description (String)
    Link (String)
    Pubdate (String)
    """
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        """
        Returns
        -------
        The value of self.guid

        """
        return self.guid
    
    def get_title(self):
        """
        Returns
        -------
        The value of self.title

        """
        return self.title
    
    def get_description(self):
        """
        Returns
        -------
        self.description

        """
        return self.description
    
    def get_link(self):
        """
        Returns
        -------
        self.link

        """
        return self.link
    
    def get_pubdate(self):
        """
        Returns
        -------
        self.pubdate

        """
        return self.pubdate
    
    
    
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS
        
# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    """
    Fires when each word in the is present in its entirety and appears 
    consequtively in the text, separated only by spaces or punctuation 
    
    Trigger is not case sensitive
    
    Returns True if an alert should be generated
    False otherwise
    """
    def __init__(self, phrase):
        """
        Parameters - phrase : string that is being searched for

        Returns None
        """
        self.phrase = phrase.lower()
        
    def is_phrase_in(self, text):
        """
        returns True if the whole phrase is present in text
        False otherwise
        """
      
        text = str(text).lower()
    #remove punctuation and replace it with spaces    
        for char in string.punctuation:
            if char in text:
                text = text.replace(char, " ")
    #make a list of the words in text        
        text_list = text.split(" ")
    #remove the extra spaces that may have been caused by splitting a list with extra spaces
        while "" in text_list:
            text_list.remove("")
    
    #make a list of the words in phrase        
        phrase_list = self.phrase.split(" ")
        
    #if phrase is longer than text then phrase is not in text
        if len(phrase_list) > len(text_list):
            return False
        
        result = []
        for word in phrase_list:
            if word in text_list:
                result.append("yes")
            
            else:
                result.append("no")
    #checks if all the words in phrase are in text       
        if "no" in result:
            return False
        elif "yes" in result:
            #to check if they are in the correct order
            phrase_again = " ".join(phrase_list)
            text_again = " ".join(text_list)
        
            if phrase_again in text_again:
                return True
            else:
                return False
    

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    """
    Fires when a news item's title contains a given phrase
    """
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
         """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
         return self.is_phrase_in(story.get_title())
                   


# Problem 4
# TODO: DescriptionTrigger
         
class DescriptionTrigger(PhraseTrigger):
    """
    fires when a news item's description contains a given phrase
    """
    
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in(story.get_description())
    
    

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    """
    Takes in time in EST as a string in the format of "3 Oct 2016 17:00:10 "
    """
    def __init__(self, time_inp):
        
        self.time_inp = datetime.strptime(time_inp, "%d %b %Y %H:%M:%S")
    
    def get_time(self): 
        return self.time_inp

    
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """
    fires when a story is published strictly before the trigger’s time
    """
    def __init__(self, time_inp):
        TimeTrigger.__init__(self, time_inp)
        
    def evaluate(self, story):
        story_pub_date = story.get_pubdate()
        self.time_inp = self.time_inp.replace(tzinfo=pytz.timezone("EST"))
            
        story_pub_date = story_pub_date.replace(tzinfo=pytz.timezone("EST"))
        if story_pub_date < self.time_inp:
            return True
        else:
            return False
        
            
    
class AfterTrigger(TimeTrigger):
    """
    fires when a story is published strictly after the trigger’s time
    """
    def __init__(self, time_inp):
        TimeTrigger.__init__(self, time_inp)
        
    def evaluate(self, story):
        story_pub_date = story.get_pubdate()
        self.time_inp = self.time_inp.replace(tzinfo=pytz.timezone("EST"))
            
        story_pub_date = story_pub_date.replace(tzinfo=pytz.timezone("EST"))
        if story_pub_date > self.time_inp:
            return True
        else:
            return False
            
       
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    """
    Produces its output by inverting the output of another trigger
    """
    def __init__(self, other_trig):
        
        self.other_trig = other_trig
        
    def evaluate(self, story):
        
        result = not self.other_trig.evaluate(story)
        return result
    

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    """
    take two triggers as arguments to its constructor, 
    and fires on a news story only if both of the inputted triggers 
    would fire on that item
    """
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, story):
        result = self.trig1.evaluate(story) and self.trig2.evaluate(story)
        return result
    
        
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    """
    Takes two triggers as arguments to its constructor, 
    fires if either one (or both) of its inputted triggers would fire on that item.
    """
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
        
    def evaluate(self, story):
        result = self.trig1.evaluate(story) or self.trig2.evaluate(story)
        return result
    
    
#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    list_good_stories = []
    for trigger in triggerlist:
       for story in stories:
           if trigger.evaluate(story):
               list_good_stories.append(story)

    return list_good_stories

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Covid")
        t2 = DescriptionTrigger("doctors")
        t3 = DescriptionTrigger("vaccine")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

