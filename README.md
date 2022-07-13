# craiglist-apartment

A quick and dirty diagram for my experience chasing down aparments on Craigslist


![Sankey gif](./assets/sankey.gif)

1

<iframe
  src="https://codepen.io/team/codepen/embed/preview/PNaGbb"
  style="width:100%; height:300px;"
></iframe>

2

<iframe
  src="assets/sankey.gif"
  style="width:100%; height:300px;"
></iframe>

3

<iframe
  src="sankey.html"
  style="width:100%; height:300px;"
></iframe>

4

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

## [Email Template](https://support.google.com/a/users/answer/9308990?hl=en) 

I used the following template, `email-template`, to solicit craiglist sellers for the following categories

- rooms & shares
- apartments / housing for rent
- sublets & temporary

<br>

![Do this to speed up emails](./assets/google_template.png)

*email-template*
<br>

```
I'm a <career> looking for a move-in date of <early|mid|late> <month> and am interested in checking out the rental unit. If that sounds good to you, I'm ready to move forward with the process.



Is there a good time for me to see the place in person? If so, what's the address?



I live in the area with a flexible work schedule so anytime works for me, but weekends and after <time> on weekdays is preferable.



Send an email or text if there's anything more you want to know about me.



<FirstName LastInitial>



Phone #: <phone #>

Email: <email>
```



## Quickstart

```bash
virtualenv -p python3 ./venv
pip install -r requirements.txt
python sankey.py
```

### Formatting and linting
```
black sankey.py
flake8 sankey.py
```