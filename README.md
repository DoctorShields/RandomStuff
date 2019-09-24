# RandomStuff

## Git
### That annoying LF/CRLF warning
`git config core.autocrlf false`

or

`git config --global core.autocrlf false`

### Making pretty trees
```
git config --global alias.lgb "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n' --abbrev-commit --date=relative --branches"

git lgb
```
