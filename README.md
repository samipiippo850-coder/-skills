# 📘 Universal Academic Skill — 通用学科学习系统

**通用的学科学习框架与辅助工具合集**  
帮助学习者系统整理教材与专家资源、分析前沿论文、提炼核心思维模型，并通过实践习题和反思日志深化理解。

---

## 🧠 项目简介

这个仓库提供一套通用的学习 Skill 体系，配合自动化脚本，可用于：

- 📚 教材与资源整理  
- 📄 前沿论文抓取与摘要  
- 🧩 思维模型与跨学科思考  
- ❓ 苏格拉底式理解提问  
- 📝 自动生成练习题模板

目标是让你“真正理解而非记忆”，提升学习效率和批判性思维能力。

---

## 🚀 快速开始

### 📦 依赖安装

确保你已安装 Python 3.8+，然后在项目根目录执行：

```bash
pip install -r requirements.txt

📂 项目结构说明

├── README.md                       # 当前文件
├── UNIVERSAL_ACADEMIC_SKILL.md     # 通用 Skill 主文档
├── requirements.txt                # Python 依赖清单
├── build_docs.sh                   # 导出 Markdown 为 PDF/Word 脚本
├── fetch_books.py                  # 教材抓取脚本
├── auto_summary.py                 # 摘要提取脚本
├── fetch_openalex.py               # OpenAlex 论文查询脚本
├── generate_quiz.py                # 练习题生成脚本
├── LICENSE                         # 开源许可（MIT）
└── outputs/                        # 自动生成输出产物

📌 抓取教材列表
python fetch_books.py
📌 自动生成文章/论文摘要
python auto_summary.py
📌 OpenAlex 论文元数据查询
python fetch_openalex.py
📌 生成理解检验题模板
python generate_quiz.py
📌 导出为 PDF/Word 文档
bash build_docs.sh

⚠️ build_docs.sh 需要安装 Pandoc + LaTeX 才能生成 PDF。

📘 License

本项目采用 MIT License，详见 LICENSE。

🙌 贡献与反馈

欢迎大家提出建议、贡献脚本或完善 Skill 内容！
请通过创建 Issue / Pull Request 参与本项目发展。


---
