from github import Github
import os
import pandas as pd


def clear(): os.system('cls') #on Windows System
clear()

token = os.getenv('GITHUB_TOKEN', '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')
g = Github(token)
repo = g.get_repo("Anidil/panidil-train")
closed_issues = repo.get_pulls(state="closed")
open_issues = repo.get_pulls(state="open")
draft_issues = repo.get_pulls(state="draft")


pulls_list = [closed_issues,open_issues, draft_issues]
status_list = ["closed","open","draft"]


df = pd.DataFrame({'Closed': closed_issues})
df['Open'] = pd.Series(open_issues)
df["draft"] = pd.Series(draft_issues)
print(df)