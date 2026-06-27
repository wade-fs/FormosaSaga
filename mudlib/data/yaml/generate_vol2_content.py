#!/usr/bin/env python3
import os
import yaml

BASE_DIR = "/home/wade/src/github/FormosaSaga/mudlib/data/yaml"

def write_yaml(subdir, filename, data):
    path = os.path.join(BASE_DIR, subdir, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)
    print(f"Generated: {subdir}/{filename}")

# --- P23.1 Settlement Updates & Additions ---

kaohsiung_settlement = {
    "id": "kaohsiung",
    "name": "高雄市",
    "tier": 1,
    "admin_level": "市",
    "county": "kaohsiung_city",
    "population": 85,
    "industry": 80,
    "culture": 75,
    "memory": 72,
    "trade": 85,
    "cohesion": 78,
    "specters_active": [],
    "eras_present": ["v1.2", "v1.5", "v2.0", "v3.0", "modern"],
    "industries": ["重工業", "港口貿易", "觀光"],
    "temples": [
        {"name": "高雄三鳳宮", "deity": "哪吒太子"}
    ],
    "sites": [
        "kaohsiung_harbor", "qishan", "gangshan", "fengshan", "qijin", 
        "gangshan_duck_pond", "gangshan_tian_di_hui", "fengshan_fort", "tainan_zhuxingwang"
    ],
    "memory_breakdown": {
        "history_events": 0.35,
        "oral_tradition": 0.30,
        "named_persons": 0.25,
        "sites": 0.28
    }
}
write_yaml("settlements", "kaohsiung.yaml", kaohsiung_settlement)

# Detailed configurations for existing Kaohsiung sites to support audit & description
kaohsiung_harbor_site = {
    "id": "kaohsiung_harbor",
    "settlement": "kaohsiung",
    "canonical_name": "高雄港",
    "is_heritage": True,
    "base_description": "高雄港，舊稱打狗港。港灣水深潮平，是南台灣最重要的貨物進出門戶與貿易樞紐。",
    "travel_arrive_text": "你來到了繁忙的高雄港碼頭，鹹濕的海風吹來，江面帆檣如林。",
    "names": [
        {"era": "qing", "name": "打狗港"},
        {"era": "japanese", "name": "高雄港"},
        {"era": "modern", "name": "高雄港"}
    ],
    "connections": ["qijin", "fengshan", "kinmen_site"]
}
write_yaml("sites/kaohsiung", "kaohsiung_harbor.yaml", kaohsiung_harbor_site)

qijin_site = {
    "id": "qijin",
    "settlement": "kaohsiung",
    "canonical_name": "旗津",
    "is_heritage": True,
    "base_description": "打狗港外的沙洲島嶼，是高雄開發最早的發祥地，岸邊小艇穿梭，漁歌互答。",
    "travel_arrive_text": "你搭乘舢舨船渡海來到旗津，踩在細軟的沙灘上，海浪一波波湧來。",
    "names": [
        {"era": "qing", "name": "旗後街"},
        {"era": "japanese", "name": "旗後"},
        {"era": "modern", "name": "旗津"}
    ],
    "connections": ["kaohsiung_harbor"]
}
write_yaml("sites/kaohsiung", "qijin.yaml", qijin_site)

qishan_site = {
    "id": "qishan",
    "settlement": "kaohsiung",
    "canonical_name": "旗山",
    "is_heritage": False,
    "base_description": "高雄北部的山城，平野延伸入山，氣候宜人，盛產糖與香蕉，是南北物資交換的市集。",
    "travel_arrive_text": "你來到旗山山城，四周層巒疊翠，街市上擺滿了山產與水果。",
    "names": [
        {"era": "qing", "name": "蕃薯寮街"},
        {"era": "japanese", "name": "旗山街"},
        {"era": "modern", "name": "旗山區"}
    ],
    "connections": ["gangshan"]
}
write_yaml("sites/kaohsiung", "qishan.yaml", qishan_site)

gangshan_site = {
    "id": "gangshan",
    "settlement": "kaohsiung",
    "canonical_name": "岡山",
    "is_heritage": False,
    "base_description": "高雄岡山聚落，北接台南，南臨鳳山。這裡平野開闊，清領時期為南北交通要衝，亦是朱一貴事件的爆發起源地。",
    "travel_arrive_text": "你來到了岡山街區，路旁有許多養鴨的池塘與農田。",
    "names": [
        {"era": "qing", "name": "阿公店"},
        {"era": "japanese", "name": "岡山街"},
        {"era": "modern", "name": "岡山區"}
    ],
    "connections": ["qishan", "fengshan", "gangshan_duck_pond", "gangshan_tian_di_hui"]
}
write_yaml("sites/kaohsiung", "gangshan.yaml", gangshan_site)

gangshan_duck_pond = {
    "id": "gangshan_duck_pond",
    "settlement": "kaohsiung",
    "canonical_name": "鴨母王養鴨地",
    "is_heritage": True,
    "base_description": "朱一貴起義前的隱居養鴨處。水塘波光粼粼，鴨群喧鬧。傳說朱一貴能以竹竿指揮鴨群，宛如行軍布陣，因此被稱為『鴨母王』。",
    "travel_arrive_text": "你來到一處寬闊的水塘邊，無數鴨子在水面嬉戲，四周竹林環繞。",
    "names": [
        {"era": "qing", "name": "鴨母寮養鴨塘"},
        {"era": "japanese", "name": "朱一貴舊蹟"},
        {"era": "modern", "name": "鴨母王養鴨地遺址"}
    ],
    "connections": ["gangshan"]
}
write_yaml("sites/kaohsiung", "gangshan_duck_pond.yaml", gangshan_duck_pond)

gangshan_tian_di_hui = {
    "id": "gangshan_tian_di_hui",
    "settlement": "kaohsiung",
    "canonical_name": "天地會秘密集會所",
    "is_heritage": False,
    "hidden": True,
    "base_description": "隱藏在岡山竹林深處的一處簡陋草寮。這是清領中期天地會暗中聯絡、歃血盟誓的秘密據點，香案上供奉著反清復明的神位。",
    "travel_arrive_text": "你穿過密集的刺竹林，眼前出現一座不起眼的草寮，門口掛著暗號燈籠。",
    "names": [
        {"era": "qing", "name": "岡山竹林草寮"},
        {"era": "japanese", "name": "天地會舊匪巢"},
        {"era": "modern", "name": "天地會秘密集會所遺址"}
    ],
    "connections": ["gangshan"]
}
write_yaml("sites/kaohsiung", "gangshan_tian_di_hui.yaml", gangshan_tian_di_hui)

fengshan_site = {
    "id": "fengshan",
    "settlement": "kaohsiung",
    "canonical_name": "鳳山",
    "is_heritage": False,
    "base_description": "高雄鳳山聚落，鄰近下淡水溪（高屏溪）。清領時期設有鳳山縣治，是南部防務與行政的重要中心，城牆周圍環繞著寬闊的護城河。",
    "travel_arrive_text": "你來到了鳳山街市，街道兩旁店鋪林立，遠處可見舊縣城的城牆輪廓。",
    "names": [
        {"era": "qing", "name": "鳳山縣城"},
        {"era": "japanese", "name": "鳳山街"},
        {"era": "modern", "name": "鳳山區"}
    ],
    "connections": ["kaohsiung_harbor", "gangshan", "fengshan_fort"]
}
write_yaml("sites/kaohsiung", "fengshan.yaml", fengshan_site)

fengshan_fort = {
    "id": "fengshan_fort",
    "settlement": "kaohsiung",
    "canonical_name": "鳳山縣城遺址",
    "is_heritage": True,
    "base_description": "清代鳳山縣城的殘存城牆與砲台。這裡曾多次在民變中易手，城磚上殘留著火燒與刀砍的痕跡，見證了政權的交替與戰火的無情。",
    "travel_arrive_text": "你站在斷垣殘壁的舊城牆前，花崗岩壘砌的城基依然堅固，城樓早已不在。",
    "names": [
        {"era": "qing", "name": "鳳山縣新城"},
        {"era": "japanese", "name": "鳳山舊城砦"},
        {"era": "modern", "name": "鳳山縣城遺址"}
    ],
    "connections": ["fengshan"]
}
write_yaml("sites/kaohsiung", "fengshan_fort.yaml", fengshan_fort)

tainan_zhuxingwang = {
    "id": "tainan_zhuxingwang",
    "settlement": "kaohsiung",
    "canonical_name": "府城朱興王行宮",
    "is_heritage": True,
    "base_description": "朱一貴攻佔台南府城後所設的短暫自治首府。他在這裡登基，自稱『義王』，年號『永和』。雖然自治僅維持了短短數月，卻是台灣民變史上的奇蹟。",
    "travel_arrive_text": "你站在這座曾作為行宮的古老院落前，紅磚牆面在陽光下顯得斑駁，昔日的喧囂已化為歷史的塵埃。",
    "names": [
        {"era": "qing", "name": "大興王府（暫設）"},
        {"era": "japanese", "name": "朱一貴偽王府遺址"},
        {"era": "modern", "name": "府城朱興王行宮遺址"}
    ],
    "connections": ["fengshan"]
}
write_yaml("sites/kaohsiung", "tainan_zhuxingwang.yaml", tainan_zhuxingwang)

# Create new Settlements: wufeng, mudan, hengchun
wufeng_settlement = {
    "id": "wufeng",
    "name": "霧峰",
    "tier": 3,
    "admin_level": "鄉",
    "county": "taichung_county",
    "population": 45,
    "industry": 40,
    "culture": 82,
    "memory": 70,
    "trade": 50,
    "cohesion": 85,
    "specters_active": [],
    "eras_present": ["v1.2", "v1.5", "v2.0", "modern"],
    "industries": ["樟腦開採", "文教", "農業"],
    "temples": [
        {"name": "霧峰南天宮", "deity": "媽祖"}
    ],
    "sites": ["wufeng_lin_mansion", "wufeng_academy"],
    "memory_breakdown": {
        "history_events": 0.40,
        "oral_tradition": 0.20,
        "named_persons": 0.30,
        "sites": 0.25
    }
}
write_yaml("settlements", "wufeng.yaml", wufeng_settlement)

wufeng_lin_mansion = {
    "id": "wufeng_lin_mansion",
    "settlement": "wufeng",
    "canonical_name": "霧峰林家宅邸",
    "is_heritage": True,
    "base_description": "台灣最具影響力的地方豪族之一——霧峰林家的宅邸。建築群規模宏大，融閩南、洋式與唐式風格於一體，大花廳戲台雕工精絕，代表了地方豪族的財富與權力。",
    "travel_arrive_text": "你來到宏偉的霧峰林家大宅前，高聳的燕尾脊與精緻的木雕令人驚嘆。",
    "names": [
        {"era": "qing", "name": "阿草埔林家大厝"},
        {"era": "japanese", "name": "霧峰林本源邸"},
        {"era": "modern", "name": "霧峰林家宮保第園區"}
    ],
    "connections": ["wufeng_academy"]
}
write_yaml("sites/wufeng", "wufeng_lin_mansion.yaml", wufeng_lin_mansion)

wufeng_academy = {
    "id": "wufeng_academy",
    "settlement": "wufeng",
    "canonical_name": "萊園私塾",
    "is_heritage": True,
    "base_description": "林家大宅旁的私人花園與私塾。園中步移景異，小橋流水，曾是中部文人志士聚會、吟詩作對以及暗中討論台灣自主命運的文教聖地。",
    "travel_arrive_text": "你漫步在清幽的萊園中，水榭歌台倒映在池水中，傳出低沉的書聲。",
    "names": [
        {"era": "qing", "name": "林氏萊園"},
        {"era": "japanese", "name": "萊園中學私塾"},
        {"era": "modern", "name": "霧峰林家花園（萊園）"}
    ],
    "connections": ["wufeng_lin_mansion"]
}
write_yaml("sites/wufeng", "wufeng_academy.yaml", wufeng_academy)

# mudan
mudan_settlement = {
    "id": "mudan",
    "name": "牡丹",
    "tier": 4,
    "admin_level": "鄉",
    "county": "pingtung_county",
    "population": 25,
    "industry": 15,
    "culture": 90,
    "memory": 88,
    "trade": 20,
    "cohesion": 92,
    "specters_active": [],
    "eras_present": ["v1.5", "v2.0", "modern"],
    "industries": ["狩獵", "山林採集"],
    "temples": [],
    "sites": ["mudan_paiwan_village", "mudan_japanese_landing", "mudan_stone_gate", "checheng_harbor"],
    "memory_breakdown": {
        "history_events": 0.45,
        "oral_tradition": 0.35,
        "named_persons": 0.10,
        "sites": 0.30
    }
}
write_yaml("settlements", "mudan.yaml", mudan_settlement)

mudan_paiwan_village = {
    "id": "mudan_paiwan_village",
    "settlement": "mudan",
    "canonical_name": "牡丹社排灣族部落",
    "is_heritage": True,
    "base_description": "深藏在恆春半島山林中的排灣族部落。以石板屋為主體結構，家屋門前雕刻著百步蛇與祖靈像。這裡的人們世世代代守護著祖靈的獵場與山林規矩。",
    "travel_arrive_text": "你沿著陡峭山路走進部落，四周是一座座古樸的石板屋，空氣中瀰漫著木柴燃燒的煙味。",
    "names": [
        {"era": "qing", "name": "牡丹社外番部落"},
        {"era": "japanese", "name": "モーダン社"},
        {"era": "modern", "name": "牡丹村排灣族部落"}
    ],
    "connections": ["mudan_stone_gate"]
}
write_yaml("sites/mudan", "mudan_paiwan_village.yaml", mudan_paiwan_village)

mudan_japanese_landing = {
    "id": "mudan_japanese_landing",
    "settlement": "mudan",
    "canonical_name": "日軍車城登陸地",
    "is_heritage": True,
    "base_description": "1874年日本遠征軍以保護琉球漁民為藉口登陸的地點。沙灘開闊，海浪拍打著礁石。當年日軍在此紮營，準備深入山林進攻排灣族部落。",
    "travel_arrive_text": "你站在寬闊的沙灘上，海風強勁，遠處可見日軍當年設立臨時港口的軍事防波堤殘跡。",
    "names": [
        {"era": "qing", "name": "車城灣沙灘"},
        {"era": "japanese", "name": "西鄉都督登陸紀念地"},
        {"era": "modern", "name": "日軍車城登陸紀念碑"}
    ],
    "connections": ["checheng_harbor", "mudan_stone_gate"]
}
write_yaml("sites/mudan", "mudan_japanese_landing.yaml", mudan_japanese_landing)

mudan_stone_gate = {
    "id": "mudan_stone_gate",
    "settlement": "mudan",
    "canonical_name": "石門古戰場",
    "is_heritage": True,
    "base_description": "兩側高山夾峙的險要峽谷，中間僅有一條溪流穿過，是防守的天然屏障。1874年，排灣族戰士在此伏擊日軍，爆發了慘烈的石門之役。",
    "travel_arrive_text": "你站在巍峨的石門峽谷口，兩側峭壁如削，溪水在谷底奔流，隱約能感受到當年的肅殺氣氛。",
    "names": [
        {"era": "qing", "name": "石門峽口"},
        {"era": "japanese", "name": "石門戰跡"},
        {"era": "modern", "name": "石門古戰場遺址"}
    ],
    "connections": ["mudan_paiwan_village", "mudan_japanese_landing"]
}
write_yaml("sites/mudan", "mudan_stone_gate.yaml", mudan_stone_gate)

checheng_harbor = {
    "id": "checheng_harbor",
    "settlement": "mudan",
    "canonical_name": "射寮港",
    "is_heritage": False,
    "base_description": "位於恆春半島西北側的古老港口，是官船與商船往來的重要靠泊點。清廷欽差大臣沈葆楨奉命來台查辦防務時，便是在此港口上岸登陸。",
    "travel_arrive_text": "你來到射寮港碼頭，幾艘小漁船在波浪中搖晃，岸邊立著古老的石碑。",
    "names": [
        {"era": "qing", "name": "射寮港渡頭"},
        {"era": "japanese", "name": "射寮港"},
        {"era": "modern", "name": "射寮漁港"}
    ],
    "connections": ["mudan_japanese_landing"]
}
write_yaml("sites/mudan", "checheng_harbor.yaml", checheng_harbor)

# hengchun
hengchun_settlement = {
    "id": "hengchun",
    "name": "恆春",
    "tier": 3,
    "admin_level": "鎮",
    "county": "pingtung_county",
    "population": 38,
    "industry": 20,
    "culture": 78,
    "memory": 82,
    "trade": 45,
    "cohesion": 80,
    "specters_active": [],
    "eras_present": ["v1.5", "v2.0", "modern"],
    "industries": ["農業", "邊防貿易"],
    "temples": [
        {"name": "恆春廣寧宮", "deity": "三山國王"}
    ],
    "sites": ["hengchun_old_town", "hengchun_south_gate"],
    "memory_breakdown": {
        "history_events": 0.40,
        "oral_tradition": 0.30,
        "named_persons": 0.15,
        "sites": 0.25
    }
}
write_yaml("settlements", "hengchun.yaml", hengchun_settlement)

hengchun_old_town = {
    "id": "hengchun_old_town",
    "settlement": "hengchun",
    "canonical_name": "恆春古城",
    "is_heritage": True,
    "base_description": "牡丹社事件後，清廷深感海防脆弱，由沈葆楨規劃興建的防禦城池。城牆採用當地硓𡏆石與磚石混建，是台灣目前保留最完整的清代城池。",
    "travel_arrive_text": "你漫步在保存完好的古老城牆上，灰黑色的磚石散發著歲月的滄桑，城門洞深邃而堅固。",
    "names": [
        {"era": "qing", "name": "恆春縣城"},
        {"era": "japanese", "name": "恆春街城壁"},
        {"era": "modern", "name": "恆春古城牆"}
    ],
    "connections": ["hengchun_south_gate"]
}
write_yaml("sites/hengchun", "hengchun_old_town.yaml", hengchun_old_town)

