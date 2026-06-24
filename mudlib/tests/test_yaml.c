// /tests/test_yaml.c
inherit "/std/test_case";

void run_tests(object me) {
    start_test("YAML 序列化與反序列化 (yaml_decode & yaml_encode)");

    // 1. 測試基礎 yaml_decode
    string yaml_str = 
        "name: \"民雄\"\n" +
        "population: 1200\n" +
        "culture: 42\n" +
        "industry:\n" +
        "  - \"鳳梨\"\n" +
        "  - \"糖業\"\n" +
        "enabled: true\n";

    mixed data = yaml_decode(yaml_str);
    assert_equal(1, mapp(data), "解碼結果應該是 Mapping");
    assert_equal("民雄", data["name"], "解碼名稱欄位");
    assert_equal(1200, data["population"], "解碼整數欄位");
    assert_equal(42, data["culture"], "解碼整數文化值");
    assert_equal(1, arrayp(data["industry"]), "解碼列表欄位為陣列");
    assert_equal(2, sizeof(data["industry"]), "陣列長度為 2");
    assert_equal("鳳梨", data["industry"][0], "解碼陣列元素 0");
    assert_equal("糖業", data["industry"][1], "解碼陣列元素 1");
    assert_equal(1, data["enabled"], "解碼布林值為 1 (true)");

    // 2. 測試 yaml_encode
    mapping test_map = ([
        "id": "tainan",
        "culture": 99,
        "features": ({ "古蹟", "小吃" })
    ]);
    string encoded = yaml_encode(test_map);
    mixed decoded = yaml_decode(encoded);

    assert_equal(1, mapp(decoded), "再次解碼後應為 Mapping");
    assert_equal("tainan", decoded["id"], "再次解碼的 id 欄位");
    assert_equal(99, decoded["culture"], "再次解碼的 culture 欄位");
    assert_equal(2, sizeof(decoded["features"]), "再次解碼的 features 長度");
    assert_equal("古蹟", decoded["features"][0], "再次解碼的 features 元素 0");

    report_results();
}
