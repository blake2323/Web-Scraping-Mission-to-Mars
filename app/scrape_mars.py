from splinter import Browser
from bs4 import BeautifulSoup


def scrape_all():
    executable_path = {'executable_path': '../chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_paragraph, news_paragraph = mars_news(browser)


    data = {
        'news_title' : news_title
        'news_paragraph' : news_paragraph
        'featured_image' : featured_image(browser)
    }

    return data


def mars_news(browser):
    return news_title, news_paragraph
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')




def feature_img(browser):
    return img.url
    