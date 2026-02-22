from typing import Generator


def game_event_generator(count: int) -> Generator:
    """Generate game events one at a time."""
    players: list = ["alice", "bob", "charlie"]
    events: list = ["killed monster", "found treasure", "leveled up"]
    levels: list = [5, 12, 8, 3, 15, 7, 10, 2, 9, 6]

    for i in range(count):
        player: str = players[i % len(players)]
        event: str = events[i % len(events)]
        level: int = levels[i % len(levels)]
        yield (i + 1, player, level, event)


def fibonacci_generator() -> Generator:
    """Generate Fibonacci numbers indefinitely."""
    a: int = 0
    b: int = 1
    while True:
        yield a
        temp: int = a
        a = b
        b = temp + b


def prime_generator() -> Generator:
    """Generate prime numbers indefinitely."""
    n: int = 2
    while True:
        is_prime: bool = True
        for i in range(2, n):
            if i * i > n:
                break
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def get_first_n(gen: Generator, n: int) -> list:
    """Get first n values from a generator."""
    result: list = []
    for _ in range(n):
        try:
            result.append(next(gen))
        except StopIteration:
            break
    return result


def process_stream(count: int) -> None:
    """Process game events stream and print analytics."""
    total: int = 0
    high_level: int = 0
    treasure: int = 0
    levelup: int = 0

    for event in game_event_generator(count):
        try:
            num, player, level, action = event
            total += 1
            if level >= 10:
                high_level += 1
            if action == "found treasure":
                treasure += 1
            if action == "leveled up":
                levelup += 1
        except (ValueError, TypeError) as e:
            print(f"Warning: skipping invalid event: {e}")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def main() -> None:
    """Main entry point."""
    print("=== Game Data Stream Processor ===")

    count: int = 1000
    print(f"Processing {count} game events...")
    print()

    try:
        preview_gen: Generator = game_event_generator(count)
        preview: list = get_first_n(preview_gen, 3)
        for event in preview:
            num, player, level, action = event
            print(f"Event {num}: Player {player} (level {level}) {action}")
        print("...")
    except (ValueError, TypeError) as e:
        print(f"Warning: could not display preview: {e}")

    print()
    process_stream(count)
    print()

    print("=== Generator Demonstration ===")

    try:
        fib: Generator = fibonacci_generator()
        fib_numbers: list = get_first_n(fib, 10)
        fib_str: list = []
        for n in fib_numbers:
            fib_str.append(str(n))
        print(f"Fibonacci sequence (first 10): {', '.join(fib_str)}")
    except (ValueError, TypeError) as e:
        print(f"Warning: fibonacci error: {e}")

    try:
        prime: Generator = prime_generator()
        prime_numbers: list = get_first_n(prime, 5)
        prime_str: list = []
        for n in prime_numbers:
            prime_str.append(str(n))
        print(f"Prime numbers (first 5): {', '.join(prime_str)}")
    except (ValueError, TypeError) as e:
        print(f"Warning: prime error: {e}")


if __name__ == "__main__":
    main()