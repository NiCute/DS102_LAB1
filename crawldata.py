import requests
import pandas as pd
import time 

# API lay duoc trong devtool
api_url = "https://tiki.vn/api/personalish/v1/blocks/listings"

# tao user Agent 
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

all_data = [] 

for i in range(1, 4): 
    # truy cap kho du lieu dienthoaimaytinhbang cua tiki
    params = {
        "limit": 40,
        "category": 1789,
        "page": i,
        "urlKey": "dien-thoai-may-tinh-bang"
    }
    
    try: 
        response = requests.get(api_url, headers=header, params=params)
        
        if response.status_code == 200:
            # sap xep du lieu thanh kieu dict de ngon ngu python doc
            json_data = response.json() 
            product = json_data.get("data", [])
            
            if len(product) == 0:
                break
                
            # Bat dau quet tung san pham trong danh sach
            for x in product:
                # Kiem tra quality sold co du lieu hay k
                if x.get("quantity_sold") != None:
                    # Neu co thi rut to giay ra, chep con so (value) vao luot_ban
                    luot_ban = x["quantity_sold"]["value"]
                else:
                    # Neu hang e, khong co to giay do thi tu dong ghi 0
                    luot_ban = 0

                item = {
                    "ten_san_pham":x.get("name"),
                    "thuong_hieu":x.get("brand_name"),
                    "gia_ban":x.get("price"),
                    "gia_goc": x.get("original_price") ,
                    "so_tien_da_giam": x.get("discount"), 
                    "danh_gia_trung_binh":x.get("rating_average"),
                    "so_luot_danh_gia": x.get("review_count"),
                    "luot_ban": luot_ban
                }
                # Bo san pham vao danh sach tong
                all_data.append(item)
            
    except:
        break

    # nghi 2 giay de tranh bi khoa IP
    time.sleep(2)

# Tao DataFrame tu danh sach vua thu thap
df = pd.DataFrame(all_data)
# Luu ra file CSV
df.to_csv("tiki_dienthoaimaytinhbang.csv",encoding="utf-8-sig") # chua loi tieng Viet


