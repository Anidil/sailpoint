from github import Github
import os
import pandas as pd
import datetime
from pprint import pprint


def clear(): os.system('cls') #on Windows System
clear()

token = os.getenv('GITHUB_TOKEN', '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')
g = Github(token)
repo = g.get_repo("Anidil/panidil-train")
closed_issues = repo.get_pulls(state="closed", sort="updated", direction="desc")
open_issues = repo.get_pulls(state="open", sort="updated", direction="desc")
draft_issues = repo.get_pulls(state="draft", sort="updated", direction="desc")
from_email='From: panidil@gmail.com'
to_email='To: anidilogs@gmail.com'
subject='Weekly Pull Request Summary'
line='==============================='

pulls_list = [closed_issues,open_issues, draft_issues]
status_list = ["closed","open","draft"]
pprint(from_email)
pprint(to_email)
pprint(subject)
pprint(line)

df = pd.DataFrame({'Closed': closed_issues})
df['Open'] = pd.Series(open_issues)
df["draft"] = pd.Series(draft_issues)
print(df)