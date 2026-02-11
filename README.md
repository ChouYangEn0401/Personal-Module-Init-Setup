# Python Project Starter Template

[English] | [繁體中文](README.zh-TW.md)

## Description
This repository provides a ready-to-use **Python Template** for quickly starting new projects.  
It is designed as a public starter template that can be cloned or downloaded to immediately begin development with minimal setup.

---

## Initialization Options

This template provides several **pre-configured setups** for different project types. Each setup is available in a separate branch.

### 1. Basic Project Initialization
Quickly set up a minimal Python project structure.

- **Test-Driven Design (TDD)**  
  Supports unit testing and test-first development.
- **Class Skeleton (Framework-Based Classing)**  
  Provides a minimal class-based structure. Does **not** include a framework, making it easy to dev new framework or build mvp model later.
- **Framework-Based Classing**:
  Provides a class-based structure under ISDFramework

### 2. Toolkit Initialization
Prepare a project that can be packaged and installed via `pip`.

### 3. Strangler Pattern Initialization
Useful for gradually replacing legacy features with new implementations.

### 4. AI/ML Project Initialization
Fast setup for AI/ML projects, including example scripts and environment configuration.

### 5. Other Skeletons
Additional templates for specialized use cases:

- **Microservice Skeleton**: Suitable for breaking a system into smaller services.
- **CLI Tool Skeleton**: For creating command-line interface tools.
- **Web App Skeleton**: Minimal web app structure using Flask or FastAPI.

---

## Available Branches

| 開發狀況              | 期待功能                                                    | branch         | 說明                                                          |
|-------------------|---------------------------------------------------------|----------------|-------------------------------------------------------------|
| RELEASE           | Toolkit Initialization                                  | `toolkit`      | 可打包成 pip 套件的專案模板                                            |
| dev               | Basic Project Initialization - Class Skeleton           | `basic-class`  | 最小 class 架構，未套入框架                                           |
| dev               | Basic Experimental Project Initialization - Facade Init | `exp-facade`   | 透過基本的Pattern快速建立最基本的實驗運作流程（Facade/Adapter/Strategy/Inherit） |
| ***legacy***      | AI/ML Project Initialization                            | `ai`           | 包含 AI/ML 範例與環境配置                                            |
| ***legacy***      | A Basic Tkinter Init Pack With Framework Built In       | `tkinter-pack` | 引用部分 ISDFramework 的架構，專門為了 tkinter 工具而開發的底層   |
| ***todo***        | Basic Project Initialization - TDD                      | `basic-tdd`    | 單純 Python 專案 + 測試先行設計                                       |
| ***todo***        | Basic Project Initialization - Framework-Based Classing | `basic-isd`    | 最小 class 架構，套入 `ISDFramework` 框架                            |
| **~~hault~~**     | Strangler Pattern Initialization                        | `strangler`    | 漸進取代舊系統的模式                                                  |
| **~~hault~~**     | Microservice Skeleton                                   | `microservice` | 適合拆小服務的專案骨架                                                 |
| **~~hault~~**     | CLI Tool Skeleton                                       | `cli`          | 建立命令列工具的專案模板                                                |
| **~~hault~~**     | Web App Skeleton                                        | `web`          | 最基本的 Web 專案結構（Flask/FastAPI）                                |

---

## Recommended Usage
- If you want a **Simple Starting Proj**, use the **basic-class** branch.
- For **AI/ML projects**, use the **ai** branch.
- Dealing with mvp/experiment, **exp-facade** branch just where to go.
- As For GUI Tkinter Project, **tkinter-pack** branch will be your best option.
- For projects that require **Test Driven Design**, use the **basic-tdd** branch.
- For gradually modernizing legacy code and do old-new-feature switch, use the **strangler** branch.
- Other specialized projects can use the **Microservice**, **CLI**, or **Web** branches.

---

## Getting Started
1-\[method1\]. **Clone the repository**:
 ```bash
 git clone <repo-url>
 cd <repo-folder>
````
1-\[method2\]. **Clone the repository**:
```bash
 git clone -b <branch-name> <repo-url>
 cd <repo-folder>
````

2. Switch to the desired branch:
```bash
git checkout <branch-name>
```
3. Install dependencies (if applicable) (Make Sure VirtualEnvironment Is Built First !!):
```bash
pip install -r requirements.txt
```
4. Start Developing and Enjoy !

