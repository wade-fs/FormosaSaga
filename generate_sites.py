import os

sites = [
    ("police_dormitory", "警察宿舍", "日治時期留下的木造平房，門前種著一棵老榕樹，是維持地方治安的警員起居之處。"),
    ("rice_shop", "米店", "門口擺著幾個大米缸，空氣中瀰漫著稻米的清香。老闆正拿著木斗在秤米。"),
    ("photo_studio", "照相館", "櫥窗裡陳列著幾張泛黃的黑白照片，牆上掛著「寫真」字樣的招牌，記錄著鎮民的歲月。"),
    ("pharmacy", "藥房", "傳統的漢藥房，一整面牆的木製百子櫃，空氣中充斥著濃郁的當歸與枸杞味。"),
    ("grocery_store", "柑仔店", "堆滿各式雜貨與零食的小店，門口掛著幾串五顏六色的塑膠玩具，是小孩們最愛來的地方。"),
    ("rice_mill", "碾米廠", "轟隆隆的機器聲不絕於耳，白色的粉塵在空中飛舞，這裡是將稻穀加工成白米的重要設施。"),
    ("lumber_yard", "木材行", "堆疊著一根根粗大的檜木與杉木，空氣中瀰漫著濃烈的木頭香氣，不時傳來電鋸的尖銳聲。"),
    ("blacksmith", "打鐵舖", "爐火熊熊燃燒，鐵匠正揮舞著大鐵鎚，發出規律的「鏘鏘」聲，火星四濺。"),
    ("tailor_shop", "裁縫店", "縫紉機發出「噠噠噠」的聲音，牆上掛著各式布料與成衣，裁縫師傅正專心地打版。"),
    ("barbershop", "理髮廳", "門口掛著旋轉的紅藍白三色燈柱，裡面傳來收音機的廣播聲與剪刀的咔嚓聲。"),
    ("watch_shop", "鐘錶行", "玻璃櫃裡擺滿了各式懷錶與手錶，牆上掛著幾個滴答作響的老爺鐘。"),
    ("health_clinic", "衛生所", "白色的建築，散發著淡淡的藥水味，是鎮民看病打針的地方。"),
    ("broadcasting_station", "民雄放送局", "一座高聳的電塔矗立在此，這裡是發送廣播訊號的重要樞紐，周圍戒備森嚴。"),
    ("old_post_office", "舊郵局", "綠色的郵筒站在門外，人們在這裡寄信、匯款，連結著打貓與外面的世界。"),
    ("credit_union", "信用合作社", "鎮民存錢與借貸的地方，算盤的劈啪聲此起彼落。"),
    ("farmers_association", "農會", "農民們聚集在此交流農事、購買肥料，是農業社會的重要組織。"),
    ("library", "圖書館", "寧靜的空間裡擺滿了書架，陽光從窗戶灑進來，有人正安靜地閱讀。"),
    ("public_hall", "公會堂", "寬敞的集會場所，經常舉辦各式演講、表演與鎮民大會。"),
    ("cinema", "戲院", "門口掛著手繪的電影海報，每到傍晚便擠滿了準備看戲的人潮。"),
    ("shaved_ice_shop", "冰果室", "玻璃櫃裡擺著各式新鮮水果，刨冰機發出沙沙的聲音，是年輕人約會的聖地。"),
    ("tea_house", "茶室", "人們圍坐在泡茶桌旁，一邊品茗一邊高談闊論，是消息流通的集散地。"),
    ("tavern", "酒家", "夜裡燈火通明，傳來酒杯交錯與女侍的嬌笑聲，是男人們尋歡作樂的場所。"),
    ("noodle_stand", "麵攤", "一鍋熱騰騰的高湯冒著白煙，老闆正熟練地切著滷味，香味四溢。"),
    ("meat_stall", "肉攤", "攤位上掛著幾塊油亮的豬肉，老闆手起刀落，將肉切成均勻的肉絲。"),
    ("fish_stall", "魚攤", "地上滿是水漬，攤位上擺著各式新鮮的魚蝦，老闆正大聲叫賣。"),
    ("market_alley", "菜市場小巷", "狹窄的巷弄裡擠滿了攤販與買菜的婦女，充滿了生機與活力。"),
    ("ancient_well", "古井", "一口深不見底的古井，井口長滿了青苔，是早期鎮民取水的地方。"),
    ("earth_god_shrine", "土地公廟", "小巧的廟宇，香火鼎盛，庇佑著這方水土的平安。"),
    ("ox_cart_road", "牛車道", "泥土路上留著深深的車轍，不時有農夫趕著牛車緩緩經過。"),
    ("railway_side", "鐵道旁", "鐵軌無限延伸，火車呼嘯而過時，地面會傳來陣陣震動。"),
    ("cemetery", "墓仔埔", "一座座墳墓錯落有致，周圍長滿了雜草，氣氛陰森冷清。"),
    ("bamboo_forest", "竹林", "茂密的竹子遮蔽了陽光，風吹過時，竹葉發出沙沙的聲響。"),
    ("pond", "埤塘", "水面平靜如鏡，偶爾有水鳥掠過，是農田灌溉的水源。"),
    ("farmhouse", "農舍", "紅磚砌成的平房，院子裡曬著菜乾，幾隻雞正在地上啄食。"),
    ("granary", "穀倉", "高大的建築，用來儲存收成的稻穀，防止蟲鼠侵襲。"),
    ("tobacco_barn", "菸樓", "屋頂上有個小氣窗，用來烘烤菸葉，散發著特殊的菸草味。"),
    ("water_wheel", "水車", "巨大的木製水車緩緩轉動，將圳水引入農田，發出規律的嘎吱聲。")
]

base_dir = "mudlib/data/yaml/sites/minxiong"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for site_id, name, desc in sites:
    filepath = os.path.join(base_dir, f"{site_id}.yaml")
    if not os.path.exists(filepath):
        yaml_content = f"""id: {site_id}
name: "{name}"
description: "{desc}"
region: "minxiong"
x: 0
y: 0
z: 0
tier: 4
dimension:
  population: 1
  industry: 1
  culture: 1
  memory: 1
  trade: 1
  cohesion: 1
properties:
  is_outdoor: true
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(yaml_content)
        print(f"Created {filepath}")

