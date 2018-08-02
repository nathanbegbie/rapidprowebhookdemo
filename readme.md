Date: 8 May 2018
Author: Nathan Begbie
---------------------

This repo was created as a temporary endpoint for the rapidpro status demo.

To install:

```
$ virtualenv ve
$ source ve/bin/activate
(ve)$ pip install -r requirements.txt
(ve)$ export FLASK_APP=app
(ve)$ flask run
```

to use with ngrok:
- [install ngrok](https://ngrok.com/download)
- run `ngrok http 5000` (assuming you're using flask default port)