hengchun_south_gate = {
    "id": "hengchun_south_gate",
    "settlement": "hengchun",
    "canonical_name": "恆春南門",
    "is_heritage": True,
    "base_description": "恆春古城的南城門（明都門）。磚造的城門結構宏偉，城門洞上方嵌有花崗岩門額，這裡曾是守衛城池、面向南海的前哨要塞。",
    "travel_arrive_text": "你站在南門圓環旁，城門洞兩側斑駁的紅色漆面在陽光下十分醒目。",
    "names": [
        {"era": "qing", "name": "恆春縣城南門（明都門）"},
        {"era": "japanese", "name": "南門圓環"},
        {"era": "modern", "name": "恆春古城南門"}
    ],
    "connections": ["hengchun_old_town"]
}
write_yaml("sites/hengchun", "hengchun_south_gate.yaml", hengchun_south_gate)

# Update taipei.yaml to add dadaocheng sites
taipei_settlement = {
    "id": "taipei",
    "name": "台北市",
    "tier": 1,
    "admin_level": "市",
    "county": "taipei_city",
    "population": 95,
    "industry": 85,
    "culture": 80,
    "memory": 75,
    "trade": 90,
    "cohesion": 70,
    "specters_active": [],
    "eras_present": ["v1.5", "v2.0", "v3.0", "modern"],
    "industries": ["金融", "商業", "茶葉出口"],
    "temples": [
        {"name": "大稻埕霞海城隍廟", "deity": "城隍爺"}
    ],
    "sites": ["dadaocheng_tea_warehouse", "dadaocheng_yanping_pier"],
    "memory_breakdown": {
        "history_events": 0.38,
        "oral_tradition": 0.22,
        "named_persons": 0.28,
        "sites": 0.28
    }
}
write_yaml("settlements", "taipei.yaml", taipei_settlement)

dadaocheng_tea_warehouse = {
    "id": "dadaocheng_tea_warehouse",
    "settlement": "taipei",
    "canonical_name": "大稻埕茶行倉庫",
    "is_heritage": True,
    "base_description": "大稻埕鼎盛時期的茶葉精製與存放倉庫。空氣中瀰漫著焙茶的濃郁炭香，紅磚與巴洛克立面的街屋見證了洋行洋商買辦茶葉的輝煌時代。",
    "travel_arrive_text": "你走進幽深的老茶行，一排排巨大的竹編茶籠整齊排列，焙茶灶正冒著熱氣。",
    "names": [
        {"era": "qing", "name": "大稻埕茶棧"},
        {"era": "japanese", "name": "大稻埕茶行倉庫"},
        {"era": "modern", "name": "大稻埕茶行展示館"}
    ],
    "connections": ["dadaocheng_yanping_pier"]
}
write_yaml("sites/taipei", "dadaocheng_tea_warehouse.yaml", dadaocheng_tea_warehouse)

dadaocheng_yanping_pier = {
    "id": "dadaocheng_yanping_pier",
    "settlement": "taipei",
    "canonical_name": "延平碼頭",
    "is_heritage": True,
    "base_description": "淡水河畔的繁忙碼頭，是清末大稻埕烏龍茶與樟腦出口海外的主要裝運港。帆船與戎克船靠滿江邊，碼頭工人川流不息。",
    "travel_arrive_text": "你來到淡水河畔，江水滔滔，昔日木船桅杆如林的景象已換成現代的河濱綠地與遊艇。",
    "names": [
        {"era": "qing", "name": "大稻埕河埠頭"},
        {"era": "japanese", "name": "大稻埕碼頭"},
        {"era": "modern", "name": "大稻埕碼頭（延平河濱公園）"}
    ],
    "connections": ["dadaocheng_tea_warehouse"]
}
write_yaml("sites/taipei", "dadaocheng_yanping_pier.yaml", dadaocheng_yanping_pier)


# Update yunlin.yaml and its sites
yunlin_settlement = {
    "id": "yunlin",
    "name": "雲林縣",
    "tier": 3,
    "admin_level": "縣",
    "county": "yunlin_county",
    "population": 52,
    "industry": 35,
    "culture": 70,
    "memory": 68,
    "trade": 45,
    "cohesion": 75,
    "specters_active": [],
    "eras_present": ["v1.0", "v1.2", "v1.5", "v2.0", "modern"],
    "industries": ["農業", "水利"],
    "temples": [
        {"name": "斗六真一寺", "deity": "觀音佛祖"}
    ],
    "sites": ["yunlin_douliu_street", "yunlin_hakka_village", "yunlin_irrigation_field"],
    "memory_breakdown": {
        "history_events": 0.30,
        "oral_tradition": 0.35,
        "named_persons": 0.15,
        "sites": 0.20
    }
}
write_yaml("settlements", "yunlin.yaml", yunlin_settlement)

yunlin_douliu_street = {
    "id": "yunlin_douliu_street",
    "settlement": "yunlin",
    "canonical_name": "斗六老街",
    "is_heritage": False,
    "base_description": "雲林斗六的舊街市。街道兩側散佈著古老的木構與紅磚店鋪，是清代斗六門的行政與商業中心，漳泉移民在此交錯雜居。",
    "travel_arrive_text": "你來到斗六老街口，四周十分嘈雜，古老屋簷下的陰影裡有許多挑夫在歇息。",
    "names": [
        {"era": "qing", "name": "斗六門街"},
        {"era": "japanese", "name": "斗六街"},
        {"era": "modern", "name": "斗六老街"}
    ],
    "connections": ["yunlin_hakka_village", "yunlin_irrigation_field"]
}
write_yaml("sites/yunlin", "yunlin_douliu_street.yaml", yunlin_douliu_street)

yunlin_hakka_village = {
    "id": "yunlin_hakka_village",
    "settlement": "yunlin",
    "canonical_name": "雲林客家庄",
    "is_heritage": False,
    "base_description": "斗六外圍的客家聚落，屋厝相連，防禦性極強。在漳泉械鬥頻繁的時代，這裡是客家移民團結共抗強鄰的堡壘。",
    "travel_arrive_text": "你走進客家庄，四周的房舍多為土角厝與防衛性竹籬，村民說著流利的客家客語。",
    "names": [
        {"era": "qing", "name": "斗六門客家庄"},
        {"era": "japanese", "name": "斗六外圍客家聚落"},
        {"era": "modern", "name": "雲林客家村落"}
    ],
    "connections": ["yunlin_douliu_street"]
}
write_yaml("sites/yunlin", "yunlin_hakka_village.yaml", yunlin_hakka_village)

yunlin_irrigation_field = {
    "id": "yunlin_irrigation_field",
    "settlement": "yunlin",
    "canonical_name": "漳泉水圳爭奪地",
    "is_heritage": False,
    "base_description": "清代漳州與泉州移民為爭奪灌溉水源而多次爆發械鬥的農田水圳旁。兩側水閘板斑駁陸離，泥地裡曾掩埋了無數械鬥死難者的骸骨。",
    "travel_arrive_text": "你站在寬闊的灌溉水圳旁，圳水湍急，兩旁是無垠的稻田，水閘口殘留著幾座無名小墳。",
    "names": [
        {"era": "qing", "name": "漳泉爭水大圳"},
        {"era": "japanese", "name": "斗六水圳"},
        {"era": "modern", "name": "漳泉水圳爭奪地"}
    ],
    "connections": ["yunlin_douliu_street"]
}
write_yaml("sites/yunlin", "yunlin_irrigation_field.yaml", yunlin_irrigation_field)


# Update miaoli.yaml and its sites
miaoli_settlement = {
    "id": "miaoli",
    "name": "苗栗縣",
    "tier": 3,
    "admin_level": "縣",
    "county": "miaoli_county",
    "population": 48,
    "industry": 30,
    "culture": 80,
    "memory": 72,
    "trade": 40,
    "cohesion": 88,
    "specters_active": [],
    "eras_present": ["v1.5", "v2.0", "modern"],
    "industries": ["農業", "鐵路修建", "樟腦"],
    "temples": [
        {"name": "苗栗玉清宮", "deity": "關聖帝君"}
    ],
    "sites": ["miaoli_old_railway", "miaoli_hakka_yi_min", "dakeng_aboriginal_village"],
    "memory_breakdown": {
        "history_events": 0.32,
        "oral_tradition": 0.38,
        "named_persons": 0.15,
        "sites": 0.15
    }
}
write_yaml("settlements", "miaoli.yaml", miaoli_settlement)

