# workplace-buddy-assistant
South African workplace AI assistant for tax queries, salary calculations, labour laws, and meeting notifications.
# Work Buddy Assistant

## Overview
Work Buddy Assistant is a South African workplace AI agent designed to help employees with:
- Tax queries (via SARS integration)
- Labour law guidance (via Department of Labour resources)
- Salary calculations (hourly, daily, weekly, monthly, annual)
- Meeting notifications and a notice board for managers

Built as part of the Microsoft Founderz 90‑minute build challenge.

---

## Features
- **Tax Laws (SARS)**: Fetches latest tax rates and thresholds from SARS.
- **Labour Laws**: Provides workplace rights, leave policies, and minimum wage info.
- **Salary Calculator**: Simple function to calculate earnings based on hours and rate.
- **Messaging Service**: Managers can post announcements; employees can view them.

---

## Tech Stack
- Python
- Flask (for API + front-end)
- Requests + BeautifulSoup (for scraping SARS and Labour info)

---

## Endpoints
- `GET /tax` → Returns SARS tax info
- `GET /labour` → Returns Labour law info
- `POST /salary` → Calculate salary (JSON: {"hours":8,"rate":100,"period":"daily"})
- `POST /messages` → Post a message (JSON: {"manager":"Manager A","message":"Team meeting at 10 AM"})
- `GET /messages` → View all messages

---

## Demo Instructions
1. Clone repo
2. Install dependencies:
