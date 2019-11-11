################################################################################
#
# Module: github-labeler.py
#
# Notes:
#
# Change label of issues.
#
################################################################################

import os
import sys

import github

from github import Label
from github import Github

################################################################################
# Main
################################################################################

def main():
    """ Main
    """
    
    github_handle = Github(os.environ["github_user"], os.environ["github_password"])

    repo = github_handle.get_repo("dotnet/coreclr")

    area_build_label = repo.get_label("area-Build")
    area_infra_label = repo.get_label("area-Infrastructure")
    build_issues = repo.get_issues(labels=[area_build_label], state="closed")

    for issue in build_issues:
        existing_labels = issue.get_labels()

        old_labels = []
        new_labels = [area_infra_label.name]
        for label in existing_labels:
            old_labels.append(label.name)
            if label.name != "area-Build":
                new_labels.append(label.name)

        print("Changing labels for {} , old labels [{}], new labels [{}]]".format(issue.html_url, " ".join(old_labels), " ".join(new_labels)))

        assert len(old_labels) == len(new_labels)

        issue.edit(labels=new_labels)

    return 0

################################################################################
# __main__
################################################################################

if __name__ == "__main__":
    main()