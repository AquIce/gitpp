'''
 > git++ is a python script that allows you to use git commands in an easier and more user friendly way.
'''

import os
import sys
import shutil

def _git_copy_files(src, dest):
	src = os.path.abspath(src)
	dest = os.path.abspath(dest)
	for i in os.listdir(os.path.join(src)):
		if (i == '.git'):
			continue
		if (os.path.isfile(os.path.join(src, i))):
			shutil.copy2(os.path.join(src, i), dest)
		else:
			shutil.copytree(os.path.join(src, i), os.path.join(dest, i))

def clone(user, repo, loc=''):
	os.system(f'git clone https://github.com/{user}/{repo}.git {loc}')

def commit(message):
	os.system(f'git commit -m "{message}"')

def push():
	os.system('git push')

def pull():
	os.system('git pull')

def add(filenames):
	for i in filenames:
		os.system(f'git add {i}')

def add_all():
	os.system('git add .')

def save(message):
	add_all()
	commit(message)
	push()

def copy(user, repo, your_user, your_repo, commit_message='', no_clone=False, loc=''):
	if (commit_message == ''):
		commit_message = f'Copied {user}/{repo} to {your_user}/{your_repo}'
	if (loc == ''):
		clone(your_user, your_repo)
		loc = your_repo
	else:
		clone(your_user, your_repo, loc)
	clone(user, repo)
	_git_copy_files(repo, your_repo)
	os.chdir(your_repo)
	add_all()
	commit(commit_message)
	push()
	os.chdir('..')
	os.system(f'rmdir {repo} /s /q')
	if (no_clone):
		os.system(f'rmdir {loc} /s /q')

def empty(repo_dir, user=''):
	if (not os.path.exists(repo_dir)):
		if (user == ''):
			print('fatal error: No user provided')
			sys.exit()
		clone(user, repo_dir)
	repo_dir = os.path.abspath(repo_dir)
	os.chdir(repo_dir)
	for i in os.listdir(os.path.join(repo_dir)):
		if (i == '.git'):
			continue
		if (os.path.isfile(os.path.join(repo_dir, i))):
			os.remove(os.path.join(repo_dir, i))
		else:
			shutil.rmtree(os.path.join(repo_dir, i))
	add_all()
	commit('Empty commit')
	push()
	os.chdir('..')
	os.system(f'rmdir {repo_dir} /s /q')

def status():
	os.system('git status')

def help():
	print('''git++ v1.0 by @SinisterIcy

clone <user> <repo>: Clones <repo> from <user> to current directory + <repo>
clone <user> <repo> <loc>: Clones <repo> from <user> to <loc>
commit <message>: Commits with <message>
push: Pushes to remote
pull: Pulls from remote
add: Adds all files to staging area
add <files...>: Adds <files> to staging area
save <message>: Adds all files, commits with <message> and pushes to remote
copy <user> <repo> <your_user> <your_repo>: Copies <repo> from <user> to <your_repo> from <your_user> with 'Copied <user>/<repo> to <your_user>/<your_repo>' as commit message
copy <user> <repo> <your_user> <your_repo> <commit_message>: Copies <repo> from <user> to <your_repo> from <your_user> with <commit_message>
copy <user> <repo> <your_user> <your_repo> <commit_message> --no-clone: Copies <repo> from <user> to <your_repo> from <your_user> with <commit_message> and does not clone the repo
copy <user> <repo> <your_user> <your_repo> <commit_message> <loc>: Copies <repo> from <user> to <your_repo> from <your_user> with <commit_message> in <loc>
empty <repo_dir>: Empties <repo_dir> (the repo must be right in <repo_dir>)
empty <user> <repo_dir>: Empties <repo_dir> (the repo does not need to be right in <repo_dir>) and clones <repo> from <user> to <repo_dir>
status: Prints git status
<any_other_args>: Runs the corresponding git command
help: Prints this message''')

def other(args):
	os.system('git', ' '.join(args))

if (__name__ == '__main__'):
	args = sys.argv[1:]
	if (len(args) == 0):
		help()
	elif (args[0] == 'clone'):
		if (len(args) != 3 and len(args) != 4):
			print(
				'fatal error: wrong number of arguments provided (expected 2: user, repo or 3: user, repo, loc)')
			sys.exit()
		if (len(args) == 3):
			clone(args[1], args[2])
		else:
			clone(args[1], args[2], args[3])
	elif (args[0] == 'commit'):
		if (len(args) != 2):
			print('fatal error: wrong number of arguments provided (expected 1: message)')
			sys.exit()
		commit(args[1])
	elif (args[0] == 'push'):
		if (len(args) != 1):
			print('fatal error: wrong number of arguments provided (expected 0)')
			sys.exit()
		push()
	elif (args[0] == 'pull'):
		if (len(args) != 1):
			print('fatal error: wrong number of arguments provided (expected 0)')
			sys.exit()
		pull()
	elif (args[0] == 'add'):
		if (len(args) == 1):
			add_all()
		else:
			add(args[1:])
	elif args[0] == 'save':
		if len(args) != 2:
			print('fatal error: wrong number of arguments provided (expected 1: message)')
			sys.exit()
		save(args[1])
	elif (args[0] == 'copy'):
		if (len(args) != 5 and len(args) != 6 and len(args) != 7):
			print('fatal error: wrong number of arguments provided (expected 4: user, repo, your_user, your_repo, 5: user, repo, your_user, your_repo, commit_message or 6: user, repo, your_user, your_repo, commit_message, no_clone/loc)')
			sys.exit()
		if (len(args) == 5):
			copy(args[1], args[2], args[3], args[4])
		elif (len(args) == 6):
			copy(args[1], args[2], args[3], args[4], args[5])
		elif (len(args) == 7):
			if (args[6] == '--no-clone'):
				copy(args[1], args[2], args[3], args[4], args[5], True)
			else:
				copy(args[1], args[2], args[3],
					 args[4], args[5], False, args[6])
	elif (args[0] == 'empty'):
		if (len(args) != 3 and len(args) != 2):
			print(
				'fatal error: wrong number of arguments provided (expected 1: repo_dir or 2: user, repo_dir )')
			sys.exit()
		if (len(args) == 2):
			empty(args[1])
		else:
			empty(args[2], args[1])
	elif (args[0] == 'status'):
		status()
	elif (args[0] == 'help'):
		help()
	else:
		other(args)
