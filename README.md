# 🎯 Project: Anime Info Generator (Python)

## 🧩 Objective

Build a simple **Anime Info Generator** that fetches and displays anime data from the **Jikan API** using **object-oriented programming (OOP)** principles.

### 🧠 Learning Focus

- API handling using the `requests` library
- Working with JSON data
- Applying OOP concepts (classes, methods, objects)
- Clean and readable code design

---
## 🧱 Requirements

1. **Use OOP Concepts**
    
    - Create a class named `AnimeInfoGenerator`
    - Define an `__init__` method and at least **two methods**:
        - `get_popular_all_time()`
        - `get_popular_airing()`
    - Each method should make an API request and display anime details.
        
2. **Use the `requests` Package**
    - Handle the API call using the `requests` library.
    - Manage errors gracefully (e.g., invalid response or connection issues).
        
3. **API Endpoints**
    - **Popular All Time:**  
        https://api.jikan.moe/v4/anime?order_by=popularity&limit=10
    - **Popular Airing:**  
        https://api.jikan.moe/v4/anime?order_by=popularity&limit=10&status=airing
        
4. **Display Output**  
    For each anime, print the following details:
    - ID
    - Japanese Title
    - English Title
    - Score
    - Studio Name (if available)
    - Official Website URL (if available)
    
Example output format:
```
ID: 30030303
Japanese Title: 鋼の錬金術師 FULLMETAL ALCHEMIST
English Title: Fullmetal Alchemist: Brotherhood
Score: 9.12
Studio: Bones
Website: https://www.hagaren.jp/
-----------------------------------
```

---