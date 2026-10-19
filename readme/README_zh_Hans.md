# Kimi Code 的 Suno by Ace Data Cloud 插件

独立安装Suno音乐服务，不改变聊天模型。由 **Ace Data Cloud** 提供，非Suno或Moonshot官方产品。独立发布v0.1.0；尚未进入Kimi官方/精选目录。

## 1. 在Kimi安装

在Kimi Code 2.2.0或更新版本的终端输入：

```text
/plugins install https://github.com/AceDataCloud/SunoKimiCode/releases/tag/v0.1.0
```

此命令安装固定v0.1.0发行版。查看源码和第三方信任提示后自行选择Trust and install；随后`/reload`或`/new`。独立发行不等于Kimi官方上架。

## 2. 注册并获取Token

打开[Ace应用列表](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_key_zh)，先注册或登录。找到General application，没有则Initialize General Application。检查Suno权限、余额与[当前价格](https://platform.acedata.cloud/models?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_pricing_zh)。复制API Key，或Manage Keys → Create，创建名为Kimi Code Suno的专用Token。检查过期时间、用量限制和Allowed APIs；按需允许/suno/audios, /suno/tasks。任务查询权限不等于生成权限。

![复制已遮盖的Key或进入Manage Keys](../assets/tutorial/get-api-key-en.png)

![单独创建Key；名称改为Kimi用途](../assets/tutorial/create-api-key-en.png)

截图复用既有Ace Dify教程，拍摄时间未提供，原示例名称为Dify tutorial；请改为自己的Kimi名称。不要复制遮盖字符或Bearer前缀，也不要用platform管理Token。

## 3. Token放在哪里

在启动Kimi的同一个终端环境中设置`ACEDATACLOUD_API_TOKEN`。macOS/Linux可隐藏输入：

```bash
read -r -s ACEDATACLOUD_API_TOKEN
export ACEDATACLOUD_API_TOKEN
kimi
```

PowerShell 7.1+使用`$env:ACEDATACLOUD_API_TOKEN = Read-Host -MaskInput`后运行`kimi`。此变量由原生manifest的`bearerTokenEnvVar`读取，不能写在聊天或仓库中。此路径不进行OAuth登录。

## 4. 首用与同ID查询

先`/suno-by-ace:check`；只列模型，不调用媒体生成。

已有任务直接`/suno-by-ace:status 原任务ID`。新请求用`/suno-by-ace:create 需求`准备参数，核对模型、价格和具体费用授权后才提交一次。保存返回task_id；pending时只查同一ID，不重新生成。以工具的终态成功/失败标记及最终媒体URL为准，不能把任务受理当完成。

401/403检查Key和权限，429等待降并发，失败/超时先查旧任务。不要自动付费重试或擅自替换模型。素材调用和编排LLM可能分别计费；安装本身不代表免费生成。本仓不声称已完成真实媒体、终态账单或营收验收。

现有托管端点`https://suno.mcp.acedata.cloud/mcp`，复用[SunoMCP](https://github.com/AceDataCloud/SunoMCP)，不复制服务实现。详见[英文完整指南](../README.md)、[来源](../assets/tutorial/sources.json)与[服务文档](https://platform.acedata.cloud/documents/suno-audios?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=suno_kimi_readme_docs_zh)。
