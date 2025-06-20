# Telegram Account Switcher (TAS) 🔄

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Version](https://img.shields.io/badge/Version-114514-brightgreen)

智能管理Telegram多账户的桌面工具，通过自动化`tdata`目录操作实现秒级账户切换

## ✨ 核心功能

- 🚀 **一键式账户切换** - 通过命令行参数快速登录指定账户
- 🔒 **安全备份机制** - 自动备份原始tdata目录
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
| 参数           | 说明          |
|--------------|-------------|
| --version    | 获取当前版本      |
| --settings   | 打开可视化设置窗口   |
| --login TAG  | 使用指定标签的账户登录 |
| --help       | 显示帮助文档      |

### 使用示例
```bash
# 目录结构(例)
Telegram/
├── tdata/          # tdata
│   └── main        # 主标签标识文件
│   └── xxx
├── tdata1/         # tdata1
│   └── t1          # t1标签
│   └── xxx
├── tdata2/         # tdata2
│   └── t2          # t2标签 
│   └── xxx
└── order files

# 登录默认账户
python main.py

# 登录标签为"t1"的账户
python main.py --login t1

# 打开设置界面
python main.py --settings
```

## ⚙️ 配置说明

### 首次运行会自动生成configs.json，或通过设置界面配置以下参数：
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

- **实时监控**：每秒检测客户端进程状态，异常退出时自动触发恢复机制
- **异常处理**：客户端崩溃后自动执行：
  - 🧹 清理残留进程（自动终止关联进程）  
  - 🔙 恢复原始tdata配置（从备份目录还原）
  - 📝 记录错误日志（`TAS.log`)

## ⚠️ 注意事项

1. 首次使用前需通过设置界面配置客户端路径
2. 建议通过设置界面管理账户标签
3. 支持自定义客户端进程检测规则
4. 您必须手动在tdata文件夹中创建标签文件
