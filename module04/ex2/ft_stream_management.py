import sys


def display_header() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")


def collect_archivist_data() -> tuple[str, str]:
    """
    Raccoglie l'ID e il report dell'archivista tramide stdin.
    Ritorna:
        Tupla (archivist_id, status_report)
    """
    archivist_id = input("\nInput Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    return archivist_id, status_report


def send_standard_message(message: str) -> None:
    """
    Invia un messaggio sul canale standard (stdout).
    Uso sys. stdout.write() per essere espliciti su quale
    stream sto ussando (equivalente print() senza file=).
    Args:
        message: Il messaggio da inviare sul canale standard
    """
    sys.stdout.write(f"[STANDARD] {message}\n")
    sys.stdout.flush()


def send_alert_message(message: str) -> None:
    """
    Invia un messaggio di allarme sul canale di errore (stderr).
    stderr e' SEPARATO da stdout: va su schermo anche se
    stdout e' reindirizzato su un file!
    Args:
        message: Il messaggio di allarme da inviare
    """
    sys.stderr.write(f"[ALERT] {message}\n")
    sys.stderr.flush()


def run_communication_test(archivist_id: str, status_report: str) -> None:
    """
    Esegue il test di communicazione sui tre canali.
    Args:
        archivist_id: L'ID dell'archivista
        status_report: Il report di stato dell'archivista
    """
    send_standard_message(
        f"Archive status from {archivist_id}: {status_report}"
    )
    send_alert_message("System diagnostic: Communication channels verified")
    send_standard_message("Data transmiission complete")
    print("\nThree-channel communication test successful.")


def main() -> None:
    """Punto di ingresso principale del programma."""
    display_header()
    archivist_id, status_report = collect_archivist_data()
    print()
    run_communication_test(archivist_id, status_report)


if __name__ == "__main__":
    main()
