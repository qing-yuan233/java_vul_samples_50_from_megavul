import json
from pathlib import Path

with Path("java_vul_samples_50.json").open("r", encoding="utf-8") as f:
    java_vul_samples_50 = json.load(f)

    # 打印1个漏洞代码样本
    item = java_vul_samples_50[0]
    print(f"Java vulnerability code： {item['func_before']}")

    