# palinkeedin

本项目用于从 LinkedIn 上爬取指定搜索词或指定 base（城市/地区）的职位信息，并整理为表格（CSV）。

## 功能
- 输入搜索关键词和 base（可选）
- 登录 LinkedIn（需手动扫码或输入账号密码）
- 爬取职位信息：公司、职务、JD 描述、招聘链接
- 输出为 CSV 表格

## 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法
1. 启动脚本：
   ```bash
   python main.py
   ```
2. 按提示输入搜索关键词和 base
3. 浏览器会自动打开，请手动登录 LinkedIn
4. 登录后程序会自动开始爬取
5. 结果保存在 `output/jobs.csv`

## 注意事项
- LinkedIn 反爬较强，建议低频率抓取，避免账号被封
- 建议使用自己的 LinkedIn 账号登录
- 本项目仅供学习交流，勿用于商业用途 