import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw
import datetime
import time

reddit = praw.Reddit(client_id='hzoV0WKPXFt1Og',
                     client_secret='WA7bEl8dawtf6MnXHRw3WmOslNQ',
                     user_agent='my user agent'
                     )

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
    return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
    return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
    return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


def process_comments(head, comment_list):
    try:
        negative = get_text_negative_proba(head.body)
        neutral = get_text_neutral_proba(head.body)
        positive = get_text_positive_proba(head.body)

        if negative > neutral and negative > positive:
            negative_comments_list.append(head.body) # Is adding the comments to the negative list
        elif positive > neutral and positive > negative:
            positive_comments_list.append(head.body) # Is adding the comments to the positive list
        else:
            neutral_comments_list.append(head.body) # Is adding the comments the neutral list
        process_comments(comment_list[1], comment_list[1:]) # traversing to the left side of the tree
        process_comments(head.replies[0], head.replies) # traversing to the right of the tree
    except IndexError:
        return


negative_comments_list = []  #creating the list for negative
neutral_comments_list = []   #creating the list for neutral
positive_comments_list = [] # creating the list for positive

comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')


oldest_time = []


def get_oldest_comment_any(head):
    time = head.created
    return time

def main():
    process_comments(comments[0], comments)
    print(comments.list().__len__()) # printing the total number of comments
    print()
    print('Negative list')
    print(len(negative_comments_list))
    print((negative_comments_list[0]))
    print()
    print('Neutral List')
    print(len(neutral_comments_list))
    print(neutral_comments_list[0])
    print()
    print('Positive list')
    print(len(positive_comments_list))
    print(positive_comments_list[0])
    print(get_oldest_comment_any(comments[1]))
    print(get_oldest_comment_any(comments[0]))


main()