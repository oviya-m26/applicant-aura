import time

NEW_NAME = b"oviya-m26"
NEW_EMAIL = b"oviya.m2605@gmail.com"

def rewrite_callback(commit, metadata):
    now = int(time.time())
    commit.author_name = NEW_NAME
    commit.author_email = NEW_EMAIL
    commit.committer_name = NEW_NAME
    commit.committer_email = NEW_EMAIL
    commit.author_date = now
    commit.committer_date = now
