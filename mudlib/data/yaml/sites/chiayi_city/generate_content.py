#!/usr/bin/env python3
"""Batch generate chiayi_city NPCs, Incidents, Memories, Quests, and World Events."""
import os

BASE = "/home/wade/src/github/FormosaSaga/mudlib/data/yaml"

# ─── NPCs (25 needed) ─────────────────────────────────────────────────────────
npcs = [
    ("NPC_city_god_keeper_chiayi", "城隍廟廟公阿全", "temple_keeper", "chiayi_city_temple",
     "身穿灰色道袍的老廟公，手持銅鈴在廟埕內來回巡視，目光如炬。",
     {"城隍": "城隍爺是嘉義的守護神，管的是陰間秩序。你說你來嘉義找什麼？找歷史？城隍爺都記錄著的。",
      "二二八": "（停頓很久）那幾天，廟埕裡站滿了人，有人在哭，有人在搬東西躲進來。城隍爺的神轎那幾天不停地在動，我阿爸說是不甘心的魂太多了。",
      "傳言": "你問傳言？嘉義城隍廟的傳言你要聽幾天？最近的是：有人深夜在廟門口看到一個穿旗袍的女人，問了廟的方向，問完就消失了，鞋聲都沒有。"}),
    ("NPC_railway_engineer_chiayi", "阿里山鐵路老技師阿義", "engineer", "alishan_railway_depot",
     "穿著磨舊工作服的中年男人，手掌粗厚，工具帶上掛著各式扳手，說話帶著山地口音。",
     {"鐵路": "阿里山的鐵路是奇蹟，從海拔三十公尺的嘉義爬到兩千多公尺的阿里山，螺旋線、之字形，都是日本工程師想出來的。當年我阿公說光是勘測就死了好多人。",
      "機車": "調度場那台Shay機車跟了我三十年，她現在不跑了，但我每天還是來保養她，機油、螺絲，都要定期確認，就算不跑，也要讓她有尊嚴。",
      "傳言": "你說調度場最深處那節車廂？那我就是不知道裡面有什麼，我知道的是，鑰匙在我師父的師父那一代就找不到了，車廂鎖著，我沒有試著開過。"}),
    ("NPC_market_granny_chiayi", "東市場阿桂嬤", "vendor", "central_market",
     "挺著腰板坐在菜攤後方，頭戴斗笠，眼睛銳利，說話直接不拐彎。",
     {"市場": "東市場從我還沒出生以前就在這裡了。我媽在這賣菜，我媽的媽也在這賣菜。我說這市場比嘉義市政府還穩，政府換過好幾次，市場還在。",
      "食物": "嘉義最好吃的是什麼？當然是雞肉飯，但你要懂得選，去那種開了三十年以上的，便宜又新鮮，不要去有招牌的，那是給外地人吃的。",
      "傳言": "你問傳言？市場最裡面那攤布行，說是賣布，我賣了一輩子菜，從來沒看到他們賣過一塊布，卻天天開門，也天天關門，你去問他們在做什麼，我很好奇。"}),
    ("NPC_artist_chiayi", "林阿祥（畫家）", "artist", "art_museum",
     "穿著沾滿油彩的寬鬆棉麻衫，頭髮凌亂，眼鏡片厚重，說話緩慢而精確。",
     {"繪畫": "嘉義為什麼是畫都？因為陳澄波。他用西洋技法畫台灣的山水和人物，畫的不是異國風情，是腳踩的土地。他死在二二八，那件事讓嘉義的畫都名字有了另一層意思。",
      "陳澄波": "（神情凝重）他是被帶到火車站前槍殺的，示眾，讓所有人看。那年他正在談判，試圖讓雙方停火。那件事後，嘉義的藝術圈沉默了好多年。",
      "傳言": "美術館那幅無名畫？我去看過，畫風跟陳澄波不一樣，但構圖和用光的方式……我不敢確定，但那幅畫讓我站在前面站了兩個小時。"}),
    ("NPC_chicken_rice_lady", "老攤雞肉飯老闆娘阿梅", "vendor", "noodle_stall_chiayi",
     "六十歲左右的婦人，圍裙整潔，手腳俐落，臉上常帶一種淡然的平靜。",
     {"雞肉飯": "我賣雞肉飯四十年，我媽賣了三十年，我媽的阿嬤在日本時代就賣了。那時候不叫火雞肉，只叫雞肉，後來換成火雞是因為火雞肉比較便宜，肉比較多。",
      "秘訣": "秘訣就是雞油。雞油要新鮮的，當天煉，隔夜的有腥味。米要好米，飯粒飽滿，不能太軟。就這樣，沒有什麼秘方。",
      "老主顧": "那個樹洞旁邊的碗？我媽說要放，我就放。問我什麼原因，我說不清楚，我媽說老主顧還在，就繼續放。"}),
    ("NPC_lantern_maker_chiayi", "燈籠師傅阿吉", "craftsman", "lantern_street",
     "四十多歲的男人，手指靈活，坐在竹架旁邊彎著腰，做事時眼神專注，旁人說話他聽得到，但不一定回應。",
     {"燈籠": "做燈籠的學問在竹篾的彎法。要讓骨架撐得住，又不能太硬，紙糊上去才不會皺。這件事說起來簡單，沒有三年，做不出一個好燈籠。",
      "日本時代": "我爺爺說，日本時代做燈籠有規定，哪些顏色可以用、哪些圖案可以畫，都要申請。做給廟的容易過，做給人家祭祖的有時候被說是迷信，要偷偷做。",
      "傳言": "我爺爺做過一批燈籠給二二八的義勇軍，後來那批人都消失了，燈籠也消失了。我爺爺說那是他做過最好看的一批燈籠，卻也是讓他後悔最深的一批。"}),
    ("NPC_confucian_teacher", "孔廟老師仁義先生", "scholar", "chiayi_confucian_temple",
     "穿著中式對襟褂子的清瘦老人，手捧一本繁體線裝書，說話文雅，喜歡引用古文。",
     {"孔廟": "諸羅縣文廟從清代就在了，嘉義人重視教育，清代的舉人比例在台灣很高。這個傳統不是偶然的，是幾百年累積下來的。",
      "教育": "日本時代的教育是有目的的，教你說日語、敬天皇。但讀書人知道，字面上服從，心裡要留著自己的根。我的老師就是那樣的人。",
      "傳言": "孔廟大門的高度被日本人降低過，這是真的，不是傳言。你量量看那個門檻，不到正常高度，是刻意的，說是現代化，其實是別的意思。"}),
    ("NPC_tailor_chiayi", "旗袍裁縫師傅清月", "craftsman", "qipao_tailor_chiayi",
     "穿著剪裁合身旗袍的中年女性，拿著針線，眼神精準，說話簡潔，動作優雅不失效率。",
     {"旗袍": "旗袍是從上海傳來的，但嘉義的版本不一樣，剪裁比較寬鬆，是台灣熱帶氣候改良的。我做的旗袍，穿起來要舒服，不只是好看。",
      "日本時代": "那時候流行和服，旗袍被認為是中國的東西，不好賣。但廟裡的女信眾還是要旗袍，所以我祖母改口說是「南方式洋裁」，才繼續做。",
      "神秘客人": "你說每年那個客人？她從來不量身，但每件旗袍都合身。我自己猜，她每次拿走的都是同樣的尺寸，只是款式不同。問她名字，她說你直接叫我阿嬤就好。"}),
    ("NPC_prison_guard_old", "舊監獄老導覽員阿賢", "guide", "chiayi_prison_old",
     "穿著文化園區背心的退休老人，腰板挺直，說起監獄歷史神情複雜，時有長停頓。",
     {"監獄": "這個扇形設計叫邊沁式監獄，一個守衛可以看到所有廊道。日本人把西方的監控哲學帶來台灣，用在這個地方。現在變成觀光景點，設計的目的和現在的用途，差距很大。",
      "囚犯": "這裡關過各式各樣的人，抗日的義士、走私犯、政治犯、普通罪犯。二二八之後，這裡很滿。我不說更多了。",
      "傳言": "某個牢房的牆壁上的那首詩？我知道你在說哪個。我第一次發現的時候是五年前，現在已經有人給它拍了照，但沒有人知道是誰刻的，也沒有人認出那個人。"}),
    ("NPC_hospital_doctor_old", "舊醫院老醫師陳文中", "doctor", "chiayi_old_hospital",
     "白髮蒼蒼的老醫師，仍習慣穿著白色大褂，雙手背在身後，說話條理清晰，偶爾會用日語說出醫學名詞再翻譯。",
     {"醫學": "日本時代的醫療比你想像中進步，但只對日本人和少數精英台灣人開放。一般台灣農民生病了，往往靠草藥和廟醫，直到戰後才逐漸改善。",
      "二二八": "（搖頭）那幾天，醫院收了很多傷患，但我只是年輕的實習生，我沒有資格說自己懂那件事。我只知道，有幾個人被帶進來，又被帶走，後來就沒有回來。",
      "傳言": "手術室的那幾個字？那不是傳言。我見過，年輕的時候。後來新主任說要粉刷，我沒有說反對，但我記得那幾個字，一直記得。"}),
    ("NPC_sugar_factory_supervisor", "糖廠監督員阿坤", "supervisor", "sugar_refinery_north",
     "體型結實的中年男人，藍色工作服口袋插著計算尺，說話有生意人的精明，但眼神偶有一絲不安。",
     {"糖廠": "北廠現在產量下滑了，不是機器的問題，是甘蔗供應少了。農民改種鳳梨、改種蔬菜，因為利潤比較高。台灣糖業的時代，在我這個世代差不多到頭了。",
      "日本時代": "你說日本時代糖廠怎樣？那時候農民沒有選擇，土地就是要種甘蔗，價格也是糖廠訂，叫做「保証價格」，實際上是壓價。但廠是有的，工作是有的，人是活著的。",
      "傳言": "那個格子我知道，從我接手的第一天前任就跟我說，那個格子不要開。我問為什麼，他說不知道，前任的前任跟他說的。就這樣傳下來了。"}),
    ("NPC_broadcasting_staff", "放送局老播音員春花", "broadcaster", "chiayi_broadcasting",
     "六十多歲的女性，說話聲音清亮，每句話的尾音自然揚起，像是永遠在廣播狀態。",
     {"廣播": "我做廣播四十年，廣播的力量在於，你看不見說話的人，但你聽得到他的聲音。聲音能傳進任何地方，鎖不住它。",
      "二二八": "二二八那天，這裡有人試圖廣播。我當時還小，但我聽到了。後來那個聲音就消失了，廣播中斷，然後是靜默，那段靜默比任何話都更讓人害怕。",
      "傳言": "那個麥克風說過什麼？沒有錄音。但有個老播音員說，他聽過一個版本的說法，是當年廣播出去的最後一句話，那句話我轉述給你聽，但我沒辦法確認是不是真的。"}),
    ("NPC_incense_maker_chiayi", "百年香舖第四代阿隆", "craftsman", "incense_shop_chiayi",
     "三十多歲的年輕男人，身上有淡淡的沉香味，做事謹慎，對古老配方有一種近乎執著的尊重。",
     {"香": "我家的香從清代傳下來，每種香的配方都有它的用途。廟裡驅邪用的和祭祖用的不一樣，祭典用的和日常薰房用的不一樣。香是和神明、祖先說話的語言。",
      "日本時代": "日本人說香是迷信，要取締。我曾祖父改口說是醫療防疫用品，改了包裝，繼續賣。台灣人在那個時代非常會說謊，但都是為了存活。",
      "傳言": "那種老委員問的香？我知道，那是一個叫『迴瀾』的配方，是清代用在大型祭典的，材料之一在戰後進不來了。我有一小包最後的存貨，不知道要怎麼處理。"}),
    ("NPC_city_park_elder", "公園老棋手阿山", "elder", "city_park",
     "每天下午在大榕樹下擺棋盤的老人，象棋棋子被摸得油光發亮，說話帶著洞悉一切的淡然。",
     {"公園": "這個公園以前是神社，神社拆了才變公園。那些石燈籠沒人搬，就留著。現在孩子在石燈籠旁邊跑，不知道那是什麼，也好，就這樣吧。",
      "下棋": "下棋是一個人坐著等另一個人的方式。你說要等誰？不重要，重要的是等著本身。我在這裡等了三十年，每天都有人來坐下來，每天都不一樣。",
      "傳言": "地窖？我聽說過。我年輕的時候挖過，在石階旁邊挖了兩尺，挖到一個鐵蓋，鏽死了，用了三個人也打不開。後來被人說是破壞古蹟，就填回去了，現在草長過去了，你看不到了。"}),
    ("NPC_riverside_fisherman", "八掌溪漁夫阿水伯", "fisherman", "riverside_settlement",
     "黑瘦的老漁夫，赤腳站在溪石上，看著水面的時間比說話的時間長。",
     {"溪": "八掌溪現在魚少了，以前我爸說一網下去幾十條，現在一天撈到十條就不錯了。是農藥，是開發，是很多事情加在一起。",
      "顱風": "颱風來我就走，不走沒辦法，溪水一漲，堤外就淹。我已經搬過三次了，每次颱風過後，又回來蓋。這裡有我的生計，走不開。",
      "傳言": "漂來的那塊木頭？那是真的，我撈到的。那個地圖我看了，指向嘉義公園，我不去挖，那是公家的地，而且我覺得那不是地圖，那是某種記號，但記號要說什麼，我看不懂。"}),
    ("NPC_county_hall_guard", "舊縣廳門衛老伯", "guard", "chiayi_county_hall_old",
     "在舊縣廳改建的文化機構擔任警衛，六十幾歲，對建築如數家珍，對訪客有問必答。",
     {"縣廳": "清代的縣署在這個位置，日本人蓋廳舍，也在這個位置，國民政府接收，縣政府還在這個位置。這塊地的命運就是做官府用的。",
      "歷史": "諸羅縣那時候管的範圍很大，比現在的嘉義縣市加起來還大。你知道諸羅為什麼改叫嘉義？就是因為林爽文之役，城裡的人守住了，皇帝說你們很「義」，就改名了。",
      "傳言": "地板低了的那個房間？我知道，我帶你去看。但你不能挖，你只能看，那個坑在哪裡，我用走的方式讓你感覺，腳踩下去有點空洞感，就是那裡。"}),
    ("NPC_old_policeman_228", "老警員阿忠（二二八倖存者）", "witness", "police_station_old",
     "已退休的老警員，身材佝僂，說話時眼神很少直視對方，但談到歷史時聲音平靜得不自然。",
     {"警察": "我做警察是民國四十年以後的事，二二八的時候我才十四歲，我只是看到的，不是做的。這件事我說清楚。",
      "二二八": "（長時間沉默）那幾天，嘉義機場的戰鬥我沒有直接看到，但槍聲聽到了。後來有人被帶到火車站，我在旁邊，我看到了，但那個人是誰，我那時候不認識。後來我才知道，是陳澄波。",
      "傳言": "檔案室被清理的事？那不是傳言，是事實。我是後來的人，我沒有資格說清楚，但有些東西，清理過一次就找不回來了。"}),
    ("NPC_medicine_seller_chiayi", "藥材行老闆達仔", "merchant", "chiayi_old_hospital",
     "胖臉和藹的中年男人，圍裙上有一股藥草混合的特殊氣味，話多，笑聲大。",
     {"藥材": "中藥西藥我都賣，嘉義的人很實際，什麼有效就用什麼，不分中西。我說你要先看病，再吃藥，但很多人是先吃藥再看病，習慣了。",
      "日本時代": "日本人帶來西醫，但台灣人的漢方藥也沒消失，兩個一起用，那時候很常見。反正都是為了活著，管他什麼方法。",
      "傳言": "舊醫院手術室的字？我聽說有人拍了照片，有人傳出來，我看過，是日文漢字混著，寫的是某個人的名字和一個日期，我念給你聽……"}),
    ("NPC_noodle_boss_chiayi", "米糕老闆阿進", "vendor", "central_market",
     "瘦長的中年男人站在灶前，用大勺子分裝米糕，動作快準狠，說話也是一樣節奏。",
     {"米糕": "嘉義米糕和台南米糕不一樣，我們的是乾式的，糯米蒸透後拌豬油，上面鋪魯肉和香菇，再加一小匙蒜泥。這是我阿嬤傳下來的比例，一點都不能差。",
      "市場": "東市場每個攤位都有故事，隔壁賣魚的從我小時候就在那裡，再隔壁賣豆腐的換了三代了，但還在同樣的位置。位置是這個市場的財產。",
      "傳言": "那個布行？我也很奇怪，他們在賣布的時代我沒有看到他們賣布，我問過，他說是倉儲，不是零售。他說話很少，但人沒有問題，就是奇怪。"}),
    ("NPC_railroad_station_clerk", "車站站務員阿義", "clerk", "chiayi_train_station",
     "穿著制服的年輕站務員，工作時認真，下班後話多，是觀察嘉義南來北往旅客的最佳位置。",
     {"車站": "嘉義車站一天有幾百班列車，縱貫線加阿里山線，這裡是嘉南平原和山區的交界點。你要去哪裡，告訴我，我幫你查班次。",
      "旅客": "各種人都從這裡過，農夫、學生、商人、軍人。有時候看到很老的人獨自坐在月台上，對著某個方向看，我不敢問他們在等誰，因為感覺是在等一個很久以前的班車。",
      "傳言": "月台那個燈柱？下面有個刻痕，很多人不注意，但如果你蹲下來看，是一個日期和一個字，字是「待」。沒有人知道誰刻的，為什麼刻，那個日期是昭和二十二年。"}),
    ("NPC_writer_reporter_chiayi", "地方記者阿文", "journalist", "art_museum",
     "手上永遠夾著一個小記事本的中年男人，眼睛習慣性地掃視四周，說話時問的比說的多。",
     {"嘉義": "嘉義是個有話說的地方，只是說的方式不一樣。有的人用畫說，有的人用廣播說，有的人用刻字說，有的人就是沉默地說。",
      "歷史": "嘉義歷史最讓我著迷的是，每一個大事件後面都有一批消失的人，那些人消失了，但他們留下的東西還在，到處都是，只是要知道去哪裡找。",
      "調查": "我在調查一件事，是關於二二八期間一個廣播員說的最後一句話。你如果知道任何線索，告訴我，我不會說是誰告訴我的。"}),
    ("NPC_old_woman_228_family", "二二八家屬老太太春梅", "survivor", "chiayi_city_temple",
     "八十多歲的老婦人，穿著樸素，坐在廟前長凳上，手持念珠，說話聲音很輕，需要靠近才聽得清楚。",
     {"城隍廟": "我每天都來，來了七十年了。我先生二二八那年走的，走之前說他去談判，會回來。他沒有回來，但我每天還是來，在廟裡等一等，然後回家。",
      "先生": "他叫林正雄，是嘉義的醫生，他說他能說得上話，能讓兩邊都聽他的。後來聽說他是其中一個被帶走的人，後來就沒有了。",
      "傳言": "（沉默）你說傳言。我說實話，我七十年沒有聽說過他的下落，也沒有收到任何通知。七十年，他應該在城隍爺那裡了，所以我每天來。"}),
    ("NPC_old_craftsman_wood", "製材所老木工阿福", "craftsman", "lumber_yard_chiayi",
     "雙手厚繭、身材矮壯的老人，身上有松木和鋸木屑的氣味，說話緩慢，每句話都像在切割木頭。",
     {"木材": "阿里山的檜木是台灣最好的木材，日本人知道，所以才建鐵路、建製材所，把那些百年老樹送下來。那些樹砍了就沒了，這件事我到現在還很難接受。",
      "製材所": "我在製材所做了三十年，剖木、打磨、分類。最好的木材送去蓋神社，蓋官廳，蓋有錢人的房子。工人住的地方用的是什麼？邊角料，剩下來的那些。",
      "傳言": "那個房間？那個我知道，是日本時代的辦公室，我做了三十年，沒有人進去過。磚封住的，裡面有什麼沒有人說，但我有一次在牆邊聽到裡面有聲音，像是紙張翻動的聲音，可能是老鼠，也可能不是。"}),
    ("NPC_chiayi_schoolgirl", "公學校女學生阿玲", "student", "chiayi_confucian_temple",
     "十五歲左右的少女，穿著黑白制服，說話帶著學生氣的好奇，對歷史問題格外認真。",
     {"學校": "我在嘉義女中讀書，學校是日本時代蓋的，但我們現在讀的是中文課本。老師說要認識台灣歷史，但課本很薄，好多事情都只有一兩行。",
      "歷史": "你知道陳澄波嗎？他是我們嘉義人，我在美術館看過他的畫，老師說他在二二八走了，但課本上沒有寫這件事，我是自己去查的。",
      "傳言": "我聽同學說孔廟的某塊石板下面有字，是清代秀才刻的，寫的是諸羅縣的一個秘密，她說是在一本舊書裡看到的。我去找那塊石板，但不確定哪一塊。"}),
]

