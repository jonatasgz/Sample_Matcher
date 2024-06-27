# Sample Matcher

Sample Matcher is a very simple app that allows the user to upload an .xlsx file containing characters or numbers on the first column (column A), and then input characters or numbers, one at a time, to check if they might be present on the uploaded list.

## Context

I developed this app to solve a very specific task I needed to perform as a laboratory worker and researcher: I had to find samples belonging to a list, but the samples were stored among other samples and I couldn't pinpoint their location withou checking one by one. Of course this simple app can be used for any kind of list matching as well.

## How to use

1. Select your .xlsx file and click Submit.
2. Enter a string in the Match sample card and click Verify.
3. If there is a match a 'Yes' message will be displayed. Otherwise a 'No' message will be displayed.

## Live version

The latest version of this app is hosted at (https://sample.pubica-me.com).

## Install instructions

You need to use a version of Python 3 to run this app.

1. Clone the repo:
´´´sh
$ git clone https://github.com/jonatasgz/Sample_Matcher.git
´´´

2. Install the requirements:
´´´sh
$ pip install -r requirements.txt
´´´

3. Run the app:
´´´sh
$ python app.py
´´´

This will run the webserver app binding it to port 5020 by default.
On my production environment I start the app by running webserver.py with gunicorn.

## Contributions

PR are accepted.
This app was a makeshift solution for a simple problem so may improvements can be made, to list some:
- If there is a match give feedback about what row the match is in.
- Allow for batch matching of different lists
- Add localization features

## License
This software is licensed under GNU General Public License v3.0 - check the LICENSE file for details.


