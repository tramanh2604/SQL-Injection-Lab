# SQL-Injection-Lab - Web Application Security

A deliberately vulnerable web application demonstrating various SQL injection techniques and PostgreSQL RCE escalation.

## 🚀 Project Overview
This lab contains multiple vulnerability levels designed topractice SQL injection attacks in a safe, controlled environment. The application is built with PHP + PostgreSQL and containerized with Docker.

## 🎯 Lab Levels
| Level | Vulnerability Type | Techniques Demonstrated |
|-------|-------------------|------------------------|
| 1 | Error-Based | Basic injection, error extraction |
| 2 | Union-Based | Data extraction via UNION queries |
| 3 | Boolean-Based Blind | Conditional responses, binary search |
| 4 | Time-Based Blind | Timing attacks, conditional delays |
| 5 | SQLi to RCE | PostgreSQL privilege escalation, file write |

## 🛠️ Tech Stack

- **Backend**: PHP 8.x
- **Database**: PostgreSQL 14
- **Containerization**: Docker + Docker-compose
- **Automation**: Python (for attack scripts)

## 📚 Full Writeup on Notion
[Write-up on Notion](https://www.notion.so/SQL-INJECTION-WRITEUP-29d991c9962d80a4a714d58152fc1d0f?source=copy_link)
___
**Fire up the lab and happy hacking!** 🔥
