import requests


class AnimeInfo:
    def __init__(self):
        self.POPULAR_ALL_TIME = (
            "https://api.jikan.moe/v4/anime?order_by=popularity&limit=10"
        )
        self.POPULAR_AIRING = (
            "https://api.jikan.moe/v4/anime?order_by=popularity&limit=10&status=airing"
        )

    def get_popular_all_time(self):
        response = requests.get(self.POPULAR_ALL_TIME)
        if response.status_code == 200:
            data = response.json()
            parsed_data = self.parse_data(data)
            self.display_info(parsed_data)
        else:
            print("Failed to fetch popular anime.")

    def get_popular_airing(self):
        response = requests.get(self.POPULAR_AIRING)
        if response.status_code == 200:
            data = response.json()
            parsed_data = self.parse_data(data)
            self.display_info(parsed_data)
        else:
            print("Failed to fetch popular airing anime.")

    def parse_data(self, data):
        parsed_data = []

        main_data = data.get("data", [])
        for item in main_data:
            studios = item.get("studios", [])
            studio_name = studios[0]["name"] if studios else "N/A"

            parsed_data.append(
                {
                    "id": item.get("mal_id"),
                    "title": item.get("title_english") or item.get("title"),
                    "japanese_title": item.get("title_japanese"),
                    "score": item.get("score"),
                    "studio": studio_name,
                    "website": item.get("url"),
                }
            )

        return parsed_data

    def display_info(self, data):
        for item in data:
            print(f"ID: {item['id']}")
            print(f"Title: {item['title']}")
            print(f"Japanese Title: {item['japanese_title']}")
            print(f"Score: {item['score']}")
            print(f"Studio: {item['studio']}")
            print(f"Website: {item['website']}")
            print("--------------------")

    def get_info(self):
        print("Anime Info Generator")
        print("1. Popular All Time")
        print("2. Popular Airing")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.get_popular_all_time()
        elif choice == 2:
            self.get_popular_airing()
        else:
            print("Invalid choice.")


c = AnimeInfo()
c.get_info()
