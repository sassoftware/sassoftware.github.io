
#pip install Github

from github import Github
from github import Auth

import os

import json


def handle_repo(g, repo):
    data = {}
    data['name'] = repo.name
    data['archived'] = repo.archived
    data['created_at'] = str(repo.created_at)
    data['description'] = repo.description
    data['forks_count'] = repo.forks_count
    data['network_count'] = repo.network_count
    data['open_issues_count'] = repo.open_issues_count
    data['private'] = repo.private
    data['stargazers_count'] = repo.stargazers_count
    data['subscribers_count'] = repo.subscribers_count
    data['watchers_count'] = repo.watchers_count
    data['pushed_at'] = str(repo.pushed_at)
    data['updated_at'] = str(repo.updated_at)
    
    t = ""
    s = ""
    for k in data.keys():
        t += k + ','
        s += str(data[k]).replace(',','_') + ','
    s += "\n"
    t += '\n'

    return t,s,data

    # recent activity
    #  * list all repos in order of last update, truncate accordingly
    #  * most recent PR with author etc etc
    #  * forks_count
    #  * network_count(?)
    #  *  stargazers_count
    # *  updated_at
    #  * (what is topics?)
    #  * created_at
    #  * filter by archive

    # marquee project

# main loop
if __name__ == "__main__":
    TOKEN= os.environ["GITHUBSTATS"]
    auth = Auth.Token(TOKEN)
    g = Github(auth=auth)

    all_repos = []
    printed = False
    count = 0
    for repo in g.get_organization("sassoftware").get_repos():
        #print(json.dumps(dict(repo)))

        t,s,d = handle_repo(g, repo)
        #if not printed:
            #print(t.strip())
            #printed = True
        #print(s.encode('ascii', 'ignore').strip())
        count += 1
        if not d['archived'] and d['name'] != 'sassoftware.github.io':
            all_repos.append(d)
    g.close() 

    output = "data = "+json.dumps(all_repos)+";"
    #print(output)
    open("data.js", "w").write(output)

    # write to js/data.js