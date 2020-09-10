# WARNING
I do not warranty this in any way. The code seems to work fine for me but do your due diligence and read the code before running. I don't want people accidentally deleting things that they need.

# notion-empty-trash
This script permanantly deletes pages in notion trash.

As an experiment, I decided to write a selenium script to permanently delete all of my deleted notion pages. I want to see if 
it positively affects performance.

Seems that it might, a little. Not much though...

So let this be a spring cleaning type script.

# Usage
## Chrome Driver
Head to the url below and download a driver for your version of chrome (go to chrome settings > about) and put it somewhere you can reference later.

https://chromedriver.chromium.org/downloads

## Config
Head to config.py and fill in the variables for your run.

These are used for various items, namely for authentication to notion.

token_v2 - login creds, head to devtools in your browser to notion cookies to retrieve this

notion_user_id - login creds, head to devtools in your browser to notion cookies to retrieve this

notion_users - login creds, head to devtools in your browser to notion cookies to retrieve this

landing_page - a page for notion to navigate to, could just be notion.so if you want. Essentially telling the driver 
where to head.

chrome_driver_location - the location of the chromedriver on your system downloaded in the previous script

## Running the script

simply install requirements with 

`pip3 install -r requirements.txt`

Then run with 

`python3 main.py`

# How does this work
First, cookies are added based on your config and notion is navigated to.

Then the script gathers a list of visible items in your trash that can be permanently deleted.

it then loops over them and clicks delete and confirms. When it runs out, it gathers more until they are all gone.