miaoli_old_railway = {
    "id": "miaoli_old_railway",
    "settlement": "miaoli",
    "canonical_name": "苗栗舊鐵路遺址",
    "is_heritage": True,
    "base_description": "清代首任巡撫劉銘傳規劃建設的台灣鐵路苗栗段。殘存的枕木被雜草覆蓋，生鏽的鐵軌延伸向遠方，見證了台灣近代化鐵路史的開端。",
    "travel_arrive_text": "你站在荒廢的舊鐵軌旁，兩旁高山連綿，古老的隧道路口已被青苔遮蔽。",
    "names": [
        {"era": "qing", "name": "劉銘傳鐵路段（苗栗）"},
        {"era": "japanese", "name": "苗栗縱貫線舊軌"},
        {"era": "modern", "name": "苗栗舊鐵路遺址"}
    ],
    "connections": ["miaoli_hakka_yi_min", "dakeng_aboriginal_village"]
}
write_yaml("sites/miaoli", "miaoli_old_railway.yaml", miaoli_old_railway)

miaoli_hakka_yi_min = {
    "id": "miaoli_hakka_yi_min",
    "settlement": "miaoli",
    "canonical_name": "苗栗義民廟",
    "is_heritage": True,
    "base_description": "苗栗當地的客家義民廟。廟宇莊嚴古樸，供奉著在林爽文事件等多次民變中，為了保鄉衛土而英勇犧牲的客家義民軍神位。",
    "travel_arrive_text": "你走進義民廟，香爐裡香煙繚繞，偏殿高懸著大清朝廷賞賜的『褒忠』匾額。",
    "names": [
        {"era": "qing", "name": "褒忠義民廟"},
        {"era": "japanese", "name": "苗栗義民廟"},
        {"era": "modern", "name": "苗栗義民廟"}
    ],
    "connections": ["miaoli_old_railway"]
}
write_yaml("sites/miaoli", "miaoli_hakka_yi_min.yaml", miaoli_hakka_yi_min)

dakeng_aboriginal_village = {
    "id": "dakeng_aboriginal_village",
    "settlement": "miaoli",
    "canonical_name": "大嵙崁原住民部落",
    "is_heritage": False,
    "base_description": "苗栗深山處的原住民泰雅族部落。四周群山環抱，古樹參天。在清領晚期『開山撫番』政策推動下，這裡曾是原住民抵禦清軍與樟腦工人的最前線。",
    "travel_arrive_text": "你越過深邃的峽谷吊橋，走進長滿山櫻花的部落，幾座古老的高腳茅草屋隱現林間。",
    "names": [
        {"era": "qing", "name": "大嵙崁生番部落"},
        {"era": "japanese", "name": "大嵙崁社"},
        {"era": "modern", "name": "大嵙崁原住民部落"}
    ],
    "connections": ["miaoli_old_railway"]
}
write_yaml("sites/miaoli", "dakeng_aboriginal_village.yaml", dakeng_aboriginal_village)


# --- P23.2 Incidents ---

incidents = [
    {
        "incident_id": "ep001_zhu_yigui",
        "name": "朱一貴事件",
        "description": "康熙六十（1721）年，鴨母王朱一貴率眾起義，攻陷鳳山縣城並直取台南府城。他在府城短暫建國自治，這是清領時期台灣第一次大規模民變。\n你將深入岡山與鳳山，還原起義軍的短暫自治奇蹟與慘烈尾聲。",
        "truth": "朱一貴事件是台灣移民社會積怨爆發的展現。朱一貴與杜君英雖聯合攻佔府城，但隨後因為閩粵籍貫的利益衝突而分裂，導致清軍得以迅速反攻平叛。事件後，清軍在南台灣加強防務，並激化了後續的閩粵分類械鬥。",
        "era_active": "v1.2",
        "settlement": "kaohsiung",
        "scope": ["gangshan", "fengshan", "tainan"],
        "clues": [
            {"clue_id": "duck_king_bamboo", "name": "鴨母王指揮鴨群的神異竹竿", "source_type": "npc_ask", "source_id": "npc:NPC_zheng_zai", "ask_topic": "鴨母王"},
            {"clue_id": "palace_spring_relic", "name": "行宮內起義軍短暫登基的斷柱殘片", "source_type": "site_look", "source_id": "site:tainan_zhuxingwang"},
            {"clue_id": "magistrate_escape_doc", "name": "鳳山知縣倉皇逃命時遺失的公文", "source_type": "npc_ask", "source_id": "npc:NPC_du_junying", "ask_topic": "知縣公文"}
        ],
        "completion_reward": {"exp": 1500, "faction": "taiwan_folk_memory", "reputation": 100}
    },
    {
        "incident_id": "ep002_lin_shuangwen",
        "name": "林爽文事件",
        "description": "乾隆五十一（1786）年，天地會領袖林爽文在彰化大里杙起義，攻佔彰化縣城與大半個台灣。這是清領歷史上規模最大的民變，波及全台，圍城數載。\n你將跨越彰化與雲林，尋找天地會的起義暗流與慘烈圍城印記。",
        "truth": "林爽文事件動搖了大清國本，清廷甚至派遣福康安率精銳大軍來台鎮壓。事件爆發時，各地方宗族為了自衛而選擇與官府合作或與義軍對立，催生了大量的『義民』信仰，對台灣中部社會的族群防衛結構產生了深遠影響。",
        "era_active": "v1.2",
        "settlement": "changhua_city",
        "scope": ["changhua_city", "yunlin", "wufeng"],
        "clues": [
            {"clue_id": "tian_di_hui_oath", "name": "竹林草寮深處的歃血盟誓血書", "source_type": "site_look", "source_id": "site:gangshan_tian_di_hui"},
            {"clue_id": "fort_siege_record", "name": "彰化城內百姓在圍城四年中的避難日記", "source_type": "npc_ask", "source_id": "npc:NPC_lin_shuangwen", "ask_topic": "彰化圍城"},
            {"clue_id": "yi_min_oxcart_bones", "name": "載運義民屍骨的牛車輪軸殘件", "source_type": "npc_ask", "source_id": "npc:NPC_lin_chaodong", "ask_topic": "義民軍"}
        ],
        "completion_reward": {"exp": 1800, "faction": "taiwan_historical_truth", "reputation": 120}
    },
    {
        "incident_id": "ep003_dai_chaochun",
        "name": "戴潮春事件",
        "description": "同治元（1862）年，戴潮春利用八卦會起義，佔領彰化並實行四年長期的圍城自治。這是地方豪族、會黨與清廷官府三方角力的極致。\n你將在彰化與台中，調查宗族門閥的博弈與百姓對平靜的渴望。",
        "truth": "戴潮春事件的本質是地方武裝力量（如八卦會）與地方豪族（如霧峰林家）之間的博弈。戴潮春聯絡中台灣各大地主，與清廷對峙長達四年，最終因霧峰林家協助清軍而宣告失敗。此役奠定了霧峰林家此後在台灣中部無可匹敵的霸主地位。",
        "era_active": "v1.5",
        "settlement": "changhua_city",
        "scope": ["changhua_city", "wufeng", "yunlin"],
        "clues": [
            {"clue_id": "bagua_seal_charter", "name": "八卦會授予各庄紳商的起義蓋印規約", "source_type": "npc_ask", "source_id": "npc:NPC_dai_chaochun", "ask_topic": "八卦會"},
            {"clue_id": "lin_mansion_letter", "name": "霧峰林家暗中聯絡清軍圍剿戴潮春的密信", "source_type": "site_look", "source_id": "site:wufeng_lin_mansion"},
            {"clue_id": "siege_starve_diary", "name": "圍城四年中城內米價飛漲的商家帳簿", "source_type": "npc_ask", "source_id": "npc:NPC_lao_zhou", "ask_topic": "四年圍城"}
        ],
        "completion_reward": {"exp": 1600, "faction": "taiwan_folk_memory", "reputation": 100}
    },
    {
        "incident_id": "ep004_mudan_incident",
        "name": "牡丹社事件",
        "description": "1874年，日本以琉球漁民遇難為由派兵侵台。排灣族戰士在石門與日軍決一死戰。這是台灣走向近代國際舞台與清廷政策轉向的關鍵事件。\n你將深入恆春半島，重現帝國試探的足跡與排灣族祖靈的怒吼。",
        "truth": "牡丹社事件是日本帝國海軍的首次海外軍事擴張，也是清廷由『消極治台』轉為『積極開山撫番』的轉折點。排灣族頭目阿祿古斯率眾奮勇抗擊日軍，雖傷亡慘重，但其英勇迫使日軍退兵。事件後沈葆楨來台建古城、增設防務，台灣的命運被徹底改寫。",
        "era_active": "v1.5",
        "settlement": "mudan",
        "scope": ["mudan", "hengchun"],
        "clues": [
            {"clue_id": "arugus_skull_spear", "name": "牡丹社頭目阿祿古斯佩戴的祖靈長矛", "source_type": "npc_ask", "source_id": "npc:NPC_arugus", "ask_topic": "祖靈規矩"},
            {"clue_id": "japanese_bullet_casing", "name": "石門古戰場泥土下出土的日軍洋槍彈殼", "source_type": "site_look", "source_id": "site:mudan_stone_gate"},
            {"clue_id": "shen_baozhen_memorial", "name": "沈葆楨巡視射寮港後撰寫的開山撫番奏摺", "source_type": "npc_ask", "source_id": "npc:NPC_shen_baozhen", "ask_topic": "海防奏摺"}
        ],
        "completion_reward": {"exp": 1700, "faction": "taiwan_historical_truth", "reputation": 110}
    },
    {
        "incident_id": "ep005_taiwan_province",
        "name": "台灣建省",
        "description": "1885年，台灣正式建省，首任巡撫劉銘傳推行全面近代化改革：興建縱貫鐵路、開辦郵政、架設電報、開山撫番。\n你將追隨劉銘傳與修築鐵路的苦力，見證現代文明在台灣土地上的誕生與代價。",
        "truth": "台灣建省與劉銘傳改革使台灣成為大清帝國最先進的省份。然而，近代化背後有著無數鐵路苦力的汗水與代價，同時伴隨著激烈殘酷的『開山撫番』，給山區原住民部落帶來了毀滅性的打擊，展現了現代化發展的光影兩面。",
        "era_active": "v1.5",
        "settlement": "taipei",
        "scope": ["taipei", "miaoli", "wufeng"],
        "clues": [
            {"clue_id": "railway_spike_rust", "name": "舊鐵道旁生鏽的鐵軌枕木鋼釘", "source_type": "site_look", "source_id": "site:miaoli_old_railway"},
            {"clue_id": "modern_telegraph_wire", "name": "劉銘傳時代自台北大稻埕架設的電報線殘段", "source_type": "npc_ask", "source_id": "npc:NPC_liu_mingchuan", "ask_topic": "鐵道建設"},
            {"clue_id": "aboriginal_loss_chief", "name": "原住民部落因樟腦林開墾而被燒毀的耕地地契", "source_type": "npc_ask", "source_id": "npc:NPC_lao_zhou", "ask_topic": "撫番代價"}
        ],
        "completion_reward": {"exp": 1600, "faction": "taiwan_cultural_memory", "reputation": 100}
    }
]