# ─── Incidents (6 needed) ──────────────────────────────────────────────────────
incidents = [
    {
        "id": "chiayi_228_incident",
        "name": "嘉義二二八：機場攻防與藝術家之死",
        "description": "民國三十六年（1947）三月，嘉義爆發激烈的二二八事件，市民義勇軍包圍水上機場，試圖奪取武器。\n陳澄波與三名仕紳代表赴水上機場談判，遭逮捕後被押至嘉義火車站前槍決示眾。\n你試圖透過殘存的記憶碎片、目擊者口述、文物，還原這段歷史的輪廓。",
        "truth": "嘉義二二八的特殊性在於，市民以相對有組織的方式進行武裝抵抗，並試圖透過談判解決。陳澄波的死不是意外，是刻意的示眾行為，目的是恐嚇和瓦解抵抗意志。事件後，嘉義的文化界沉默了近四十年。",
        "era": "postwar",
        "scope": ["chiayi_city"],
        "clues": [
            {"id": "airport_battle_report", "name": "機場攻防目擊者口述", "type": "npc_ask", "source": "npc:NPC_old_policeman_228", "topic": "二二八"},
            {"id": "chen_chengpo_painting", "name": "陳澄波最後作品", "type": "site_look", "source": "site:art_museum"},
            {"id": "228_family_testimony", "name": "二二八家屬春梅的等待", "type": "npc_ask", "source": "npc:NPC_old_woman_228_family", "topic": "先生"},
            {"id": "broadcasting_last_words", "name": "放送局最後廣播", "type": "npc_ask", "source": "npc:NPC_broadcasting_staff", "topic": "二二八"},
        ],
        "reward": {"exp": 2000, "faction": "taiwan_historical_truth", "reputation": 150},
    },
    {
        "id": "chiayi_linshuangwen_incident",
        "name": "林爽文之役：諸羅義民",
        "description": "乾隆五十一年（1786），林爽文率領天地會眾起義，佔領台灣大部分地區。\n諸羅縣城成為清朝在南台灣的重要據點，城內軍民頑強守城長達十個月。\n「嘉義」這個名字，就是乾隆皇帝為表揚守城之「義」而賜名。\n你透過古城牆、文廟、城隍廟的記憶，還原這段義民守城的歷史。",
        "truth": "林爽文事件中的「義民」守城，並非如官方所呈現的純粹忠君愛國，其背後有更複雜的族群角力（閩粵矛盾）與在地利益考量。但守城的勇氣和犧牲是真實的，「嘉義」這個名字因此得來，成為台灣最早因義行得名的地方。",
        "era": "qing",
        "scope": ["chiayi_city"],
        "clues": [
            {"id": "city_wall_siege_mark", "name": "舊城牆上的攻城痕跡", "type": "site_look", "source": "site:old_city_wall"},
            {"id": "confucian_temple_document", "name": "文廟的守城記事", "type": "site_look", "source": "site:chiayi_confucian_temple"},
            {"id": "county_hall_record", "name": "縣廳舊檔中的義民名冊", "type": "npc_ask", "source": "npc:NPC_county_hall_guard", "topic": "歷史"},
        ],
        "reward": {"exp": 1500, "faction": "taiwan_cultural_memory", "reputation": 100},
    },
    {
        "id": "chiayi_alishan_lumber_incident",
        "name": "阿里山林業開發：百年神木的消失",
        "description": "明治四十一年（1908），嘉義至阿里山的鐵路動工，日本的阿里山林業開發正式展開。\n百年以上的檜木、扁柏、紅檜被大規模採伐，嘉義製材所成為全台最大木材加工中心。\n你透過製材所遺址、鐵路調度場、老木工的記憶，還原這段山林開發的歷史代價。",
        "truth": "阿里山林業的開發在短短數十年內砍伐了大量原始森林，改變了山地原住民鄒族的生活空間與文化領地。嘉義的「木材之都」繁榮建立在山林消耗的基礎上，戰後雖縮小規模，但生態損失已無法彌補。",
        "era": "japanese",
        "scope": ["chiayi_city"],
        "clues": [
            {"id": "lumber_yard_blueprint", "name": "製材所舊設計圖", "type": "site_look", "source": "site:lumber_yard_chiayi"},
            {"id": "railway_log_records", "name": "鐵路運材記錄冊", "type": "site_look", "source": "site:alishan_railway_depot"},
            {"id": "woodworker_memory", "name": "老木工阿福的三十年", "type": "npc_ask", "source": "npc:NPC_old_craftsman_wood", "topic": "木材"},
        ],
        "reward": {"exp": 1200, "faction": "ecological_memory", "reputation": 80},
    },
    {
        "id": "chiayi_chenzhengpo_art_incident",
        "name": "畫都的誕生與凋零：陳澄波的嘉義",
        "description": "陳澄波是台灣西洋美術的先驅，也是嘉義最重要的藝術家。\n他將西洋油畫技法應用於台灣風景與人物，創作出充滿本土氣息的現代畫作。\n二二八事件中，他以仕紳身分赴水上機場談判，遭逮捕後槍決於嘉義火車站前。\n你試圖透過畫作、藝術家的記憶與城市空間，重建這位藝術家的生命與死亡。",
        "truth": "陳澄波的死象徵著一個世代台灣知識份子與藝術家的命運：在殖民地時代艱苦求進，在母國接收後反而成為第一批被清洗的對象。他留下的畫作成為台灣美術史的瑰寶，也成為那個時代最沉重的見證。",
        "era": "postwar",
        "scope": ["chiayi_city"],
        "clues": [
            {"id": "chen_painting_unsigned", "name": "美術館中的無名油畫", "type": "site_look", "source": "site:art_museum"},
            {"id": "artist_testimony", "name": "林阿祥對陳澄波的記憶", "type": "npc_ask", "source": "npc:NPC_artist_chiayi", "topic": "陳澄波"},
            {"id": "station_front_mark", "name": "火車站前的歷史標記", "type": "site_look", "source": "site:chiayi_train_station"},
        ],
        "reward": {"exp": 1800, "faction": "taiwan_cultural_memory", "reputation": 120},
    },
    {
        "id": "chiayi_sugar_economy_incident",
        "name": "糖業資本主義：嘉南平原的甜蜜剝削",
        "description": "日治時期，台灣製糖株式會社在嘉南平原強制推行蔗作，農民失去選擇作物的自由，\n被迫以低於市場的「保証價格」出售甘蔗給糖廠。\n嘉義的糖廠是這個不平等體制的核心機構之一。\n你透過糖廠遺址、農民的口述與舊文書，追查這段甜蜜背後的苦澀。",
        "truth": "台灣糖業的日治時期發展是一種典型的殖民地資本主義剝削：農民的土地和勞力被整合進大規模農業生產體系，利潤流向日本資本。戰後這個體制轉手給國民政府的台糖公司，剝削的結構雖有改變，但農民長期處於弱勢的處境延續了很久。",
        "era": "japanese",
        "scope": ["chiayi_city", "minxiong"],
        "clues": [
            {"id": "sugar_contract_document", "name": "糖業「保証價格」合約", "type": "site_look", "source": "site:sugar_refinery_north"},
            {"id": "farmer_testimony_sugar", "name": "糖廠監督員的矛盾", "type": "npc_ask", "source": "npc:NPC_sugar_factory_supervisor", "topic": "日本時代"},
            {"id": "minxiong_sugar_link", "name": "民雄糖業的關聯", "type": "memory", "source": "memory:minxiong_sugar_001"},
        ],
        "reward": {"exp": 1300, "faction": "taiwan_folk_memory", "reputation": 90},
    },
    {
        "id": "chiayi_city_naming_incident",
        "name": "諸羅改名嘉義：一個城市的命名政治",
        "description": "乾隆五十三年（1788），為表揚諸羅縣城軍民在林爽文事件中的忠義守城，\n清高宗下詔改「諸羅」為「嘉義」，意為「嘉其義行」。\n這個名字從清代延用至今，成為台灣少數因義行而命名的城市。\n你透過縣廳舊址、城牆遺跡與地方記憶，重建這段命名的歷史。",
        "truth": "「嘉義」這個名字的由來，是台灣歷史中少見的正面官方表揚，但它也遮掩了守城過程中更複雜的族群矛盾與政治現實。城市的名字是歷史的壓縮包，展開來才能看到它的全貌。",
        "era": "qing",
        "scope": ["chiayi_city"],
        "clues": [
            {"id": "naming_edict_rubbing", "name": "改名詔書拓本", "type": "site_look", "source": "site:chiayi_county_hall_old"},
            {"id": "confucian_teacher_naming", "name": "仁義先生的城市故事", "type": "npc_ask", "source": "npc:NPC_confucian_teacher", "topic": "歷史"},
            {"id": "city_wall_naming_stone", "name": "城牆上的嘉義刻字", "type": "site_look", "source": "site:old_city_wall"},
        ],
        "reward": {"exp": 1000, "faction": "taiwan_cultural_memory", "reputation": 70},
    },
]

