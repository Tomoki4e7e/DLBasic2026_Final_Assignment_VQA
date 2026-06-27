# Pythonで修正するスクリプト

import json

with open("DL_Basic_2026_Spring_Competition_VQA_baseline.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# metadata.widgets を削除
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]
    print("widgets メタデータを削除しました")

with open("DL_Basic_2026_Spring_Competition_VQA_baseline.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("保存完了")
