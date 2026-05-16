import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# 1. 自动加载 .env 环境变量
load_dotenv()

# 2. 初始化应用
app = FastAPI(title="AI 智能数据分析助手 (全栈精简版)")

# 3. 数据库与大模型组件初始化
# 老师敲黑板：LangChain 会自动读取环境变量中的 OPENAI_API_KEY 和 OPENAI_API_BASE，无需手动 os.getenv
db_password = os.getenv("DB_PASSWORD", "040817")
db = SQLDatabase.from_uri(f"mysql+pymysql://root:{db_password}@localhost:3306/ai_demo")

llm = ChatOpenAI(model="deepseek-ai/DeepSeek-V3", temperature=0)

# 4. 构建 Agent 智能体
agent_executor = create_sql_agent(
    llm=llm, db=db,
    agent_type="zero-shot-react-description",
    verbose=True, handle_parsing_errors=True
)

# 5. 数据校验模型
class QueryRequest(BaseModel):
    question: str

# =====================================================================
# 6. 路由定义 (极其清爽)
# =====================================================================
@app.get("/")
async def index():
    """直接返回前端网页"""
    return FileResponse("index.html")

@app.post("/api/v1/chat-sql")
async def chat_with_sql(request: QueryRequest):
    """核心 AI 查询接口"""
    try:
        response = await agent_executor.ainvoke({"input": request.question})
        return {"status": "success", "data": {"question": request.question, "answer": response["output"]}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Agent 异常: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)