# ─── Memories (20 needed) ─────────────────────────────────────────────────────
memories = [
    {"id": "chiayi_228_001", "title": "火車站前的三月", "era": "postwar", "type": "歷史目擊",
     "quality": 3, "site": "chiayi_train_station", "settlement": "chiayi_city",
     "desc": "民國三十六年三月二十五日清晨，嘉義火車站前廣場人聲寂靜。\n不是早晨的靜，是恐懼的靜。\n四個穿著西裝的男人被帶到廣場中央，其中一個是畫家，他的手曾畫過嘉義的陽光。\n槍聲之後，廣場更靜了，比靜還靜的那種。"},
    {"id": "chiayi_228_002", "title": "廣播室的靜默", "era": "postwar", "type": "口述記憶",
     "quality": 2, "site": "chiayi_broadcasting", "settlement": "chiayi_city",
     "desc": "放送局的麥克風在三月初那幾天說了很多話，那些話是喊叫，是報告，是求援。\n後來麥克風不說話了，不是因為沒有話說，是說話的人消失了。\n靜默比任何話都更響亮，整個嘉義都聽到了那個靜默。"},
    {"id": "chiayi_lumber_001", "title": "製材所的第一班", "era": "japanese", "type": "日誌記錄",
     "quality": 2, "site": "lumber_yard_chiayi", "settlement": "chiayi_city",
     "desc": "明治四十四年，製材所的第一批阿里山檜木運抵嘉義。\n工人們從沒見過那樣粗的原木，要四個人環抱才能合攏。\n鋸台開動的第一天，木屑在陽光裡飛揚，嘉義的空氣裡有了松木和機器的混合氣味。\n那棵樹在山上活了八百年。"},
    {"id": "chiayi_lumber_002", "title": "送上山的最後批木工", "era": "japanese", "type": "人物記憶",
     "quality": 2, "site": "alishan_railway_depot", "settlement": "chiayi_city",
     "desc": "最後一批送上阿里山的本島木工，大正十二年的夏天出發。\n他們坐在小火車的貨車廂裡，看著嘉義平原的稻田漸漸縮小。\n上山之後，有人再也沒有下來，不是因為死，是因為習慣了山上的生活，不想回來了。"},
    {"id": "chiayi_market_001", "title": "東市場的黎明", "era": "japanese", "type": "日常記憶",
     "quality": 2, "site": "central_market", "settlement": "chiayi_city",
     "desc": "東市場天未亮就開市了。\n賣魚的把冰塊敲碎鋪在魚身上，卡嗒卡嗒的聲音是嘉義清晨的第一首歌。\n菜攤的燈光把人的臉照得橘黃，每個人都在說話，聲音疊聲音，形成一種城市才有的喧囂和諧。"},
    {"id": "chiayi_temple_001", "title": "城隍廟的七月普渡", "era": "qing", "type": "信仰記憶",
     "quality": 2, "site": "chiayi_city_temple", "settlement": "chiayi_city",
     "desc": "農曆七月，城隍廟埕搭起高台，台上的大士爺像比廟頂還高。\n紙糊的山珍海味堆成小山，香的煙把整個廟埕瀰漫成灰白。\n城隍爺那幾天特別忙，管著從四方漂來的孤魂，讓他們吃飽，讓他們走。"},
    {"id": "chiayi_temple_002", "title": "問卜的女人", "era": "modern", "type": "日常記憶",
     "quality": 1, "site": "chiayi_city_temple", "settlement": "chiayi_city",
     "desc": "那個老太太每天來，坐在廟前長凳上，手持念珠，不問卜，不燒香，只是坐著。\n廟公說她七十年了，每天都來，說是在等一個人。\n她不說等誰，但看她望向廟門的方向，那個方向通向火車站。"},
    {"id": "chiayi_painting_001", "title": "諸羅山的夕陽", "era": "japanese", "type": "藝術記憶",
     "quality": 3, "site": "art_museum", "settlement": "chiayi_city",
     "desc": "那幅油畫的右下角簽著日文字，但畫的是台灣的山，台灣的光，台灣的土地氣息。\n畫家用西方的媒材，畫出了一個本島人對這片土地的眷戀。\n那種眷戀不是語言說得清楚的，它在色彩和筆觸裡，在看畫的那個人心裡突然疼了一下的感覺裡。"},
    {"id": "chiayi_painting_002", "title": "無名畫的等待", "era": "postwar", "type": "謎團記憶",
     "quality": 2, "site": "art_museum", "settlement": "chiayi_city",
     "desc": "那幅畫掛在這裡，沒有人來認領，也沒有人要移走它。\n策展人說，如果這幅畫有主人，主人一定知道它在這裡。\n但沒有人來，七十年了，只有觀眾來，看完離去，畫繼續掛著，等一個它不確定是否還在等的人。"},
    {"id": "chiayi_train_001", "title": "阿里山小火車的第一聲汽笛", "era": "japanese", "type": "歷史記憶",
     "quality": 2, "site": "alishan_railway_depot", "settlement": "chiayi_city",
     "desc": "明治四十五年，阿里山森林鐵路正式通車。\n第一聲汽笛聲從嘉義出發，穿過平原，爬上山壁，進入森林。\n站台上的人拍手叫好，山上的鄒族人第一次看到這個冒煙的鐵獸，\n面面相觑，不知道這個開始意味著什麼。"},
    {"id": "chiayi_train_002", "title": "月台上的等待", "era": "postwar", "type": "人物記憶",
     "quality": 1, "site": "chiayi_train_station", "settlement": "chiayi_city",
     "desc": "燈柱下面刻著「待」。\n站務員說那個字從他開始做的第一天就在那裡，是哪個昭和年間的人刻的。\n那個人等著什麼，那個人後來等到了嗎，燈柱知道，但燈柱不說話。"},
    {"id": "chiayi_city_naming_001", "title": "乾隆的賜名詔書", "era": "qing", "type": "歷史文件",
     "quality": 3, "site": "chiayi_county_hall_old", "settlement": "chiayi_city",
     "desc": "乾隆五十三年的詔書說：諸羅縣軍民義勇守城，嘉其義行，改名嘉義。\n那幾個字，改變了一座城市的名字，也改變了這座城市和自身歷史的關係。\n從此，嘉義人每次說出自己城市的名字，都在無意識中說出一段守城的記憶。"},
    {"id": "chiayi_wall_001", "title": "土城守夜", "era": "qing", "type": "戰鬥記憶",
     "quality": 2, "site": "old_city_wall", "settlement": "chiayi_city",
     "desc": "乾隆五十二年秋，諸羅縣城被林爽文的軍隊包圍，城牆外是漫漫長夜。\n守城的人白天拿武器，晚上拿鋤頭修補被炮擊崩塌的牆段。\n那些土牆修了崩、崩了修，守了將近十個月。\n城牆上的每一塊舊磚，都吸過那些人的汗。"},
    {"id": "chiayi_kominka_001", "title": "公會堂裡的皇民演講", "era": "japanese", "type": "政治記憶",
     "quality": 2, "site": "performance_stage", "settlement": "chiayi_city",
     "desc": "昭和十四年，公會堂裡坐滿了被通知來「聽講」的嘉義仕紳。\n台上的官員說皇民化是機會，是進步，是成為日本國民的榮耀。\n台下的人臉上是標準的恭敬表情，那個表情後面是什麼，沒有人說出來，\n也沒有人忘記。"},
    {"id": "chiayi_lantern_001", "title": "義勇軍的燈籠", "era": "postwar", "type": "人物記憶",
     "quality": 2, "site": "lantern_street", "settlement": "chiayi_city",
     "desc": "那一批燈籠是紅色的，尺寸比廟用的大，比婚慶的小。\n燈籠師傅的爺爺說，他做那批燈籠時手沒有停過，因為要趕，因為需要它的人說急。\n後來那批燈籠去了哪裡，沒有人說，送去的人也沒有回來說。"},
    {"id": "chiayi_market_002", "title": "布行的秘密", "era": "modern", "type": "謎團記憶",
     "quality": 1, "site": "central_market", "settlement": "chiayi_city",
     "desc": "市場最深處有一家布行，店門永遠開著，但從來沒有布。\n老闆坐在裡面喝茶，有人進去問價，他說缺貨，但沒有說什麼時候有貨。\n市場的人說他在那裡三十年了，從來沒有進過布，也從來沒有人知道他靠什麼維生。"},
    {"id": "chiayi_park_001", "title": "神社的石燈籠", "era": "japanese", "type": "物件記憶",
     "quality": 2, "site": "city_park", "settlement": "chiayi_city",
     "desc": "神社拆了，石燈籠還在。\n那些石燈籠是大正時代用花崗岩刻的，上面有奉納的年份和捐獻者的日本名字。\n戰後的孩子在燈籠旁邊跑，不知道那是什麼，跑過去、跑回來，燈籠默默站著，\n像一個沒有人理解的見證者。"},
    {"id": "chiayi_prison_001", "title": "刑務所的詩", "era": "japanese", "type": "文字記憶",
     "quality": 3, "site": "chiayi_prison_old", "settlement": "chiayi_city",
     "desc": "昭和二十二年三月，牢房的牆壁上出現了用指甲刻的字。\n字是日文漢字交替，是一首沒有名字的詩，寫的是窗外的光，寫的是不知道明天的感覺。\n刻字的人後來去了哪裡，沒有人知道。詩還在牆上，年復一年地留著。"},
    {"id": "chiayi_chicken_rice_001", "title": "火雞肉飯的起源", "era": "postwar", "type": "飲食記憶",
     "quality": 1, "site": "chicken_rice_alley", "settlement": "chiayi_city",
     "desc": "戰後初期，美軍顧問帶來了火雞，火雞肉便宜，一隻可以切出很多份。\n嘉義的廚師把火雞肉用熱水拆絲，淋上煉製的雞油，鋪在白飯上。\n這道食物在最困難的年代讓很多嘉義人吃飽了，後來成了嘉義的名片，\n但記得它起源的人越來越少。"},
    {"id": "chiayi_sugar_001", "title": "甘蔗平原的冬天", "era": "japanese", "type": "農業記憶",
     "quality": 2, "site": "sugar_refinery_north", "settlement": "chiayi_city",
     "desc": "採收季是冬天，嘉南平原的甘蔗在乾冷的季風中一片金黃。\n農民的手被甘蔗葉劃滿了細小的傷口，鹽水泡過繼續砍。\n那些甘蔗送進北廠，製成砂糖，裝進麻袋，運往日本。\n農民得到的是「保証價格」，是一個他們沒有辦法拒絕的數字。"},
]

