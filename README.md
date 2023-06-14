# IOS - Whisper - Notion
IOS-Whisper-Notion 是一个用于在苹果手机中使用 Whisper将系统语音备忘录转换为文字并发送到notion中进行整理的工具。用户可以在语音备忘录中分享录音文件，并通过 Whisper 进行语音识别。识别后的文本将自动保存到 iOS 备忘录中或者同步到Notion中进行整理和总结，主要目的是从语音备忘录中提取和组织文本信息。

## 项目概述
该项目使用Whisper将语音备忘录转换为文本，并使用Notion AI整理这些文本。录音信息可能是普通零碎的想法或者会议录音，转录后通过适当的prompt可以直接根据语音片段生成完整的文章或者会议纪要。之所以写了这个小工具是因为发现系统录音中保存了很多平时零散的记录，但是语音信息不方便检索和整理，ps 本项目中的所有代码几乎都由GPT4生成。

## 开始前的准备
需要使用OpenAI的官方API。如果你没有信用卡绑定，可以注册新账号，新账号可以获得5美元的免费额度。在注册接码的时候尽量选择使用不太常见的国家，比如肯尼亚等，亲测可行，注册成本仅需15卢布（不到一块钱）ps: 新账号的5美元额度大概可以转录15小时的音频。

## 使用说明
该项目主要有两种实现方式。

### 方法一：直接使用OpenAI的官方API
这种方法需要有科学上网的环境（也可以通过cloudflare使用自己的域名代理），并且不方便处理转录后的文本。如果希望直接将语音备忘录转录后保存到苹果自带的备忘录，不需要在notion中进行后续处理或者整理进知识库，可以直接使用这种方式，该方式不需要部署任何项目，直接点击下面的shortcuts链接就可以。

### 方法二：使用Vercel搭建服务
这种方法可以实现Whisper转录和Notion保存。该方式需要部署这个项目。

## 部署

1. 注册一个 OpenAI 账户并获取 API 密钥。
2. 使用以下链接下载并安装 Shortcuts：Shortcuts 链接
3. 点击以下按钮一键部署    

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FAichaelLee%2Fios-whisper-notion.git&env=DATABASE_ID&env=NOTION_AUTH&env=OPENAI_KEY&env=HEADER_AUTH_PASS&repository-name=ios-whisper-notion)

4. 在 Vercel 中配置环境变量 OPENAI_API_KEY（必需）、NOTION_API_KEY（必需）和HEADER_AUTH_PASS（必需）。
5. 将 Shortcuts 配置为使用你的 Vercel 后端服务地址。
注意：vercel 的自带域名已经被墙，所以需要自己的域名转发或者带梯运行

服务器自部署：
下载之后直接执行main.py即可
需要配置环境变量如下：
```
DATABASE_ID=XXXX // notion database_id 必须
NOTION_AUTH=XXXX // notion auth 必需
OPENAI_KEY=XXXX // openai api key 必需
OPENAI_PROXY=https://yourapiproxy/v1/ // openai 代理 非必需
HEADER_AUTH_PASS=XXXX // 简单的密码验证，用于请求时在header头中添加 必需
TEXT_GPT_PROMPT=你是一个写作大师，基于以下逻辑和观点，拓展出一篇文章，详略有序，有故事有论证 // 使用GPT处理时的初始prompt 非必需
```
## 使用

1. 在语音备忘录中选择要转录的录音文件。
2. 点击分享按钮，然后选择发送到我的 Whisper。
3. 等待 Whisper 转录完成。
4. 如果使用方式一，转录后的文本将自动保存到 iOS 备忘录中，方式二转录后的文本会发送到 Notion 中进行后续的处理。

## 演示


## License
MIT
