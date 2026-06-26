# -*- coding: utf-8 -*-
import unittest
import os
import subprocess
import shutil

class TestNewSiteScaffold(unittest.TestCase):
    def setUp(self):
        self.project_root = os.path.abspath(os.path.dirname(__file__))
        self.script_path = os.path.join(self.project_root, "bin", "new-site")
        self.test_settlement = "minxiong"
        self.test_site = "police_dormitory_test_scaffold"
        self.test_site_id = f"{self.test_settlement}_{self.test_site}"

    def tearDown(self):
        # 清除測試產生的檔案
        site_file = os.path.join(self.project_root, "mudlib", "data", "yaml", "sites", self.test_settlement, f"{self.test_site_id}.yaml")
        mem_file = os.path.join(self.project_root, "mudlib", "data", "yaml", "memories", f"{self.test_site_id}_001.yaml")
        if os.path.exists(site_file):
            os.remove(site_file)
        if os.path.exists(mem_file):
            os.remove(mem_file)

    def test_scaffold_generation(self):
        # 執行 new-site 腳本
        cmd = [self.script_path, self.test_settlement, self.test_site]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        self.assertEqual(res.returncode, 0, f"腳本執行失敗: {res.stderr}")
        
        # 驗證 Site YAML 生成與欄位
        site_file = os.path.join(self.project_root, "mudlib", "data", "yaml", "sites", self.test_settlement, f"{self.test_site_id}.yaml")
        self.assertTrue(os.path.exists(site_file), "Site YAML 檔案應被建立")
        
        with open(site_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(f"id: {self.test_site_id}", content)
            self.assertIn(f"settlement: {self.test_settlement}", content)
            self.assertIn("base_description:", content)

        # 驗證 Memory YAML 生成與欄位
        mem_file = os.path.join(self.project_root, "mudlib", "data", "yaml", "memories", f"{self.test_site_id}_001.yaml")
        self.assertTrue(os.path.exists(mem_file), "Memory YAML 檔案應被建立")
        
        with open(mem_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(f"id: {self.test_site_id}_001", content)
            self.assertIn(f"trigger_site: \"{self.test_site_id}\"", content)

if __name__ == "__main__":
    unittest.main()
