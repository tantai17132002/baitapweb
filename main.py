#các thư viện cần thiết
import folder_op, Web_op

def start():
    url_list = ['http:''vietnamnet.vn'] #chứa các đường link sẽ được duyệt
    history = [] #chứa các đường link đã duyệt
    max_page = 1000 #quy định số lượng các trang web đã tải về
    count = 0 #đếm số lượng trang web đã tải về
    data_folder = "C:\\Users\MyPC\\Dowmloads\\

    #kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0):
        url = url_list.pop(0)
        page = web_op.doc_noi_dung(url)
        links = web_op.lay_cac_duong_link(page)
        for item in links: #Duyệt từng đường linnk thu được để kiểm tra tích hợp
            if web_op.luu_noi_dung_xuong_file(item): #Nếu đường link là hợp lệ thì tiếp tục


