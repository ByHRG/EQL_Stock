import requests
from bs4 import BeautifulSoup


class EQL:
    def run(self, url):
        req = requests.get("url")
        soup = BeautifulSoup(req.text, 'html.parser')
        output = {
            "Name": soup.find('input', {"id":"godNm"})["value"],
            "Image": "https://cdn.eqlstore.com"+soup.find('input', {"id":"defaultImage"})["value"],
            "Price": soup.find('input', {"id":"realPrice"})["value"],
            "Url": url,
            "Stock": {},
        }
        for i in req.text.split('<form id="singleShopInvForm"></form>')[-1].split('<div class="container cont_PR">')[0].replace("\n\n", "").split("<!-- 모든 아이템 출고여부 및 출고예정일이 동일함 여부 체크 -->"):
            if i == "":
                continue
            data = {
                i.split("itmNmIT")[-1].split('">')[0].split('value="')[-1]: i.split("totUsefulInvQty")[-1].split('">')[0].split('value="')[-1]
            }
            output["Stock"].update(data)
        return output



url = "https://www.eqlstore.com/product/GP9024071058167/detail"
print(EQL().run(url))
