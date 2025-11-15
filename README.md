# 🔍 Internal Asset Search Dashboard

This is a lightweight, internal web dashboard built with **Flask** and **Pandas** that helps you search for asset data (like IP addresses or hostnames) across multiple Excel or CSV files.

> 🚧 Built for analysts and admins who need fast visibility into decentralized inventory and log data.

---

## 🧩 Problem It Solves

Most organizations store their asset inventories, logging summaries, and IP/hostname mappings across multiple Excel files, systems, or reports. This makes it:

- Hard to **trace a device** by its IP or hostname
- Time-consuming to check if a device is **sending logs**
- Impossible to get a **centralized view** without manually opening and searching every sheet

---

## 💡 What This Dashboard Does

- 📂 Load multiple Excel/CSV files from a central `data/` folder  
- 🔎 Provides a simple web interface to **search assets** by hostname or IP  
- 🧠 Displays matching results with full metadata and source file
- 🛡 Keeps your data internal and secure (no cloud needed)

---

## 🚀 How to Run It

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/internal-asset-search.git
cd internal-asset-search

