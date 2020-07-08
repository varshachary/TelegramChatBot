import re
import bs4
import requests


def text(input_text):
    """
    :type input_text: object
    """
    params = {"translatetext": input_text}

    # You can replace the target url your own api url
    target_url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(target_url, data=params)

    soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[37].strip("\r\n")
    return giz_text
