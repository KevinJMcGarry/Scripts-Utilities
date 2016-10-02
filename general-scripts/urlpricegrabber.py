'''
URL PriceGrabber
if you consistently need to check the price on something - with just the url and the css selector for the
price of the product at that url, you can easily download and extract the prices a list of products.
Very useful, for example, if you have to check the price on a bunch of different items every day to see if the
price changed.

Will update this to store all the URLs and CSS price selectors in lists and have a for loop iterate over those
lists to create a new dictionary with the item and the price.

'''

import bs4, requests

def getBarnesAndNoblePrice(productUrl):
    response = requests.get(productUrl)  # download web page and store in response (large text string)
    response.raise_for_status()  # if the download fails, program will end with notification
    soup = bs4.BeautifulSoup(response.text, 'html.parser')  # convert text data to more readable html structure
    # html.parser option removes ugly warning messsage
    element = soup.select('#prodInfoContainer > form.pdp-form > p > span.price.current-price')
    # the above returns a list of matching elements in the selector
    return element[0].text.strip()  # we're only interested in the first element in the list returned,
    # stripping off all excess spacing and characters

url = 'http://www.barnesandnoble.com/w/doing-math-with-python-amit-saha/1121152671'
price = getBarnesAndNoblePrice(url)  # the evaluation of the function is returned and assigned to price
print('The price of the item you are interested in is {}'.format(price))
