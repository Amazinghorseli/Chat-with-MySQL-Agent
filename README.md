# 📊 AI 智能 MySQL 数据分析助手

这是一个基于 **FastAPI + LangChain + DeepSeek + MySQL** 打造的低延迟、全栈 Text-to-SQL 智能数据分析系统。用户可以使用自然语言（人话）直接对数据库进行查询，AI 会自动思考、生成并执行 SQL，最终返回可视化结果。

## 🚀 技术栈
- **后端框架**: FastAPI (Python 3.10+)
- **大模型编排**: LangChain (ReAct 思考链架构)
- **大模型驱动**: DeepSeek-V3 (通过硅基流动 API 接入)
- **数据库**: MySQL 8.0+
- **环境管理**: uv (现代化高效包管理器)
- **前端交互**: HTML5 + Tailwind CSS + Vanilla JS

## 📦 本地快速部署
1. 安装依赖：`uv pip install -r requirements.txt` (若有)
2. 配置项目根目录下的 `.env` 文件：
   ```env
   OPENAI_API_KEY=your_siliconflow_key
   OPENAI_API_BASE=[https://api.siliconflow.cn/v1](https://api.siliconflow.cn/v1)
   DB_PASSWORD=your_mysql_password