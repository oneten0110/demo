rm: cannot remove '/etc/post-install/01-devices.post': Permission denied
rm: cannot remove '/etc/post-install/03-mtab.post': Permission denied
rm: cannot remove '/etc/post-install/06-windows-files.post': Permission denied
rm: cannot remove '/etc/post-install/99-post-install-cleanup.post': Permission denied

admin@DESKTOP-A6P899I MINGW64 /d/grid/venv
$ git^C

admin@DESKTOP-A6P899I MINGW64 /d/grid/venv
$  source /d/grid/venv/Scripts/activate
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv
$  git init
Initialized empty Git repository in D:/grid/venv/.git/
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git add .
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git commit am"this is a test"
error: pathspec 'amthis is a test' did not match any file(s) known to git
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git commit -am"this is a test"
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git branch
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git checkout new1
error: pathspec 'new1' did not match any file(s) known to git
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git branch
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git -u origin matser
unknown option: -u
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]    
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]        
           <command> [<args>]
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git -u origin master
unknown option: -u
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]    
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]        
           <command> [<args>]
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git remote -v
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git config --global user.name "oneten0110"
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git config --global user.email "hemachandran.p21@gmail.com"
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u orgin master
error: src refspec master does not match any
error: failed to push some refs to 'orgin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git branch
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (master)
$ git branch -M main
git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "Initial commit"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git init
Reinitialized existing Git repository in D:/grid/venv/.git/
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -am"this is a test"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "Initial commit"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git branch
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'origin'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ gi push
bash: gi: command not found
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git remote add origin https://github.com/oneten0110/demo
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git -am commit "a"
unknown option: -am
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -am"this is a test"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git init 
Reinitialized existing Git repository in D:/grid/venv/.git/
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git branch
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -am "g"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ls
a.py  c.html  Include/  Lib/  pyvenv.cfg  sample.pdf  Scripts/
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
git commit -m "Initial commit"
git push -u origin main
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git status
echo "# Demo Repo" > README.md
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ls
a.py  c.html  Include/  Lib/  pyvenv.cfg  README.md  sample.pdf  Scripts/
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git -am commit "this is a test"
unknown option: -am
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
           [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
           [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
           <command> [<args>]
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -am "this is a test"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ echo "hello" > test.txt
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ls
a.py  c.html  Include/  Lib/  pyvenv.cfg  README.md  sample.pdf  Scripts/  test.txt
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git status
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "First commit"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ls -la
total 32
drwxr-xr-x 1 admin 197121    0 Mar 13 12:35 ./
drwxr-xr-x 1 admin 197121    0 Mar 13 12:14 ../
drwxr-xr-x 1 admin 197121    0 Mar 13 12:36 .git/
-rw-r--r-- 1 admin 197121   71 Mar 13 10:53 .gitignore
-rw-r--r-- 1 admin 197121  952 Mar 13 12:29 a.py
-rw-r--r-- 1 admin 197121 3533 Mar 13 11:03 c.html
drwxr-xr-x 1 admin 197121    0 Mar 13 10:52 Include/
drwxr-xr-x 1 admin 197121    0 Mar 13 10:52 Lib/
-rw-r--r-- 1 admin 197121  213 Mar 13 10:53 pyvenv.cfg
-rw-r--r-- 1 admin 197121   12 Mar 13 12:32 README.md
-rw-r--r-- 1 admin 197121 2830 Oct  5  2024 sample.pdf
drwxr-xr-x 1 admin 197121    0 Mar 13 11:53 Scripts/
-rw-r--r-- 1 admin 197121    6 Mar 13 12:35 test.txt
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ cat .gitignore
# Created by venv; see https://docs.python.org/3/library/venv.html
*
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ^C
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ nano .gitignore
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -am "this is a test"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "this is a test"
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
git commit -m "First commit"
git push -u origin main
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ cat .gitignore
# Created by venv; see https://docs.python.org/3/library/venv.html
*
git add .
git commit -m "First commit"
git push -u origin main



(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ nano .gitignore
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git rm -r --cached .
fatal: pathspec '.' did not match any files
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'sample.pdf', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'test.txt', LF will be replaced by CRLF the next time Git touches it
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git rm -r --cached .
rm '.gitignore'
rm 'README.md'
rm 'a.py'
rm 'c.html'
rm 'pyvenv.cfg'
rm 'sample.pdf'
rm 'test.txt'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "First commit"
On branch main

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        a.py
        c.html
        pyvenv.cfg
        sample.pdf
        test.txt

nothing added to commit but untracked files present (use "git add" to track)
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/oneten0110/demo'
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git add .
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'sample.pdf', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'test.txt', LF will be replaced by CRLF the next time Git touches it
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   a.py
        new file:   c.html
        new file:   pyvenv.cfg
        new file:   sample.pdf
        new file:   test.txt

(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit -m "First commit"
[main (root-commit) cf52a0e] First commit
 7 files changed, 360 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 a.py
 create mode 100644 c.html
 create mode 100644 pyvenv.cfg
 create mode 100644 sample.pdf
 create mode 100644 test.txt
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
To https://github.com/oneten0110/demo
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/oneten0110/demo'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git pull origin main --allow-unrelated-histories
remote: Enumerating objects: 35, done.
remote: Counting objects: 100% (35/35), done.
remote: Compressing objects: 100% (25/25), done.
remote: Total 35 (delta 6), reused 32 (delta 3), pack-reused 0 (from 0)
Unpacking objects: 100% (35/35), 621.32 KiB | 769.00 KiB/s, done.
From https://github.com/oneten0110/demo
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
hint: Waiting for your editor to close the file... Vim: Error reading input, exiting...
Vim: preserving files...
Vim: Finished.
error: there was a problem with the editor 'vi'
Not committing merge; use 'git commit' to complete the merge.
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main|MERGING)
$ git push -u origin main
To https://github.com/oneten0110/demo
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/oneten0110/demo'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main|MERGING)
$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        new file:   Meet - dsr-vnun-hve - Google Chrome 3_12_2026 10_58_27 AM.png
        new file:   a.txt
        new file:   c.py
        new file:   complete_git_tutorial_readme.md
        new file:   d.py
        new file:   f.py
        new file:   python
        new file:   "\342\227\217 aa.py - foundation - Visual Studio Code 3_10_2026 11_39_55 AM.png"
        new file:   "\342\227\217 exp.html - foundation - Visual Studio Code 3_10_2026 10_19_24 AM.png"

(venv)
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main|MERGING)
$ git commit
[main 8096135] Merge branch 'main' of https://github.com/oneten0110/demo
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ ls -la .git/.MERGE_MSG.swp
-rw-r--r-- 1 admin 197121 12288 Mar 13 12:45 .git/.MERGE_MSG.swp
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ rm .git/.MERGE_MSG.swp
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git commit --no-edit
On branch main
nothing to commit, working tree clean
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git status
On branch main
nothing to commit, working tree clean
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$ git push -u origin main
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (11/11), 3.44 KiB | 3.44 MiB/s, done.
Total 11 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To https://github.com/oneten0110/demo
   e8c4abd..8096135  main -> main
branch 'main' set up to track 'origin/main'.
(venv) 
admin@DESKTOP-A6P899I MINGW64 /d/grid/venv (main)
$