import os
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo(os.environ.get("BITBUCKET_REPO"))
# Your mock repo
mock_repo = git.Repo(os.environ.get("GITHUB_MOCK_REPO"))
# Copy commits from private repos to mock repo
importer = Importer([repo], mock_repo)
# my author email
importer.set_author(os.environ.get("AUTHOR"))
importer.import_repository()
