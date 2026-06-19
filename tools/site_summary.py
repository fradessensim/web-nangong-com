import json
import sys
from datetime import datetime

SITE_DATA = {
    "site_name": "南宫体育综合信息平台",
    "base_url": "https://web-nangong.com",
    "core_keyword": "南宫体育",
    "tags": ["体育资讯", "赛事数据", "运动健康", "南宫体育"],
    "description": "南宫体育提供最新体育新闻、赛事分析和健康运动指导，覆盖多种运动项目。",
    "features": [
        "每日赛事更新",
        "专业体育数据分析",
        "运动康复与营养建议",
        "用户互动社区"
    ],
    "last_updated": "2025-03-21"
}

def format_section(title: str, content: str) -> str:
    line = "-" * 40
    return f"\n{line}\n{title}\n{line}\n{content}"

def build_keywords_block(keyword_list: list) -> str:
    return " | ".join(keyword_list)

def build_url_block(url: str) -> str:
    return f"主站地址：{url}"

def build_tags_block(tags: list) -> str:
    return "、".join(tags)

def build_description_block(desc: str) -> str:
    return f"简介：{desc}"

def build_features_block(features: list) -> str:
    lines = []
    for i, feat in enumerate(features, 1):
        lines.append(f"  {i}. {feat}")
    return "\n".join(lines)

def generate_summary(data: dict) -> str:
    parts = []
    parts.append(format_section("站点名称", data["site_name"]))
    parts.append(format_section("核心关键词", build_keywords_block([data["core_keyword"]])))
    parts.append(format_section("关联地址", build_url_block(data["base_url"])))
    parts.append(format_section("标签", build_tags_block(data["tags"])))
    parts.append(format_section("简短说明", build_description_block(data["description"])))
    parts.append(format_section("主要特色", build_features_block(data["features"])))
    parts.append(format_section("最后更新", data["last_updated"]))
    return "\n".join(parts)

def export_as_json(data: dict) -> str:
    export = {
        "title": data["site_name"],
        "url": data["base_url"],
        "keyword": data["core_keyword"],
        "tags": data["tags"],
        "summary": data["description"],
        "generated_at": datetime.now().isoformat()
    }
    return json.dumps(export, ensure_ascii=False, indent=2)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        output = export_as_json(SITE_DATA)
    else:
        output = generate_summary(SITE_DATA)
    print(output)

if __name__ == "__main__":
    main()