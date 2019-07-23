from splinter import Browser
from bs4 import BeautifulSoup


def scrape_all():
    executable_path = {'executable_path': '../chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)


    data = {
        'news_title' : news_title,
        'news_paragraph' : news_paragraph,
        'featured_image' : featured_image(browser)
    }

    return data


def mars_news(browser):
    
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    content_element = slide_elem.find('div', class_="content_title")
    news_title = content_element.get_text()
    news_paragraph = slide_elem.find('div', class_="article_teaser_body").text
    return news_title, news_paragraph




def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info   ', wait_time=2)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    img_url_rel
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
        
    return img_url

    