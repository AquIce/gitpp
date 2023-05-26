# git++

git++ is a tool to make git commands easier and more user friendly

## Commands

### clone

```html
git++ clone <user> <repo>
```
- Clones `https://github.com/<user>/<repo>` to `/<current_dir>/<repo>`

```html
git++ clone <user> <repo> <loc>
```
- Clones `https://github.com/<user>/<repo>` to `/<current_dir>/<loc>`

### commit

```html
git++ commit <message>
```
- Commits with `<message>`

### push

```html
git++ push
```
- Pushes to remote

### pull

```html
git++ pull
```
- Pulls from remote

### add

```html
git++ add
```
- Adds all files to staging area

```html
git++ add <files...>
```
- Adds `<files>` to staging area

### save

```html
git++ save <message>
```
- Adds all files, commits with `<message>` and pushes to remote

### copy

```html
git++ copy <user> <repo> <your_user> <your_repo>
```
- Copies `https://github.com/<user>/<repo>` to `https://github.com/<your_user>/<your_repo>`
- Uses "`Copied <user>/<repo> to <your_user>/<your_repo>`" as commit message
- Clones `<your_repo>` locally

```html
git++ copy <user> <repo> <your_user> <your_repo> <commit_message>
```
- Copies `https://github.com/<user>/<repo>` to `https://github.com/<your_user>/<your_repo>`
- Uses `<commit_message>` as commit message
- Clones `<your_repo>` locally

```html
git++ copy <user> <repo> <your_user> <your_repo> <commit_message> --no-clone
```
- Copies `https://github.com/<user>/<repo>` to `https://github.com/<your_user>/<your_repo>`
- Uses `<commit_message>` as commit message
- Does not clone `<your_repo>` locally

```html
git++ copy <user> <repo> <your_user> <your_repo> <commit_message> <loc>
```
- Copies `https://github.com/<user>/<repo>` to `https://github.com/<your_user>/<your_repo>`
- Uses `<commit_message>` as commit message
- Clones `<your_repo>` in `<loc>`

### empty

```html
git++ empty <repo_dir>
```
- Empties `<repo_dir>`
- The repo must be already cloned in `<repo_dir>`

```html
git++ empty <user> <repo_dir>
```
- Empties `<repo_dir>`
- The repo does not need to be cloned in `<repo_dir>` yet
- Clones `<repo>` from `<user>` to `<repo_dir>`

### status

```html
git++ status
```
Prints git status

### help

```html
git++ help
```
Prints help informations

### Others

```html
git++ <any_other_args...>
```
Runs the corresponding git command
