# pythonjedis.github.io
Python Jedis news, tutorials, and project list; conveniently drafted in HTML!

### The File Processor

This website uses a hacky, homebrewed static site generator written in python. Before you will see any of your changes, you must run main.py, so long as the directory structure stays intact, this should work.

```
+-- assets
|  +-- css
|  +-- img
|  +-- js
+-- templates~
|  +-- includes
+-- index.html
+-- main.py
```

Everything you will be editing to change the site, will be in the templates~ folder (The tilde is there to denote a hidden or working directory). This is plain old html/css/js. The tricky part is pretending like these files are in the root directory, so in order to access the assets folder, you just type something like <img src="/assets/img/stuff.png">. 
Using a templates directory like this allows us to add some preprocessing to our site, so that we can have file includes. This is handy because we can type <%= "header.html" %> and only edit one header.html file. Once we run main.py, all changes to the header will reflect across all the different files that include it.

That part of the program is a bit buggy because we are using readlines instead of by character. So for the time being, make sure you type out <%= "file.ext" %> like that all on one line. The program then goes and finds "file.ext" and copies it's contents to the main file.

### The Actual Web Technology

PythonJedis uses Zurb's Foundation CSS for styling and is limited to client side code only. Which means just HTML, CSS, and Javascript. We can make use of file includes as mentioned above to emulate some server side functionality; but otherwise this site is mainly for static information like links to resources and information about the github. However, further down the road as the site generator evolves, we will be adding things like loops and data storage so we can write blog posts using a markdown-like syntax.

### TODO

- main.py
 - Add Loops and a Data Schema for Dynamic Content
 - Read by character and not by line
- Content
 - Add links to github projects and explain them
 - Better organization of contact information
 - Skype info, reddit info, emails, etc.
 - Some user generated tutorials
