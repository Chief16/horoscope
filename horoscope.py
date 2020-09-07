import requests
from bs4 import BeautifulSoup

print("Please Choose One")
print("Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces")
all_signs = ["aries","taurus","gemini","leo","virgo",'libra',"scorpio","sagittarius","capricorn","aquarius","pisces"]

def horo():
    while True:
        sign = input("Enter your Sign: ").lower()
        if sign in all_signs:
            url = (f"https://www.astrology.com/horoscope/daily/{sign}.html")
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            a = soup.find_all('p')[0].get_text()
            # for i in range(0,1):
            print(a)
            with open('test.txt','a+') as f:
                f.write("\n\n" + sign.upper()+" -- "+ a)
            inp = input("Wanna try Again ? [Y/N] ").lower()
            if inp == "y":
                print("Ok...")
                print("-----------------------------")
                pass
            else:
                print("Ok!")
                break
        elif sign not in all_signs:
            print("Wrong Sign chosen...")
            inp = input("Wanna try Again ? [Y/N] ").lower()
            if inp == "y":
                print("Ok...")
                print("-----------------------------")
                pass
            else:
                print("Ok!")
                break
        else:
            break

horo()