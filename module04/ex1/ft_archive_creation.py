def create_archive(filename: str, entries: list[str]) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"\nInitializing new storage unit: {filename}")
    vault = open(filename, "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    i = 1
    for entry in entries:
        line = f"[ENTRY {i:03d}] {entry}\n"
        vault.write(line)
        print(f"[ENTRY {i:03d}] {entry}")
        i = i + 1
    vault.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


def main() -> None:
    filename = "new_discovery.txt"
    entries = [
        "New quantum algorithm discovered",
        "Effieciency increased by 347%",
        "Archived by Data Archivit trainee",
    ]
    create_archive(filename, entries)


if __name__ == "__main__":
    main()
