![GitHub Tag](https://img.shields.io/github/v/tag/jonatasgz/Sample_Matcher)
![GitHub License](https://img.shields.io/github/license/jonatasgz/Sample_Matcher)

# Sample Matcher

Sample Matcher is a very simple app that allows the user to upload an .xlsx file containing characters or numbers on the first column (column A), and then input characters or numbers, one at a time, to check if they might be present on the uploaded list.

## Context

I developed this app to solve a very specific task I needed to perform as a laboratory worker and researcher: I had to find samples belonging to a list, but the samples were stored among other samples and I couldn't pinpoint their location without checking them one by one. Of course this simple app can be used for any kind of list matching as well.

## Live version

The latest version of this app can be used at my [server](https://sample.publica-me.com). 

No uploaded data is stored.

## Install instructions

You need to use a version of Python 3 to run this app.

1. Clone the repo:
```
$ git clone https://github.com/jonatasgz/Sample_Matcher.git
```

2. Install the requirements:
```
$ pip install -r requirements.txt
```

3. Run the app:
```
$ python app.py
```

The app will bind port 5020 by default.
On my production environment I start the app by running webserver.py with gunicorn:
```
$ gunicorn --workers 4 --timeout 600 --worker-class gevent --bind localhost:5020 webserver:app
```

A secret key called 'MATCHER_SECRET_KEY' is fetched from your environment, if it exists. Otherwise a .env file will be created on the app root folder with a new key.

## How to use

1. Select your .xlsx file and click Submit.
2. Enter a string in the Match sample card and click Verify. A barcode reader with automatic enter is ideal to the job, since the input field has autofocus enabled
3. If there is a match a 'Yes' message will be displayed. Otherwise a 'No' message will be displayed.

## Contributions

PR are accepted.
This app was a makeshift solution for a simple problem so may improvements can be made, to list some:
- If there is a match give feedback about what row the match is in.
- Allow for batch matching of different lists
- Add localization features

## License
This software is licensed under GNU General Public License v3.0 - check the LICENSE file for details.


