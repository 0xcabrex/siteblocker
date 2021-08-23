## SITE BLOCKER

A simple site blocker that uses (modifies) `/etc/hosts` to redirect named websites to localhost (127.0.0.1).

**NOTE / REQURIEMENTS:** 
 - This only works on linux systems, It will not work on windows systems!
 - A file with the name `website_lists.txt` having all the websites that needs to be blocked.
 - File must run as sudo.

Running the file:
```python3
sudo python3 blocker.py <arguments>
```
It also takes 2 parameters: 
 - fix: Fixes the `etc/hosts` file.
 - block: Blocks file until `fix` is called again.


Limitations: Timings to block and free the websites are hard-coded into the if-blocks.