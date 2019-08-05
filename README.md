# bash-scripts
Generic bash scripts to get things going. Firstly, setting up git locally, plus passwordless ssh to get things going smoothly...

## Setting up git locally

Once git bash is installed, configure user details:
```
git config --global user.name "Linus Torwalds"
git config --global user.email ltorvalds@linux.org
```
These are the user details that will show up in your commits when you push your changes to the remote.  
To use ssh over https, meaning you don't have to log in every time you push to remote, generate rsa key and put public part (.pub) on github; account Settings > SSH and GPG keys > New SSH key.  
Add the private part (no file extension) to your home direction .ssh folder, renaming it id_rsa, so you should have this file locally:
```
ls ~/.ssh/id_rsa
```
Test to make sure there is access:
```
ssh -vT git@github.com
```
All being well, the end of the debug session will show:
```
(...)
debug1: Offering public key: /u/.ssh/id_rsa RSA SHA256:GoTkDk9cJBpVL6maiR2wtyLQIDSni6kdvRFWTp3xC1c
debug1: Server accepts key: /u/.ssh/id_rsa RSA SHA256:GoTkDk9cJBpVL6maiR2wtyLQIDSni6kdvRFWTp3xC1c
debug1: Authentication succeeded (publickey).
Authenticated to github.com ([140.82.118.3]:22).
debug1: channel 0: new [client-session]
debug1: Entering interactive session.
debug1: pledge: network
debug1: client_input_channel_req: channel 0 rtype exit-status reply 0
Hi dsikar! You've successfully authenticated, but GitHub does not provide shell access.
debug1: channel 0: free: client-session, nchannels 1
Transferred: sent 2720, received 2228 bytes, in 0.2 seconds
Bytes per second: sent 13494.9, received 11053.9
debug1: Exit status 1
```
Next, the local repository needs a remote that tells the github server we are dealing with ssh.  
To see that is the case, look at the remote locate repository points to:
```
git remote -v
```
If you are pushing to the an https adress e.g. https://github.com/ltovalds/linux-kernel.git, change it to the ssh version e.g.:
```
git remote set-url origin git@github.com:ltorvalds/linux-kernel.git
```
And that should be the passwordless ssh added, and not need to login when pushing to remote.