for inc in incidents:
    write_yaml("incidents", f"{inc['incident_id']}.yaml", inc)


# --- P23.3 Routes ---

routes = [
    {
        "id": "route_tainan_kaohsiung",
        "nodes": ["tainan", "gangshan"],
        "distance_km": 35,
        "travel_time": {"walk": "7h", "horse": "2.5h", "modern": "40m", "railway": "35m"},
        "eras": ["v1.2", "v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_kaohsiung_pingtung",
        "nodes": ["gangshan", "hengchun"],
        "distance_km": 90,
        "travel_time": {"walk": "18h", "horse": "6h", "modern": "1.5h", "railway": "1.2h"},
        "eras": ["v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_lukang_changhua",
        "nodes": ["lukang", "changhua_city"],
        "distance_km": 15,
        "travel_time": {"walk": "3h", "horse": "1h", "modern": "20m", "railway": "18m"},
        "eras": ["v1.0", "v1.2", "v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_changhua_taichung",
        "nodes": ["changhua_city", "wufeng"],
        "distance_km": 20,
        "travel_time": {"walk": "4h", "horse": "1.5h", "modern": "25m", "railway": "20m"},
        "eras": ["v1.2", "v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_changhua_yunlin",
        "nodes": ["changhua_city", "yunlin"],
        "distance_km": 42,
        "travel_time": {"walk": "9h", "horse": "3.5h", "modern": "45m", "railway": "40m"},
        "eras": ["v1.0", "v1.2", "v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_taichung_miaoli",
        "nodes": ["wufeng", "miaoli"],
        "distance_km": 45,
        "travel_time": {"walk": "10h", "horse": "4h", "modern": "50m", "railway": "45m"},
        "eras": ["v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_miaoli_taipei",
        "nodes": ["miaoli", "taipei"],
        "distance_km": 110,
        "travel_time": {"walk": "22h", "horse": "8h", "modern": "1.8h", "railway": "1.5h"},
        "eras": ["v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    },
    {
        "id": "route_yunlin_chiayi",
        "nodes": ["yunlin", "chiayi_city"],
        "distance_km": 30,
        "travel_time": {"walk": "6h", "horse": "2h", "modern": "35m", "railway": "30m"},
        "eras": ["v1.0", "v1.2", "v1.5", "v2.0", "v2.1", "v3.0", "modern"]
    }
]

for rt in routes:
    write_yaml("routes/settlements", f"{rt['id']}.yaml", rt)


# --- P23.4 NPCs (大寫前綴 NPC_) ---

npcs = [
    {
        "id": "NPC_zhu_yigui",
        "name": {"zh-TW": "朱一貴"},
        "settlement": "kaohsiung",
        "home_site": "gangshan_duck_pond",
        "role": "rebel_leader",
        "hint": {"zh-TW": "身著粗布衣，手拿竹竿，眼神堅毅。他擅長養鴨，傳說能像帶兵一樣指揮鴨群。"},
        "responses": {
            "起義": {"zh-TW": "官逼民反！清廷官吏橫徵暴斂，台灣百姓苦不堪言。我等在岡山誓師，要為天下百姓討回公道！"},
            "鴨母王": {"zh-TW": "呵呵，不過是些聽話的鴨子罷了。但人若能像鴨群般團結一心，縱有清軍鐵騎，又何懼之有？"},
            "自治": {"zh-TW": "我們佔領府城後，尊奉朱明，減免苛稅。百姓要的是安居樂業，不是滿清的公文 and 鞭子！"}
        }
    },
    {
        "id": "NPC_du_junying",
        "name": {"zh-TW": "杜君英"},
        "settlement": "kaohsiung",
        "home_site": "gangshan_tian_di_hui",
        "role": "rebel_leader",
        "hint": {"zh-TW": "客家義軍領袖，身材高大，面容冷峻，腰間佩戴著客家鐵刀。"},
        "responses": {
            "朱一貴": {"zh-TW": "阿貴是有膽識，但府城那些閩南紳商排擠我們客家兄弟！天下是大家一起打的，憑什麼好處都歸他們？"},
            "裂痕": {"zh-TW": "閩粵本是一家，但分贓不公，兄弟鬩牆，這場大事怕是走不遠了……"},
            "知縣公文": {"zh-TW": "鳳山知縣跑得比兔子還快，他的大印和公文被我們截獲了。公文上全是催繳稅糧的命令，真是不把百姓當人。"}
        }
    },
    {
        "id": "NPC_zheng_zai",
        "name": {"zh-TW": "鄭仔"},
        "settlement": "kaohsiung",
        "home_site": "gangshan_duck_pond",
        "role": "farmer",
        "hint": {"zh-TW": "朱一貴的隔壁農夫鄰居，皮膚曬得黝黑，戴著斗笠，說起話來滔滔不絕。"},
        "responses": {
            "朱一貴": {"zh-TW": "阿貴以前天天在池塘邊趕鴨子，嘴裡唸唸有詞。他那根長竹竿一揮，幾百隻鴨子就排成整齊的方陣，神氣得很！"},
            "鴨母王": {"zh-TW": "大家都叫他鴨母王。他登基那天，整個岡山的兄弟都去放鞭炮慶祝，沒想到一個養鴨的也能做皇帝。"}
        }
    },
    {
        "id": "NPC_lin_shuangwen",
        "name": {"zh-TW": "林爽文"},
        "settlement": "changhua_city",
        "home_site": "changhua_city_site",
        "role": "rebel_leader",
        "hint": {"zh-TW": "身披布甲，腰懸雙刀，神色嚴肅而剛毅的天地會起義領袖。"},
        "responses": {
            "天地會": {"zh-TW": "天地會盟兄弟，反清復明，同生共死！官府越是追捕，我們的火種就燒得越旺！"},
            "彰化圍城": {"zh-TW": "半線古城是防線關鍵。我們幾度攻城，清軍死守。這城牆是用百姓的血鋪出來的，一旦城破，絕不饒恕官兵！"}
        }
    },
    {
        "id": "NPC_zhuang_datian",
        "name": {"zh-TW": "莊大田"},
        "settlement": "kaohsiung",
        "home_site": "fengshan_fort",
        "role": "rebel_leader",
        "hint": {"zh-TW": "南路起義軍領袖，性格火爆，滿臉鬍鬚，手持一桿長柄大刀。"},
        "responses": {
            "林爽文": {"zh-TW": "林爽文在北路起兵，我在南路響應！南北夾擊，要讓清軍在台灣無處可逃！"},
            "南路防線": {"zh-TW": "鳳山縣城雖然破了，但官兵的大船還在海口轉悠。兄弟們必須守住這幾座砲台，不能讓清廷援軍輕易登陸！"}
        }
    },
    {
        "id": "NPC_dai_chaochun",
        "name": {"zh-TW": "戴潮春"},
        "settlement": "changhua_city",
        "home_site": "changhua_confucian_temple",
        "role": "rebel_leader",
        "hint": {"zh-TW": "手搖摺扇，面容儒雅，但眼神中透著深沉心機的八卦會首領。"},
        "responses": {
            "八卦會": {"zh-TW": "彰化平原各庄結拜八卦會，是為了在械鬥與官府剝削下求生。我們以宗族為骨幹，官府也奈何不得。"},
            "四年圍城": {"zh-TW": "這座半線城，我們圍了四年。城裡的米糧雖然斷了，但只要各庄源源不斷支持我們，我們就能一直撐下去。"}
        }
    },
    {
        "id": "NPC_arugus",
        "name": {"zh-TW": "阿祿古斯"},
        "settlement": "mudan",
        "home_site": "mudan_paiwan_village",
        "role": "tribal_chief",
        "hint": {"zh-TW": "牡丹社排灣族總頭目。滿頭白髮，神情威嚴，身上披著華麗的傳統排灣族羽飾披風。"},
        "responses": {
            "日軍": {"zh-TW": "那些穿藍衣服的矮子帶著洋槍闖進我們的獵場。這裡的一草一木都是祖靈賜予的，除非我們戰死，否則外人休想奪走！"},
            "祖靈規矩": {"zh-TW": "進入牡丹社的山林，就必須遵循祖靈的規矩。琉球人遇難，我們供水給糧，但他們不尊重我們的禁忌，這才是災禍的開始。"},
            "石門": {"zh-TW": "石門是我們獵人守護部落的鐵閘。在那裡，我們的箭雨會讓入侵者知道，排灣族的山嶺不可侵犯！"}
        }
    },
    {
        "id": "NPC_jp_interpreter",
        "name": {"zh-TW": "田中翻譯官"},
        "settlement": "mudan",
        "home_site": "mudan_japanese_landing",
        "role": "interpreter",
        "hint": {"zh-TW": "身穿日軍制服的年輕翻譯官，戴著眼鏡，神色緊張，手中拿著一本沾了泥土的記事本。"},
        "responses": {
            "登陸": {"zh-TW": "海浪太大了，我們的士兵很多人都在吐。車城的居民看我們的眼神充滿了敵意，這片山林實在太潮濕、太恐怖了。"},
            "番社": {"zh-TW": "西鄉都督命令我們查明牡丹社的具體位置。但是山裡的瘴氣和那些神出鬼沒的獵人，讓我們的偵察隊傷亡慘重。"},
            "翻譯": {"zh-TW": "我奉命與車城和番社溝通，但雙方的語言隔閡太深。這場戰爭，本來可以避免的……"}
        }
    },
    {
        "id": "NPC_shen_baozhen",
        "name": {"zh-TW": "沈葆楨"},
        "settlement": "mudan",
        "home_site": "checheng_harbor",
        "role": "magistrate",
        "hint": {"zh-TW": "大清欽差大臣，身穿一品官服，神情冷峻而精明，手撫長鬚，顯得憂國憂民。"},
        "responses": {
            "牡丹社": {"zh-TW": "日軍以琉球人為藉口侵我疆土，實乃窺視我台灣防務。本大臣奉命來台，當內撫番社、外禦強敵。"},
            "開山撫番": {"zh-TW": "台灣後山歷來被視為版圖之外，此乃大謬！當開闢道路、安撫番社、設官治理，方能斷絕外人窺覬之心。"},
            "海防奏摺": {"zh-TW": "本大臣已上奏朝廷，請求在恆春建城防守，並興建砲台。台灣乃東南門戶，海防不可一日鬆懈！"}
        }
    },
    {
        "id": "NPC_liu_mingchuan",
        "name": {"zh-TW": "劉銘傳"},
        "settlement": "taipei",
        "home_site": "dadaocheng_tea_warehouse",
        "role": "magistrate",
        "hint": {"zh-TW": "首任台灣巡撫，身穿官服，眼神銳利如鷹，行事雷厲風行，渾身散發著改革者的強大氣場。"},
        "responses": {
            "建省": {"zh-TW": "台灣建省乃是萬世之基！我們要用鐵路、電報、洋槍把這片土地武裝起來，不能再讓外強輕易染指！"},
            "鐵道建設": {"zh-TW": "火車一響，黃金萬兩！從基隆到新竹的鐵路必須按期完工。那些守舊鄉紳說動了風水，簡直是愚昧至極！"},
            "樟腦": {"zh-TW": "大稻埕的茶葉與山區的樟腦是建省的財源。但開墾樟腦林勢必與深山生番起衝突，朝廷必須雙管齊下，撫剿並重。"}
        }
    },
    {
        "id": "NPC_lao_zhou",
        "name": {"zh-TW": "苦力老周"},
        "settlement": "miaoli",
        "home_site": "miaoli_old_railway",
        "role": "laborer",
        "hint": {"zh-TW": "修築鐵路的苦力老兵，皮膚被曬得像黑炭，雙手長滿了厚厚的老繭，肩膀上有被扁擔壓出的血印。"},
        "responses": {
            "鐵路": {"zh-TW": "巡撫老爺說這叫火車鐵軌。我們天天用鐵鎚砸石頭、鋪枕木。不少兄弟沒死在戰場上，倒死在工地的熱病和落石底下了。"},
            "撫番代價": {"zh-TW": "山裡的泰雅族人反抗得厲害，因為我們砍了他們的樟腦樹。官兵天天跟他們打仗，聽說燒了好幾個部落，作孽啊……"},
            "汗水": {"zh-TW": "這鋼軌底下的每一根枕木，都浸透了我們苦力的汗水。只求完工後能拿到工錢回家娶媳婦。"}
        }
    },
    {
        "id": "NPC_lin_chaodong",
        "name": {"zh-TW": "林朝棟"},
        "settlement": "wufeng",
        "home_site": "wufeng_lin_mansion",
        "role": "clan_leader",
        "hint": {"zh-TW": "霧峰林家當主，文質彬彬但英氣勃勃，腰懸長劍，手按家訓文書。"},
        "responses": {
            "霧峰林家": {"zh-TW": "我們林家從阿草埔起家，篳路藍縷。在林爽文與戴潮春兩次大亂中，我們林家精忠報國，協助清軍平叛，方有今日之基業。"},
            "義民軍": {"zh-TW": "亂世之中，朝廷無力保境，唯有地方鄉紳組織義勇，方能保宗族性命。南投與彰化的義民廟，便是歷史的明證。"},
            "樟腦專賣": {"zh-TW": "林家得巡撫委託，掌管中部樟腦與山防。這不僅是林家的財源，更是守護台灣中部防線的重大責任。"}
        }
    },
    {
        "id": "NPC_chen_zai",
        "name": {"zh-TW": "農民陳仔"},
        "settlement": "yunlin",
        "home_site": "yunlin_irrigation_field",
        "role": "farmer",
        "hint": {"zh-TW": "漳州籍農夫，手裡拿著一把沾滿泥土的鋤頭，神色警惕，說話帶著濃郁的漳州腔。"},
        "responses": {
            "爭水": {"zh-TW": "泉州人太霸道了！把上游的水源全用土壩攔住，我們下游客莊的稻子全都要枯死了！不打一仗，大家都得餓死！"},
            "械鬥": {"zh-TW": "鋤頭不光是耕地用的，也是保命用的。前幾年械鬥，我用這鋤頭跟泉州人的鐵叉拼過命。這水圳裡的泥，是紅色的。"},
            "陳仔": {"zh-TW": "我就是個耕田的，誰想天天打仗？但宗族兄弟如果不抱團，在這台灣荒島上根本活不下去。"}
        }
    },
    {
        "id": "NPC_a_shui",
        "name": {"zh-TW": "商人阿水"},
        "settlement": "yunlin",
        "home_site": "yunlin_douliu_street",
        "role": "merchant",
        "hint": {"zh-TW": "泉州籍雜貨商，穿著長衫，撥弄著算盤，說話精明。"},
        "responses": {
            "漳州人": {"zh-TW": "漳州人說我們攔水，但那水圳是我們泉州庄出錢出力挖的，憑什麼白白分給他們？凡事要講個理，不講理就只能動傢伙了。"},
            "商路": {"zh-TW": "斗六街是漳泉商旅的交會點。每次鄉下械鬥打起來，城裡的鋪子就得關門。和氣生財，但底線不能讓！"}
        }
    },
    {
        "id": "NPC_hakka_old_woman",
        "name": {"zh-TW": "客家老婦"},
        "settlement": "yunlin",
        "home_site": "yunlin_hakka_village",
        "role": "elder",
        "hint": {"zh-TW": "滿臉皺紋的客家老阿婆，穿著藍衫，雙手顫抖地捧著一本殘缺不全的族譜。"},
        "responses": {
            "族譜": {"zh-TW": "這是我們張氏家族從廣東帶過來的族譜。上次庄子被放火，大堂燒毀了，我冒死把這族譜搶了出來。這是我們在台灣的根，不能丟啊。"},
            "轉移族譜": {"zh-TW": "年輕人都去參加義民軍守隘口了。如果庄子守不住，請好心人幫忙把這本族譜送到苗栗義民廟的親族那裡去，老婆子感激不盡。"},
            "客家庄": {"zh-TW": "我們客家人在平原人少，常被閩南大庄欺負。只有拜義民爺、大家抱成一團，才能活下來。"}
        }
    }
]

for npc in npcs:
    write_yaml("npcs", f"{npc['id']}.yaml", npc)


# --- P23.5 Memories ---

memories = [
    # EP001 Zhu Yigui
    {
        "id": "zhu_yigui_daily",
        "title": "鴨母王的日常",
        "era": "v1.2",
        "evidence_type": "生態記憶",
        "quality": 2,
        "progress": 10,
        "description": "清康熙晚期，阿公店（岡山）郊外。朱一貴手持青竹竿，站在寬闊的養鴨池旁。他一聲呼哨，數百隻母鴨排成整齊的雁行方陣游過水面。圍觀的鄉民驚嘆：『阿貴能使鴨如兵，真乃天命也！』",
        "settlement": "kaohsiung",
        "trigger_site": "gangshan_duck_pond",
        "conditions": []
    },
    {
        "id": "short_spring",
        "title": "義軍的短暫春天",
        "era": "v1.2",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "1721年夏，台南府城。朱一貴登基，大興王府前張燈結彩。義軍宣佈廢除清廷苛稅，開倉濟貧，街頭充溢著台灣百姓自主建國的狂喜。然而，這春雷般的建國奇蹟，僅僅維持了寒暑數月。",
        "settlement": "kaohsiung",
        "trigger_site": "tainan_zhuxingwang",
        "conditions": []
    },
    {
        "id": "hakka_rift",
        "title": "客家離心的裂痕",
        "era": "v1.2",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "起義軍佔領府城後的大殿內。杜君英與朱一貴爆發激烈爭吵。杜君英憤而拔刀：『我們客家兄弟流血最多，如今封賞卻無份，這天下是閩南人的天下嗎？』這道裂痕，註定了義軍的分裂與覆滅。",
        "settlement": "kaohsiung",
        "trigger_site": "gangshan_tian_di_hui",
        "conditions": []
    },
    {
        "id": "magistrate_document",
        "title": "知縣的公文",
        "era": "v1.2",
        "evidence_type": "官府記憶",
        "quality": 2,
        "progress": 10,
        "description": "鳳山縣衙書案上。散落著鳳山知縣倉皇逃命時留下的公文。公文中滿是催逼賦稅與緝捕『天地會匪』的嚴厲措辭，字裡行間透出清廷基層統治的腐敗與民怨的沸騰。",
        "settlement": "kaohsiung",
        "trigger_site": "fengshan_fort",
        "conditions": []
    },
    {
        "id": "city_joys",
        "title": "府城內的悲歡",
        "era": "v1.2",
        "evidence_type": "生活記憶",
        "quality": 1,
        "progress": 10,
        "description": "起義軍進城那天，府城普通百姓的院子內。母親抱著孩子躲在水缸後，聽著外面震天的鑼鼓聲與火繩槍聲。百姓在戰火中祈求的不是誰當皇帝，而是最簡單的和平與稻米。",
        "settlement": "kaohsiung",
        "trigger_site": "tainan_zhuxingwang",
        "conditions": []
    },
    # 新增現有打狗與旗津地標的記憶，解決孤立地標問題
    {
        "id": "kaohsiung_harbor_trade",
        "title": "打狗港的戎克船",
        "era": "v1.2",
        "evidence_type": "生活記憶",
        "quality": 2,
        "progress": 10,
        "description": "打狗港內，成群的戎克船與木帆船靠岸。挑夫們光著膀子運送著一袋袋白糖與稻米，這是南部最重要的對外窗口，空氣裡飄著糖蜜與海水的鹹味。",
        "settlement": "kaohsiung",
        "trigger_site": "kaohsiung_harbor",
        "conditions": []
    },
    {
        "id": "qijin_lighthouse",
        "title": "旗後山頂的晚霞",
        "era": "v1.2",
        "evidence_type": "生態記憶",
        "quality": 2,
        "progress": 10,
        "description": "站在旗後山頭，夕陽將打狗海口染成一片金紅。遠處的漁火在晚霞中閃爍，那時還沒有鋼筋水泥燈塔，只有守望海口的哨所與古老航標。",
        "settlement": "kaohsiung",
        "trigger_site": "qijin",
        "conditions": []
    },
    {
        "id": "qishan_banana_valley",
        "title": "薯寮山谷的晨霧",
        "era": "v1.2",
        "evidence_type": "生活記憶",
        "quality": 1,
        "progress": 10,
        "description": "蕃薯寮（旗山）山谷，清晨的霧氣還沒散去，農夫便挑著一擔擔番薯與山產在石板路上跋涉。這裡的汗水，匯聚成了打狗山城最初的商業血脈。",
        "settlement": "kaohsiung",
        "trigger_site": "qishan",
        "conditions": []
    },
    # EP002 Lin Shuangwen
    {
        "id": "spread_map",
        "title": "失控的版圖",
        "era": "v1.2",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "乾隆五十一年冬，林爽文在彰化大里杙誓師。起義軍在幾週內連克彰化、諸羅，戰火以星火燎原之勢席捲半個台灣。清廷守軍節節敗退，台灣的版圖在天地會的大旗下一度完全失控。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_city_site",
        "conditions": []
    },
    {
        "id": "south_route",
        "title": "莊大田的南路",
        "era": "v1.2",
        "evidence_type": "歷史事件",
        "quality": 2,
        "progress": 10,
        "description": "鳳山縣城外。南路領袖莊大田親自抬著土炮擊碎了縣城大門，義軍如潮水般湧入。莊大田站在廢墟上大喊：『北有林爽文，南有莊大田！滿清的江山今天到頭了！』",
        "settlement": "kaohsiung",
        "trigger_site": "fengshan_fort",
        "conditions": []
    },
    {
        "id": "yi_min_opposition",
        "title": "對立的同鄉",
        "era": "v1.2",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "彰化平原交界處。起義軍與客家庄的『義民軍』持械對峙。雙方本是渡海來台的同鄉，卻因土地防衛與宗族派系，在戰場上兵刃相向，成為清領台灣歷史上最深沉的悲劇。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_confucian_temple",
        "conditions": []
    },
    {
        "id": "changhua_fear",
        "title": "彰化縣城的恐懼",
        "era": "v1.2",
        "evidence_type": "生活記憶",
        "quality": 2,
        "progress": 10,
        "description": "被起義軍圍困的彰化縣城內。夜裡火光四起，城內米糧斷絕。百姓在隘門後瑟瑟發抖，握著菜刀聽著八卦山頂傳來的隆隆炮聲，感受著戰火臨城的極度恐懼。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_east_gate",
        "conditions": []
    },
    {
        "id": "oxcart_bones",
        "title": "牛車與骸骨",
        "era": "v1.2",
        "evidence_type": "物件記憶",
        "quality": 3,
        "progress": 10,
        "description": "林爽文事件平息後，一輛輛滿載著無名戰死義民骸骨的牛車緩緩駛入彰化庄。鄉紳含淚將骸骨合葬，建立了義民塚（今彰化義民廟）。那嘎吱作響的牛車輪軸聲，承載著中台灣沉重的歷史悲哀。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_south_gate",
        "conditions": []
    },
    # EP003 Dai Chaochun
    {
        "id": "four_year_siege",
        "title": "四年的圍城",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "同治元至四年，彰化縣城。戴潮春的八卦會將彰化古城團團圍困。城門緊閉，護城河乾涸。四年中，圍城成了彰化人生活的常態，無數商號倒閉，昔日繁華的中台灣走廊化為廢墟。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_west_gate",
        "conditions": []
    },
    {
        "id": "clan_game",
        "title": "宗族的博弈",
        "era": "v1.5",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "霧峰林家大宅的密室中。林朝棟與幕僚看著地圖。戴潮春八卦會勢大，但清軍援兵已至。林家面臨生死抉擇：是繼續觀望，還是起兵協助清軍換取樟腦開採權與世襲官爵？",
        "settlement": "wufeng",
        "trigger_site": "wufeng_lin_mansion",
        "conditions": []
    },
    {
        "id": "city_changes_hands",
        "title": "易手的城池",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 2,
        "progress": 10,
        "description": "彰化城樓上。八卦會的黃旗被降下，清軍的黃龍旗與霧峰林家勇營的字姓旗重新升起。城外遍地狼煙，這座多次易手的城池，城磚已被戰火燻得焦黑一片。",
        "settlement": "changhua_city",
        "trigger_site": "changhua_north_gate",
        "conditions": []
    },
    {
        "id": "yearn_for_peace",
        "title": "平靜的渴望",
        "era": "v1.5",
        "evidence_type": "生活記憶",
        "quality": 1,
        "progress": 10,
        "description": "經歷了戴潮春四年大亂後，斗六老街的黃昏。雜貨鋪老闆重新打開了緊閉四年的木板門，清掃街面的石板。百姓提著菜籃走過，貪婪地享受著這得來不易、不知能維持多久的平靜。",
        "settlement": "yunlin",
        "trigger_site": "yunlin_douliu_street",
        "conditions": []
    },
    # EP004 Mudan Incident
    {
        "id": "arugus_rules",
        "title": "阿祿古斯的規矩",
        "era": "v1.5",
        "evidence_type": "社會記憶",
        "quality": 3,
        "progress": 10,
        "description": "1871年，牡丹社石板屋內。總頭目阿祿古斯看著獲救的琉球漁民，指著圖騰柱告誡：『喝了我們的水，就是客。但不能跨過祖靈地界的紅線，否則就是挑釁。』這條規矩，是山林千百年的生存法則。",
        "settlement": "mudan",
        "trigger_site": "mudan_paiwan_village",
        "conditions": []
    },
    {
        "id": "japanese_footprints",
        "title": "日軍的足跡",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 2,
        "progress": 10,
        "description": "1874年夏，車城灣沙灘。日軍士兵在軍號聲中列隊登陸，西鄉從道都督親自將軍旗插在沙灘上。蒸汽軍艦在近海吐著黑煙，這是近代台灣土地上第一次出現成建制的日軍足跡。",
        "settlement": "mudan",
        "trigger_site": "mudan_japanese_landing",
        "conditions": []
    },
    {
        "id": "interpreter_diary",
        "title": "翻譯官的日記",
        "era": "v1.5",
        "evidence_type": "個人記憶",
        "quality": 2,
        "progress": 10,
        "description": "登陸軍營內。田中翻譯官在煤油燈下用顫抖的手寫道：『這裡的夏日酷熱難耐，山林如同一隻巨大的綠色野獸。番社戰士的吹箭與長槍神出鬼沒，我們根本看不到敵人。這不是保護琉球，這是地獄。』",
        "settlement": "mudan",
        "trigger_site": "mudan_japanese_landing",
        "conditions": []
    },
    {
        "id": "shen_memorial",
        "title": "欽差的考量",
        "era": "v1.5",
        "evidence_type": "官府記憶",
        "quality": 3,
        "progress": 10,
        "description": "射寮港碼頭旁臨時大帳中。沈葆楨看著恆春半島地圖，神色凝重：『日人志不在琉球人，而在窺我台灣。當速建城池以實邊防，並開山招撫後山生番，不能再使此地為化外之民。』",
        "settlement": "mudan",
        "trigger_site": "checheng_harbor",
        "conditions": []
    },
    {
        "id": "empire_probe",
        "title": "帝國擴張的試探",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "1874年底，日本東京皇居內。陸軍大臣指著台灣恆春地圖，對參謀說：『清廷雖然退讓賠款，但我們已經試探出了他們海防的空虛與退讓。台灣，將是我們大日本帝國向南擴張的第一塊基石。』",
        "settlement": "mudan",
        "trigger_site": "mudan_stone_gate",
        "conditions": []
    },
    # EP005 Taiwan Province
    {
        "id": "modernization",
        "title": "近代化的腳步",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "1887年，台北大稻埕. 蒸汽火車『騰雲號』在震耳欲聾的汽笛聲與滾滾黑煙中緩緩出站，兩旁擠滿了驚嘆的市民。劉銘傳站在月台上，看著鐵軌延伸向南方，宣告台灣近代化時代的正式來臨。",
        "settlement": "taipei",
        "trigger_site": "dadaocheng_yanping_pier",
        "conditions": []
    },
    {
        "id": "laborers_sweat",
        "title": "苦力的汗水",
        "era": "v1.5",
        "evidence_type": "生活記憶",
        "quality": 2,
        "progress": 10,
        "description": "苗栗深山鐵道工地。烈日當空，鐵道苦力老周與夥伴用鋼鏟敲擊堅硬的花崗岩，肩膀被扁擔磨得血肉模糊。昨夜山體滑坡壓死了兩名工友，但工頭皮鞭一揚，繁重的勞作依然沒有停息。",
        "settlement": "miaoli",
        "trigger_site": "miaoli_old_railway",
        "conditions": []
    },
    {
        "id": "aboriginal_cost",
        "title": "開山撫番的代價",
        "era": "v1.5",
        "evidence_type": "生態記憶",
        "quality": 2,
        "progress": 10,
        "description": "被清軍洋槍大炮轟擊後、殘火未熄的大嵙崁泰雅族部落。千年古樹被砍伐殆盡用以提煉樟腦，原住民戰士抱著戰死親人的屍體，看著被強行開闢的官道，眼中滿作國族擴張帶來的血淚仇恨。",
        "settlement": "miaoli",
        "trigger_site": "dakeng_aboriginal_village",
        "conditions": []
    },
    {
        "id": "province_glory",
        "title": "建省十年的榮光與落寞",
        "era": "v1.5",
        "evidence_type": "歷史事件",
        "quality": 3,
        "progress": 10,
        "description": "1895年初，大稻埕茶行屋頂上。老茶商扶著欄杆看著台北城。劉銘傳早已離職，建省十年的洋務榮光，在甲午戰敗、台灣即將割讓日本的傳言中，化為滿城惶恐與無奈的落寞長嘆。",
        "settlement": "taipei",
        "trigger_site": "dadaocheng_tea_warehouse",
        "conditions": []
    },
    # 解決苗栗義民廟孤立問題
    {
        "id": "miaoli_yi_min_belief",
        "title": "苗栗褒忠的香火",
        "era": "v1.5",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "苗栗義民廟殿內，擺滿了鄉民奉獻的香燭。自林爽文大亂以後，保鄉衛土的義民信仰在此生根，大清皇帝御賜的『褒忠』牌匾在大殿上方熠熠生輝，成為凝聚地方客家人的精神堡壘。",
        "settlement": "miaoli",
        "trigger_site": "miaoli_hakka_yi_min",
        "conditions": []
    },
    # 解決雲林地標孤立問題
    {
        "id": "yunlin_genealogy_transfer",
        "title": "客家庄的殘缺族譜",
        "era": "v1.2",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "雲林客家庄祠堂廢墟。火災燒毀了大部分大堂，客家老阿婆在灰燼中哭泣，緊緊抱著一本殘破的張氏族譜。這本殘缺的族譜，是他們宗族在台灣開墾的唯一血脈證據。",
        "settlement": "yunlin",
        "trigger_site": "yunlin_hakka_village",
        "conditions": []
    },
    {
        "id": "yunlin_water_clash",
        "title": "水圳旁的鋤頭對決",
        "era": "v1.2",
        "evidence_type": "生態記憶",
        "quality": 2,
        "progress": 10,
        "description": "水圳閘門旁，兩邊的庄民手持鋤頭與鐵叉對峙。為了爭奪賴以生存的灌溉水源，昔日的鄰里在泥濘中拼死相搏，水流中漸漸染上了暗紅，訴說著生存與分類的血淚。",
        "settlement": "yunlin",
        "trigger_site": "yunlin_irrigation_field",
        "conditions": []
    },
    # 解決恆春地標孤立問題
    {
        "id": "hengchun_wall_built",
        "title": "恆春古城的基石",
        "era": "v1.5",
        "evidence_type": "官府記憶",
        "quality": 2,
        "progress": 10,
        "description": "恆春建城工地。沈葆楨督導官民，使用當地的硓𡏆石與磚石混合築城。城牆拔地而起，阻斷了海風與外敵，宣告此地從此納入朝廷防務的核心版圖。",
        "settlement": "hengchun",
        "trigger_site": "hengchun_old_town",
        "conditions": []
    },
    {
        "id": "hengchun_south_gate_scenery",
        "title": "南門外的海風",
        "era": "v1.5",
        "evidence_type": "生態記憶",
        "quality": 1,
        "progress": 10,
        "description": "恆春南門下。強勁的落山風捲起沙塵，城門外的官道直通南海口。戍守城門的士兵拉緊了帽帶，默默守望著這片島嶼最南端的國境邊陲。",
        "settlement": "hengchun",
        "trigger_site": "hengchun_south_gate",
        "conditions": []
    },
    # 解決霧峰地標孤立問題
    {
        "id": "wufeng_academy_lecture",
        "title": "萊園私塾的讀書聲",
        "era": "v1.5",
        "evidence_type": "社會記憶",
        "quality": 2,
        "progress": 10,
        "description": "萊園的木造亭台內，清風徐徐。私塾先生正在指導林家子弟研讀經史，低沉的書聲伴隨著流水聲。在戰亂頻仍的时代，這裡保留了一絲難得的文教火種，亦孕育著未來思想改革的溫床。",
        "settlement": "wufeng",
        "trigger_site": "wufeng_academy",
        "conditions": []
    }
]

for mem in memories:
    write_yaml("memories", f"{mem['id']}.yaml", mem)

print("ALL VOL2 YAML FILES SUCCESSFULLY GENERATED!")
