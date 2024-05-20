import git

import git


def gitDiff(branch1, branch2):
    format = '--name-only'
    commits = []
    g = git.Repo('./')
    differ = g.diff('%s..%s' % (branch1, branch2), format).split("\n")
    for line in differ:
        if len(line):
            commits.append(line)

    #for commit in commits:
    #    print '*%s' % (commit)
    return commits


g = git.Repo('./')
commit = g.iter_commits()




repo = git.Repo("./")
t = repo.head.commit.tree()
repo.git.diff(t)