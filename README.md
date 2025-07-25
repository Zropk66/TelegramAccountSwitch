# Telegram Account Switcher (TAS) 🔄

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Version](https://img.shields.io/badge/Version-114514-brightgreen)

智能管理Telegram多账户的桌面工具，通过自动化`tdata`目录操作实现秒级账户切换

## ✨ 核心功能

- 🚀 **一键式账户切换** - 通过命令行参数快速切换指定账户
- 🖥 **可视化配置** - 基于PySide6的GUI设置界面
- 📡 **实时进程监控** - 持续检测客户端运行状态
- 🛡 **数据保护** - 异常退出时自动恢复原始配置
- 📊 **日志系统** - 详细记录运行日志（`TAS.log`）

## 📦 安装指南

### 环境要求

- Python 3.8+
- Windows 10/11
- .NET Framework 4.8+

```bash
# 克隆仓库
git clone https://github.com/Zropk66/TelegramAccountSwitch.git
cd TelegramAccountSwitch

# 安装依赖
pip install -r requirements.txt

# 编译命令
nuitka --mingw64 --assume-yes-for-downloads --show-progress --show-memory --standalone --onefile --windows-console-mode=disable --plugin-enable=pyside6 --output-filename=TAS --output-dir=output --remove-output --lto=yes --jobs=8 .\launcher.py
```

## 🚀 使用指南

### 命令行参数

| 长参数          | 短参数    | 说明        |
|:-------------|:-------|:----------|
| --version    | -v     | 获取当前版本    |
| --settings   |        | 打开可视化设置窗口 |
| --switch TAG | -s TAG | 切换指定标签的账户 |
| --help       | -h     | 获取帮助文档    |

### 使用示例

```textmate
# 目录结构(例)
Telegram/
├── tdata/          # 账户1
│   └── main        # 主标签标识文件
│   └── xxx
├── tdata1/         # 账户2
│   └── t1          # t1标签
│   └── xxx
├── tdata2/         # 账户3
│   └── t2          # t2标签 
│   └── xxx
└── order files

# 登录默认账户
python main.py

# 登录标签为"t1"的账户
python main.py -s t1

# 打开设置界面
python main.py --settings
```

## ⚙️ 配置说明

### 首次运行会自动生成configs.json, 并会自动打开设置界面, 您需要配置以下参数：

```json
{
  "client": "Telegram.exe",
  "path": "C:/Path/To/Telegram",
  "default": "main",
  "tags": [
    "t1",
    "t2"
  ],
  "log_output": true
}
```

## 🛡️ 进程守护

- **实时监控**: 每秒检测客户端进程状态，异常退出时自动触发恢复机制.
- **异常处理**: 客户端崩溃后自动执行：
    - 🧹 清理残留进程.
    - 🔙 自动恢复默认账户.
    - 📝 记录日志（`TAS.log`).

## 👓 作者声明

- **超低占用**: 在后台监控进程启动的情况下占用不超过40MB, 设置界面不超过70MB.
- **离线应用**: 软件不与任何服务器连接，也不访问任何网络，纯本地运行.

## ⚠️ 注意事项

1. 首次使用前需通过设置界面设置必要参数.
2. 建议通过设置界面管理账户标签.
3. 必须手动在账户文件夹中创建标签文件.

## 💖 贡献指南

热烈欢迎任何形式的贡献！无论是代码改进、文档修正还是新功能建议，你的贡献都将使项目变得更好。

### 提交问题

如果您遇到任何错误或问题，请：

1. 在 [Issues 页面](https://github.com/Zropk66/TelegramAccountSwitch/issues) 查看是否已有相关讨论
2. 若不存在类似问题，请[新建 Issue](https://github.com/Zropk66/TelegramAccountSwitch/issues/new/choose) 并清晰描述：
    - 遇到的问题现象
    - 复现步骤
    - 期望结果
    - 环境信息（如系统版本、依赖版本等）

**我会尽快响应并解决！**

### 代码贡献

想贡献代码？请按以下流程：

```bash
# 1. Fork 本仓库
# 2. 创建新分支（推荐使用功能描述命名）：
git checkout -b feature/your-feature

# 3. 提交代码变更
git commit -m "feat: 添加了新功能"

# 4. 推送分支到你的 Fork：
git push origin feature/your-feature

# 5. 提交 Pull Request 到本仓库的 main 分支
```