# ─── World Events (4 needed) ──────────────────────────────────────────────────
world_events = [
    {
        "id": "chiayi_ghost_festival",
        "name": "嘉義城隍廟中元普渡",
        "type": "scheduled",
        "era_active": None,
        "trigger": {"month": 7, "day": 15, "calendar": "lunar"},
        "duration_days": 3,
        "affected_sites": ["chiayi_city_temple", "chiayi_city", "lantern_street"],
        "description": "農曆七月十五日，城隍廟舉行中元大普渡，廟埕搭起高台，燈籠街的紅燈籠全數點亮，整個嘉義的氣氛既熱鬧又肅穆。",
        "site_desc_override": {
            "chiayi_city_temple": "廟埕搭起高台，大士爺像高達兩層樓，香火鼎盛，人聲鼎沸，煙霧瀰漫，分不清是香煙還是紙錢的灰。",
            "lantern_street": "所有的燈籠都亮起來了，巷子被紅光染透，像走進了另一個世界的入口。",
        },
    },
    {
        "id": "chiayi_typhoon_warning",
        "name": "颱風警報",
        "type": "random",
        "era_active": None,
        "probability": 0.3,
        "season": "summer",
        "duration_days": 2,
        "affected_sites": ["riverside_settlement", "chiayi_city", "central_market"],
        "description": "氣象台發布颱風警報，嘉義市進入備戰狀態，市場提早收攤，河岸居民往城裡撤離。",
        "site_desc_override": {
            "chiayi_city": "街道上的攤販都收起來了，圓環噴水池停了，廣場空曠，風吹過的聲音格外響亮。",
            "riverside_settlement": "堤外已無人煙，小屋的竹板被綁緊了，但在強風來臨前，這些薄薄的竹板能撐多久，沒有人知道。",
        },
    },
    {
        "id": "chiayi_alishan_train_festival",
        "name": "阿里山鐵路週年紀念",
        "type": "scheduled",
        "era_active": "modern",
        "trigger": {"month": 12, "day": 25},
        "duration_days": 3,
        "affected_sites": ["alishan_railway_depot", "chiayi_train_station"],
        "description": "阿里山鐵路通車紀念日，調度場展出修復的老式蒸汽機車，各地鐵路迷和遊客聚集嘉義，車站前廣場人滿為患。",
        "site_desc_override": {
            "alishan_railway_depot": "老技師阿義今天特別換了整潔的工作服，那台Shay機車的鋼板被擦得發亮，她今天是主角。",
        },
    },
    {
        "id": "chiayi_228_memorial",
        "name": "二二八和平紀念日",
        "type": "scheduled",
        "era_active": "modern",
        "trigger": {"month": 2, "day": 28},
        "duration_days": 1,
        "affected_sites": ["chiayi_train_station", "art_museum", "chiayi_city_temple"],
        "description": "二月二十八日，嘉義各地舉行紀念活動。美術館展出陳澄波作品，火車站前舉行公民追悼，城隍廟早上特別開光普渡亡魂。",
        "site_desc_override": {
            "chiayi_train_station": "廣場中央放著幾束白菊花，沒有人放的，但每年今天都會出現，沒有人知道是誰放的。",
            "art_museum": "館內安靜異常，今天的參觀者比平日少，但停留的時間比平日長，每個人都在那幅畫前多待了一會兒。",
        },
    },
]

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        print(f"  SKIP (exists): {os.path.basename(path)}")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  CREATED: {os.path.basename(path)}")

