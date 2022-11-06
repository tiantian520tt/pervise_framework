# Pervise Framework
![image](https://user-images.githubusercontent.com/64673335/193805503-a2c267c0-8bdf-4c8e-959c-9b0ed98d9555.png)
<br/>
A simple and complete security testing framework
一个简单而完整的安全测试框架

Powered by Python 3.7
动力源自 Python 3.7

# Process
Currently implemented functions:
目前实现的功能：
 - Import the qualified Pervise module, and then allow the user to call it.
 - 调用合格的Pervise模块，并允许用户调用它
 - It supports rich third-party development formats and is easy to be compatible with Pervise, with only minor modifications.
 - 它支持丰富的第三方开发格式，很容易与Pervise兼容，只需稍作修改。
 - Connect remotely to the server running Pervise and perform limited work.
 - 远程连接到运行Pervise的服务器并执行有限的工作。
 - Use the powerful Prepper module to help you manage the host.
 - 使用功能强大的Prepper模块来帮助您管理目标。


# Usage
IDE: Pycharm
Run Pervise.py
Command/Powershell:
python pervise.py
...

# Developer! Read me!!!
If you want to develop modules for Pervise, you should refer to the existing modules. They are easy to understand.
如果你想为Pervise开发模块，你最好参考现有的模块。它们很容易理解。

# Tips
pyinstaller.exe -F --hidden-import requests --hidden-import platform -w .\payload.py
<br/>
Use this pyinstaller command when packaging the Preparer Payload<br/>
打包Preparer Payload时使用此pyinstaller命令

# Update
## 6/11/2022
1. Added "about" user window.
2. Fix bugs.
## 10/7/2022
1. The color display is updated and compatible with the general display on Linux/Windows. The color module has been changed.
![image](https://user-images.githubusercontent.com/64673335/194475448-b28459d5-2757-422f-a79b-d23965986e7c.png)
2. Fix vulnerabilities related to the Prepper Payload. It can now be packaged into an exe for stable use. Please refer to "Tips" for packaging method.
3. Successfully solved the compatibility problem on Windows Server 2012, and successfully compatible with Linux distributions such as Kali Linux/Ubuntu/CentOS, but still does not support systems before Windows Server 2012, which may cause exceptions.
