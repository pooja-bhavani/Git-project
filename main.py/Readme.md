# Git and GitHub in one shot
To initailize a empty directory in git
```
git init  
```
![image](https://github.com/user-attachments/assets/dc5cdb52-3b1a-490c-821d-9547aed8a74d)

Gives information about which branch we are in, how many commits we have made, and how many tracked or untracked files are there.
```
Git status
```
![image](https://github.com/user-attachments/assets/cec46997-56c3-4795-953b-0f6ba6f29025)

# Commands for git and git branches
To add a file to staging area
```
git add 
```
Adds all tracked and untracked files
```
git add . 
```
Used to track the staged files after being added by git add.
```
git commit -m <commit message>
```
To checkout from one branch and create a new branch
```
git branch checkout -b 
```
![image](https://github.com/user-attachments/assets/e563e9a4-2fb6-4a04-850d-4f45b53b54e0)

To switch between branches
```
git checkout
```
![image](https://github.com/user-attachments/assets/b599d075-0932-44dc-8a43-bcaa47c0981f)
![image](https://github.com/user-attachments/assets/419e2ced-bde0-48f5-9c1b-8f6cc5318d78)
 
Gets Information about author who commits
```
Git log 
```
![image](https://github.com/user-attachments/assets/74f14553-a178-46c2-aef0-e018e486e29e)

Suppose I have added the file to staging area and i want to unstage it and keep it untracked. (Restore process)
```
git restore --staged <filename>
```
![image](https://github.com/user-attachments/assets/77eb1210-56cc-4eaa-9c3a-a159c06f983e)
![image](https://github.com/user-attachments/assets/5d9836a4-3721-4c42-b608-0fbbc789ed0d)

To permanently delete a file
![image](https://github.com/user-attachments/assets/1182772b-1032-43bb-829c-a08774283c67)
Creates a new commit that inverts the changes of a previous commit.
```
Git revert
```
![image](https://github.com/user-attachments/assets/20e9b870-6571-4d18-9313-4aa99e6be48f)
![image](https://github.com/user-attachments/assets/ab50fbf0-6c5c-4a6c-ad0a-8af76d07788c)

If I checkout and create a new branch from master it will have the changes of master and if I checkout and create a new branch from dev is will dev changes
![image](https://github.com/user-attachments/assets/2f41a811-1bbf-4b10-8c7a-e974714402bd)



![image](https://github.com/user-attachments/assets/03c57ae8-4ade-417f-8af9-4bd8d17f8417)