# Write NPCs
print("=== NPCs ===")
for npc_id, name_zh, role, site, hint, responses in npcs:
    lines = [
        f"id: {npc_id}",
        f"name:",
        f'  zh-TW: "{name_zh}"',
        f"settlement: chiayi_city",
        f"home_site: {site}",
        f"role: {role}",
        f'hint:',
        f'  zh-TW: "{hint}"',
        f"responses:",
    ]
    for topic, reply in responses.items():
        lines.append(f'  "{topic}":')
        lines.append(f'    zh-TW: "{reply}"')
    write_file(f"{BASE}/npcs/{npc_id}.yaml", "\n".join(lines) + "\n")

# Write Incidents
print("\n=== Incidents ===")
for inc in incidents:
    clue_lines = []
    for c in inc["clues"]:
        clue_lines.append(f"  - clue_id: {c['id']}")
        clue_lines.append(f"    name: {c['name']}")
        clue_lines.append(f"    source_type: {c['type']}")
        clue_lines.append(f"    source_id: \"{c['source']}\"")
        if "topic" in c:
            clue_lines.append(f"    ask_topic: {c['topic']}")
    scope_lines = "\n".join(f"  - {s}" for s in inc["scope"])
    content = f"""incident_id: {inc['id']}
name: {inc['name']}
description: |
  {chr(10).join('  ' + l if i > 0 else l for i, l in enumerate(inc['description'].strip().splitlines()))}
truth: |
  {chr(10).join('  ' + l if i > 0 else l for i, l in enumerate(inc['truth'].strip().splitlines()))}
era_active: {inc['era']}
settlement: chiayi_city
scope:
{scope_lines}
clues:
{chr(10).join(clue_lines)}
completion_reward:
  exp: {inc['reward']['exp']}
  faction: {inc['reward']['faction']}
  reputation: {inc['reward']['reputation']}
"""
    write_file(f"{BASE}/incidents/{inc['id']}.yaml", content)

