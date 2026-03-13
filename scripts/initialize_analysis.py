# filepath: scripts/initialize_analysis.py
import json
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("="*50)
    print("🚀 竞品分析项目初始化工具 v1.0")
    print("="*50)
    print("\n请根据提示完成问卷，我们将为您生成专属的竞品分析计划。\n")

    # 1. 收集品牌信息
    brand_name = input("1. 请输入您的品牌/产品名称 (直接回车跳过): ").strip()
    brand_industry = input("2. 请输入您所在的行业 (例如：SaaS、电商、工具): ").strip()
    
    # 2. 收集竞品信息
    print("\n3. 请输入您要分析的竞品名称（建议3-5个，输入空行结束）：")
    competitors = []
    while True:
        comp = input(f"   竞品 {len(competitors) + 1}: ").strip()
        if not comp:
            if len(competitors) == 0:
                print("   ⚠️ 至少需要输入一个竞品！")
                continue
            break
        competitors.append(comp)

    # 3. 选择分析维度
    print("\n4. 请选择本次分析的重点维度 (输入编号，用逗号分隔，直接回车全选):")
    dimensions_map = {
        "1": "市场现状与行业分析", "2": "竞品背景分析", "3": "产品定位与企业愿景",
        "4": "目标用户分析", "5": "竞品数据分析", "6": "产品与功能分析",
        "7": "运营推广策略分析", "8": "盈利模式分析", "9": "SWOT分析", "10": "结论与建议"
    }
    for k, v in dimensions_map.items():
        print(f"   [{k}] {v}")
    
    selected_dims_input = input("\n   您的选择: ").strip()
    if not selected_dims_input:
        selected_dimensions = list(dimensions_map.values())
    else:
        selected_dimensions = [dimensions_map.get(i.strip()) for i in selected_dims_input.split(',') if i.strip() in dimensions_map]

    # 4. 定义分析目标
    print("\n5. 本次竞品分析的核心目标是什么？")
    goals_map = {
        "1": "融资准备 (重点关注市场规模和差异化)",
        "2": "产品迭代 (重点关注功能体验和用户痛点)",
        "3": "市场进入策略 (重点关注竞争格局和切入点)",
        "4": "运营策略优化 (重点关注获客渠道和转化)"
    }
    for k, v in goals_map.items():
        print(f"   [{k}] {v}")
    goal_input = input("   请选择目标编号: ").strip()
    analysis_goal = goals_map.get(goal_input, "综合深度分析")

    # 生成计划对象
    plan = {
        "project_info": {
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "brand_name": brand_name or "未命名项目",
            "industry": brand_industry
        },
        "analysis_goal": analysis_goal,
        "competitors": competitors,
        "selected_dimensions": selected_dimensions,
        "status": "initialized"
    }

    # 保存计划文件
    output_dir = "outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = f"analysis_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(plan, f, ensure_ascii=False, indent=4)

    print("\n" + "="*50)
    print("✅ 项目初始化完成！")
    print(f"📁 您的分析计划已保存至: {filepath}")
    print("💡 下一步：您可以运行 `generate_excel_templates.py` 生成对应的数据对标表。")
    print("="*50)

if __name__ == "__main__":
    main()