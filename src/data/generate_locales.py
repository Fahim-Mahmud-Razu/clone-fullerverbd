import os
import json

BASE_DIR = "/home/razu/Explore Folders/clone-fullerverbd"
DATA_DIR = os.path.join(BASE_DIR, "src", "data")

jp_data = {
  "locale": "jp",
  "title": "Max Gloves BD Ltd.",
  "nav_heading": "私たちの商品",
  "process_heading": "私たちの作業プロセス",
  "categories_heading": "当社の製品カテゴリー",
  "process": [
    { "num": "01", "title": "原材料", "url": "/jp/raw-materials", "img": "/front-end/img/service/rawmaterials.jpg" },
    { "num": "02", "title": "切断工程", "url": "/jp/cutting-process", "img": "/front-end/img/service/catting.jpg" },
    { "num": "03", "title": "縫製工程", "url": "/jp/sewing-process", "img": "/front-end/img/service/swwim.jpg" },
    { "num": "04", "title": "包装", "url": "/jp/packaging", "img": "/front-end/img/service/Packaging.jpg" }
  ],
  "categories": [
    { "id": 23, "title": "革冬用手袋", "url": "/jp/category/23", "img": "/media-library/wenter.png" },
    { "id": 17, "title": "革ドライバー手袋", "url": "/jp/category/17", "img": "/media-library/driver.png" },
    { "id": 18, "title": "本革手袋", "url": "/jp/category/18", "img": "/media-library/Grain-Gloves_jp.png" },
    { "id": 19, "title": "床革手袋", "url": "/jp/category/19", "img": "/media-library/split_jp.png" },
    { "id": 20, "title": "革溶接手袋", "url": "/jp/category/20", "img": "/media-library/walding.png" },
    { "id": 21, "title": "革パーム手袋", "url": "/jp/category/21", "img": "/media-library/palm_gloves_jp.png" },
    { "id": 25, "title": "レザー溶接アパレル", "url": "/jp/category/25", "img": "/media-library/pant.png" },
    { "id": 24, "title": "レザー溶接アパレル", "url": "/jp/category/24", "img": "/media-library/jek.png" },
    { "id": 27, "title": "合成皮革手袋", "url": "/jp/category/27", "img": "/media-library/Microfiber-Gloves_jp.png" },
    { "id": 29, "title": "メカニックグローブ", "url": "/jp/category/29", "img": "/media-library/0172317000.png" },
    { "id": 30, "title": "インパクトグローブ", "url": "/jp/category/30", "img": "/media-library/0000025056864_1.png" },
    { "id": 31, "title": "100% 綿スムーズ手袋", "url": "/jp/category/31", "img": "/media-library/cotton_new_gloves_jp.png" }
  ],
  "stats": [
    { "icon": "flaticon-apartment", "value": "1,200", "title": "熟練労働者" },
    { "icon": "flaticon-industry", "value": "12,000", "title": "平方メートル" },
    { "icon": "flaticon-helmet", "value": "1,00,000", "title": "月間手袋生産数（ダース）" },
    { "icon": "flaticon-happy", "value": "40", "title": "総生産数（100万組）" }
  ]
}

kr_data = {
  "locale": "kr",
  "title": "Max Gloves BD Ltd.",
  "nav_heading": "우리의 제품",
  "process_heading": "우리의 작업 과정",
  "categories_heading": "우리의 제품 카테고리",
  "process": [
    { "num": "01", "title": "원자재", "url": "/kr/raw-materials", "img": "/front-end/img/service/rawmaterials.jpg" },
    { "num": "02", "title": "절단 공정", "url": "/kr/cutting-process", "img": "/front-end/img/service/catting.jpg" },
    { "num": "03", "title": "봉제 공정", "url": "/kr/sewing-process", "img": "/front-end/img/service/swwim.jpg" },
    { "num": "04", "title": "포장", "url": "/kr/packaging", "img": "/front-end/img/service/Packaging.jpg" }
  ],
  "categories": [
    { "id": 23, "title": "가죽 겨울 장갑", "url": "/kr/category/23", "img": "/media-library/wenter.png" },
    { "id": 17, "title": "가죽 드라이버 장갑", "url": "/kr/category/17", "img": "/media-library/driver.png" },
    { "id": 18, "title": "가죽 그레인 장갑", "url": "/kr/category/18", "img": "/media-library/Grain-Gloves_jp.png" },
    { "id": 19, "title": "가죽 분할 장갑", "url": "/kr/category/19", "img": "/media-library/1683696630133.png" },
    { "id": 20, "title": "가죽 용접 장갑", "url": "/kr/category/20", "img": "/media-library/1681625619walding.png" },
    { "id": 21, "title": "가죽 손바닥 장갑", "url": "/kr/category/21", "img": "/media-library/1683343527152.png" },
    { "id": 25, "title": "가죽 용접 의류", "url": "/kr/category/25", "img": "/media-library/pant.png" },
    { "id": 24, "title": "가죽 용접 의류", "url": "/kr/category/24", "img": "/media-library/jek.png" },
    { "id": 27, "title": "합성 가죽 장갑", "url": "/kr/category/27", "img": "/media-library/1681354887170_1.png" },
    { "id": 29, "title": "기계공의 장갑", "url": "/kr/category/29", "img": "/media-library/16813546270172317000 (2).png" },
    { "id": 30, "title": "임팩트 장갑", "url": "/kr/category/30", "img": "/media-library/16813520360000025056864_1.png" },
    { "id": 31, "title": "100% 면 인터록 장갑", "url": "/kr/category/31", "img": "/media-library/1696248180cotton_new.png" }
  ],
  "stats": [
    { "icon": "flaticon-apartment", "value": "1,200", "title": "숙련된 근로자" },
    { "icon": "flaticon-industry", "value": "12,000", "title": "평방 미터" },
    { "icon": "flaticon-helmet", "value": "1,00,000", "title": "월별 장갑 생산량(다스)" },
    { "icon": "flaticon-happy", "value": "40", "title": "전체 장갑 생산량(백만)" }
  ]
}

with open(os.path.join(DATA_DIR, "jp_data.json"), "w", encoding="utf-8") as f:
  json.dump(jp_data, f, indent=2, ensure_ascii=False)

with open(os.path.join(DATA_DIR, "kr_data.json"), "w", encoding="utf-8") as f:
  json.dump(kr_data, f, indent=2, ensure_ascii=False)

print("Generated jp_data.json and kr_data.json!")
