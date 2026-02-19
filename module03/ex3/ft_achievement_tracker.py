def find_rare(all_ach: set, players: list) -> set:
    rare: set = set()
    for achievement in all_ach:
        count: int = 0
        i: int = 0
        while i < len(players):
            if achievement in players[i]:
                count += 1
            i += 1
        if count == 1:
            rare.add(achievement)
    return rare


def main() -> None:
    print("=== Achievement Tracker System ===")
    alice: set = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob: set = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set = {"level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    all_ach: set = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_ach}")
    print(f"Total unique achievements: {len(all_ach)}")
    common: set = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common}")
    players: list = [alice, bob, charlie]
    rare: set = find_rare(all_ach, players)
    print(f"Rare achievements (1 player): {rare}")
    alice_bob_common: set = alice.intersection(bob)
    alice_unique: set = alice.difference(bob)
    bob_unique: set = bob.difference(alice)
    print(f"\nAlice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
