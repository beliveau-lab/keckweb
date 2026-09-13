# 快速开始指南

## 🔴 重要提示

**千万不要** 直接双击HTML文件打开！这样导航链接不会工作。

你必须通过本地Web服务器来运行网站。

## ✅ 正确的启动方法

### 方法1：最简单（推荐）

#### Windows 用户：
1. 将所有文件保存到一个文件夹
2. 找到 `start_server.bat` 文件
3. **双击** `start_server.bat`
4. 网站会自动在浏览器中打开 👍

#### Mac 用户：
1. 将所有文件保存到一个文件夹
2. 打开 "终端" (Terminal)
3. 输入命令：`bash start_server.sh`
4. 回车，网站自动在浏览器中打开

#### Linux 用户：
1. 将所有文件保存到一个文件夹
2. 打开终端
3. 进入文件夹：`cd /path/to/folder`
4. 运行：`bash start_server.sh`
5. 网站自动在浏览器中打开

### 方法2：手动启动服务器

#### Windows（命令提示符）：
```
# 进入文件夹
cd C:\Users\YourName\Downloads\keck-website

# 启动服务器
python -m http.server 8000
```

#### Mac/Linux（终端）：
```bash
# 进入文件夹
cd ~/Downloads/keck-website

# 启动服务器
python3 -m http.server 8000
```

然后在浏览器打开：**http://localhost:8000**

## 🎯 现在你会看到：

✅ Home 导航链接可以点击
✅ Equipment 导航链接可以点击
✅ Services & Rates 导航链接可以点击
✅ Schedule 导航链接可以点击（打开预约表单）
✅ Policies 导航链接可以点击
✅ Contact 导航链接可以点击
✅ Email 按钮可以点击
✅ 所有链接都能正常跳转

## ❓ 常见问题

**Q: 我应该使用哪个Python版本？**
A: Python 3 (推荐)。如果没有 Python 3，用 Python 2 也可以。

**Q: 服务器启动后浏览器没有自动打开怎么办？**
A: 手动在浏览器地址栏输入：http://localhost:8000

**Q: 怎样停止服务器？**
A: 按下 **Ctrl + C** (在终端/命令提示符中)

**Q: 如果提示"端口8000被占用"怎么办？**
A: 改用其他端口，例如：`python3 -m http.server 8001`

**Q: 为什么不能直接打开HTML文件？**
A: 浏览器的安全限制。相对路径（../index.html）只能在HTTP服务器上工作，不能用 file:// 协议。

## 🚀 开始使用

选择上面的任意一种方法启动网站，现在所有导航链接都应该能正常工作了！
