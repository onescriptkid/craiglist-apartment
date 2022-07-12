# craiglist-apartment

A quick and dirty diagram for my experience chasing down aparments on Craigslist


<iframe
  src="sankey.html"
  style="width:100%; height:300px;"
></iframe>
<iframe
  src="http://google.com"
  style="width:100%; height:300px;"
></iframe>


Run the following strategies to alleviate the painful process:
- Enable email templates in [gmail](https://support.google.com/a/users/answer/9308990?hl=en) and madlib with the `email_template`
- Add *saved searches* to automatically receive listings via email notifications as they're posted.
- Avoid grifts by not clicking links and *always* seeing the listing IRL.

## Filters

I used the following filters

- Max Price $1600
- has image
- posted today
- bundle duplicates
- lat/lng search via circular map selection

## Email Template

I used the following template, `email-template`, to solicit craiglist sellers for the following categories

- rooms & shares
- apartments / housing for rent
- sublets & temporary

*email-template*

```
```

## Quickstart

```bash
virtualenv -p python3 ./venv
pip install -r requirements.txt
python sankey.py
```