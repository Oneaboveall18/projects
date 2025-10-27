# 🎯 Project: Anime Info Generator (Python)

## 🧩 Objective

Build a simple **Anime Info Generator** that fetches and displays anime data from the **Jikan API** using **Object-Oriented Programming (OOP)** principles.

### 🧠 Learning Focus

* Making API requests using the `requests` library
* Parsing and handling JSON responses
* Using OOP (classes, methods, and objects) in Python
* Writing clean, readable, and modular code


## 🧱 Requirements

### 1. Use OOP Concepts

* Create a class named **`AnimeInfo`**
* Implement an `__init__` constructor that stores API URLs
* Define at least **three methods**:

  * `get_popular_all_time()` → Fetch top 10 anime of all time
  * `get_popular_airing()` → Fetch top 10 currently airing anime
  * `parse_data()` → Extract and format the required anime fields
* Use an additional `display_info()` method to print results neatly


### 2. Use the `requests` Package

* Use the **`requests`** library to make API calls.
* Check for `status_code == 200` before processing data.
* Gracefully handle failed requests with user-friendly messages.


### 3. API Endpoints

| Type                 | Endpoint                                                                    |
| -------------------- | --------------------------------------------------------------------------- |
| **Popular All Time** | `https://api.jikan.moe/v4/anime?order_by=popularity&limit=10`               |
| **Popular Airing**   | `https://api.jikan.moe/v4/anime?order_by=popularity&limit=10&status=airing` |


### 4. Display Output

For each anime, print the following details:

* **ID**
* **English Title**
* **Japanese Title**
* **Score**
* **Studio** (if available)
* **Website URL**

---

### 🧾 Example Output

```
Anime Info Generator
1. Popular All Time
2. Popular Airing
Enter your choice: 1

ID: 5114
Title: Fullmetal Alchemist: Brotherhood
Japanese Title: 鋼の錬金術師 FULLMETAL ALCHEMIST
Score: 9.12
Studio: Bones
Website: https://myanimelist.net/anime/5114
--------------------
ID: 11061
Title: Hunter x Hunter (2011)
Japanese Title: HUNTER×HUNTER（2011）
Score: 9.05
Studio: Madhouse
Website: https://myanimelist.net/anime/11061
--------------------
```

## ▶️ How to Run

1. Make sure Python is installed (`python --version`).
2. Install dependencies:

   ```bash
   pip install requests
   ```
3. Run the script:

   ```bash
   python main.py
   ```
4. Choose between:

   * `1` → Popular All Time
   * `2` → Popular Airing
