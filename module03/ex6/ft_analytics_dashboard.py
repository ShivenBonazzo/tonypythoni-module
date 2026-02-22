def main() -> None:
    """Main entry point."""

    players_data: list = [
        {"name": "alice", "score": 2300, "active": True,
         "region": "north", "achievements": 5},
        {"name": "bob", "score": 1800, "active": True,
         "region": "east", "achievements": 3},
        {"name": "charlie", "score": 2150, "active": True,
         "region": "central", "achievements": 7},
        {"name": "diana", "score": 2050, "active": False,
         "region": "north", "achievements": 4},
        {"name": "eve", "score": 1500, "active": False,
         "region": "east", "achievements": 2},
        {"name": "frank", "score": 900, "active": True,
         "region": "central", "achievements": 1},
    ]

    achievements_data: list = [
        {"player": "alice", "achievement": "first_kill"},
        {"player": "bob", "achievement": "level_10"},
        {"player": "charlie", "achievement": "boss_slayer"},
        {"player": "alice", "achievement": "level_10"},
        {"player": "diana", "achievement": "first_kill"},
        {"player": "charlie", "achievement": "first_kill"},
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers: list = [
        p["name"] for p in players_data if p["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    doubled: list = [
        p["score"] * 2 for p in players_data if p["score"] > 2000
    ]
    print(f"Scores doubled: {doubled}")

    active_players: list = [
        p["name"] for p in players_data if p["active"]
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict = {
        p["name"]: p["score"] for p in players_data
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict = {
        "high": len([p for p in players_data if p["score"] >= 2000]),
        "medium": len([p for p in players_data if 1500 <= p["score"] < 2000]),
        "low": len([p for p in players_data if p["score"] < 1500])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict = {
        p["name"]: p["achievements"] for p in players_data
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    unique_players: set = {p["name"] for p in players_data}
    print(f"Unique players: {unique_players}")

    unique_achievements: set = {
        a["achievement"] for a in achievements_data
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set = {
        p["region"] for p in players_data if p["active"]
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players: int = len(unique_players)
    print(f"Total players: {total_players}")

    total_achievements: int = len(unique_achievements)
    print(f"Total unique achievements: {total_achievements}")

    scores: list = [p["score"] for p in players_data]
    average: float = sum(scores) / len(scores)
    print(f"Average score: {average}")

    top: dict = sorted(
        players_data,
        key=lambda p: p["score"],
        reverse=True
    )[0]
    print(
        f"Top performer: {top['name']} "
        f"({top['score']} points, {top['achievements']} achievements)"
    )


if __name__ == "__main__":
    main()