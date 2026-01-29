# Python Project Starter Template

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

| 開發狀況      | 期待功能                                          | branch         | 說明                                                     |
|-----------| ------------------------------------------------ |----------------|--------------------------------------------------------|
| dev       | Basic Project Initialization - TDD              | `basic-tdd`    | 單純 Python 專案 + 測試先行設計                                  |
| dev       | Basic Project Initialization - Class Skeleton | `basic-class`  | 最小 class 架構，未套入框架                                      |
| dev       | Basic Project Initialization - Framework-Based Classing | `basic-isd`    | 最小 class 架構，套入 `ISDFramework` 框架 |
| release   | Toolkit Initialization           | `toolkit`      | 可打包成 pip 套件的專案模板                                       |
| **hault** | Strangler Pattern Initialization | `strangler`    | 漸進取代舊系統的模式                                             |
| dev       | AI/ML Project Initialization | `ai`           | 包含 AI/ML 範例與環境配置                                       |
| **hault** | Microservice Skeleton | `microservice` | 適合拆小服務的專案骨架                                            |
| **hault** | CLI Tool Skeleton | `cli`          | 建立命令列工具的專案模板                                           |
| **hault** | Web App Skeleton | `web`          | 最基本的 Web 專案結構（Flask/FastAPI）                           |

---

## Recommended Usage
- If you want a **simple starting point**, use the **Class Skeleton** branch.
- For projects that require **TDD**, use the **TDD** branch.
- For gradually modernizing legacy code, use the **Strangler** branch.
- For **AI/ML projects**, use the **AI** branch.
- Other specialized projects can use the **Microservice**, **CLI**, or **Web** branches.

---

## Getting Started

1. **Clone the repository**:
 ```bash
 git clone <repo-url>
 cd <repo-folder>
````

2. Switch to the desired branch:
```bash
git checkout <branch-name>
```
3. Install dependencies (if applicable):
```bash
pip install -r requirements.txt
```
4. Start Developing and Enjoy !

