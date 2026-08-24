import re

with open('.github/workflows/auto-merge.yml', 'r') as f:
    content = f.read()

# Make sure headSha is available in all branches
old_1 = """              prAuthor = pulls.data[0].user.login;
              prTitle = pulls.data[0].title;
              prBranch = pulls.data[0].head.ref;
              headSha = context.payload.workflow_run.head_sha;"""
new_1 = """              prAuthor = pulls.data[0].user.login;
              prTitle = pulls.data[0].title;
              prBranch = pulls.data[0].head.ref;
              headSha = pulls.data[0].head.sha;"""

content = content.replace(old_1, new_1)

with open('.github/workflows/auto-merge.yml', 'w') as f:
    f.write(content)