# Write Memories
print("\n=== Memories ===")
for mem in memories:
    content = f"""id: {mem['id']}
title: "{mem['title']}"
era: "{mem['era']}"
evidence_type: "{mem['type']}"
quality: {mem['quality']}
progress: 10
description: |
  {chr(10).join('  ' + l if i > 0 else l for i, l in enumerate(mem['desc'].strip().splitlines()))}
settlement: "{mem['settlement']}"
trigger_site: "{mem['site']}"
conditions: []
"""
    write_file(f"{BASE}/memories/{mem['id']}.yaml", content)

# Write World Events
print("\n=== World Events ===")
for ev in world_events:
    trigger_lines = "\n".join(f"  {k}: {v}" for k, v in ev["trigger"].items())
    affected_lines = "\n".join(f"  - {s}" for s in ev["affected_sites"])
    override_lines = "\n".join(
        f"    {site}: |\n      {desc}" for site, desc in ev.get("site_desc_override", {}).items()
    )
    content = f"""id: {ev['id']}
name: {ev['name']}
type: {ev['type']}
era_active: {ev.get('era_active') or 'null'}
trigger:
{trigger_lines}
duration_days: {ev['duration_days']}
affected_sites:
{affected_lines}
description: |
  {ev['description']}
effects:
  site_desc_override:
{override_lines if override_lines else '    {}'}
"""
    write_file(f"{BASE}/world_events/{ev['id']}.yaml", content)

print("\nAll done!")
