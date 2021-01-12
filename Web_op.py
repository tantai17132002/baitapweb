#Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup

#Các hàm cần thiết

#Hàm đọc nội dung của trang web theo url chỉ định
#kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    #Gửi yêu cầu truy cập url
    raw_page = requests.get(url)
    #lấy code html của trang web được trả về theo url
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

#Hàm lấy đường link web trong nội dung đọc về
#Kết quả trả về là 1 list chứa các đường link
def lay_cac_duong_link(content):
    a_tags = content.find_all("a")
    result = []
    for item in a_tags:
        link = item.get("href")
        result.append(link)
    return result

#Hàm kiểm tra tích hợp lệ của 1 đường link
#Kết quả trả về: True nếu hợp lệ, False nếu không hợp lệ
def kiem_tra_link(link):
    pass

#Hàm chỉnh sửa đường link nếu link là không đầy đủ
#Kết quả trả về là 1 đường link đầy đủ
def chinh_sua_link(link):
    pass


