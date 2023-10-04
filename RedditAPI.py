import praw

class RedditAPI:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def get_subreddit_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = subreddit.new(limit=limit)
        return posts

    def get_top_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = subreddit.top(limit=limit)
        return posts


class RedditPost:
    def __init__(self, blog_post_raw):
        self.comments = []

        self.title = blog_post_raw.title
        self.body = blog_post_raw.selftext
        self.score = blog_post_raw.score
        self.is_self_post = blog_post_raw.is_self
        self.comments.extend(blog_post_raw.comments)

    def __str__(self):
        return f"Title: {self.title}\n Body: {self.body}\n Score: {self.score}\n Is Self Post: {self.is_self_post}\n Comments: {self.get_comments()}"
    
    def comments_number(self):
        return len(self.comments)
    
    def get_comments(self):
        if len(self.comments) > 0:
            comments = []
            for comment in self.comments:
                comments.append(comment.body)
            return comments
        return ['No comments']

    def get_comment(self, index):
        if 0 <= index < len(self.comments):
            return self.comments[index].body
        return 'Invalid index'
    
    def to_csv(self):
        return [[self.title],[self.body],[self.get_comments()]]