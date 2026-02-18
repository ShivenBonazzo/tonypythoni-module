import sys

def parse_scores(args: list) -> list:
	scores: list = []
	i: int = 1
	while i < len(args):
		try:
			scores.append(int(args[i]))
		except ValueError:
			print(f"Warning: i{args[i]}' is not valid, skipped.")
		i += 1
	return scores


def display_analytics(scores: list) -> None:
	print("=== Player Score Analytics ===")
	if len(scores) == 0:
		print("No scores provided. Usage python3 ft_score_analytics.py <score1> <score2> ...")
		return
	total: int = sum(scores)
	average: float = total / len(scores)
	score_range: int = max(scores) - min(scores)

	print(f"Scores processed: {scores}")
	print(f"Total players: {len(scores)}")
	print(f"Total score: {total}")
	print(f"Average score: {average}")
	print(f"High score: {max(scores)}")
	print(f"Low score: {min(scores)}")
	print(f"Score range: {score_range}")


def main() -> None:
	scores: list = parse_scores(sys.argv)
	display_analytics(scores)


if __name__ == "__main__":
	main()