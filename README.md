# devagi-openai
基于DevAGI平台的基础代码

## 使用


#### 第一步：安装所需依赖包

```
pip install -r requirements.txt
```

#### 第二步：重命名配置文件 `.env`

```
mv .env.example .env
```

#### 第三步：更改 `.env` 文件的 key 为自己的在 DevAGI 平台获取的 key

```
OPENAI_API_KEY="sk-KJaw8tpNf1lu3********************q3PcwLUPNZOVXIe7"
OPENAI_API_BASE="https://api.fe8.cn/v1"
```

#### 第四步：运行`index.py`代码