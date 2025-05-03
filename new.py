# Git and GitHub in one shot
Difference between centralized and distributed version control?
CVC: All version history and files are stored on a central server. Does’t have local storage to store copy of the data pushed to central repository. Developers pull the latest version and commit changes directly to the central repository.

DVCS: Every developer's machine has a full local copy of the entire repository, including the complete version history. Developers can commit, revert, and review history locally, even without internet access. Changes are later pushed to or pulled from a central/shared repository to collaborate with others.

Git init - is to initailize a empty directory in git
Git status - gives information about which branch we are in, how many commits we have made, and how many tracked or untracked files are there.

#Git Branches
What is Branch?
→ the branch is created from the main branch
Suppose we have run git init and created a branch which will be the main or master branch in which we have written the code we don’t want to change the main code but want to perform some experiments in that case we create seperate branches from main branch so a copy of the main code will also be in the new branch.

git reset: Deletes a commit from branch history. 
Git revert: creates a new commit to undo changes of last commit.
git rebase: moves commits from one branch onto another to keep history clean.  
  
Commands for git and git branches
```
git branch checkout -b <new branch> - to checkout from one branch and create a new branch.
git checkout - to switch between branches 
git add <filename> - Used to stage the untracked file
git add  .  - to add all tracked and untracked files
git commit -m <commit message> - Used to track the staged files after being added by git add.
Git log - to get Information about author who commits
```
once I have committed things to the branch then I can switch between branches using git checkout <branch-name>
If I delete a file and want to restore it again 

Here a Question arises how it will restore it back if we delete the file from trash as well?
-> Because it was stored in git it will get back the file even if you delete it.
Suppose I have added the file to staging area and i want to unstage it and keep it untracked.

* To permanently delete a file
Git revert - Creates a new commit that inverts the changes of a previous commit.

If I checkout and create a new branch from master it will have the changes of master and if I checkout and create a new branch from dev is will dev changes

If I checkout and create a new branch from master it will have the changes of master and if I checkout and create a new branch from dev is will dev changes


