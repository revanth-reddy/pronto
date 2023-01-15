import git
from datetime import datetime, timedelta, timezone

'''
I am using git package "GitPython" installed from pip

To Install :
pip install GitPython
'''




'''
Replace the path link in the below line.
'''
repo = git.Repo('/Users/revanth/Desktop/TAU/react_base')

# Active branch
active_branch = repo.active_branch
print('active branch:', active_branch)
# # # # #

# Modified files
modified_files = repo.git.diff('--name-only')
print("local changes (whether modified or not):", modified_files!="")
# # # # #

# Last week authored
week_ago = datetime.now().replace(tzinfo=timezone(offset=timedelta())) - timedelta(days=7)

head_commit = repo.head.commit
was_authored_in_last_week = head_commit.authored_datetime > week_ago
print("recent commit (within last week):", was_authored_in_last_week)
# # # # #

# Authored by Rufus
was_authored_by_rufus = head_commit.author.name == 'Rufus'
print("blame Rufus (authored by Rufus):", was_authored_by_rufus)
# # # # #
