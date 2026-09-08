def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_n_primes(n):
    """Print the first n prime numbers."""
    if n <= 0:
        print("Please enter a positive integer.")
        return

    count = 0
    num = 2
    primes = []

    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1

    print(f"The first {n} prime numbers are:")
    for i, prime in enumerate(primes, 1):
        print(f"{i}. {prime}")


if __name__ == "__main__":
    n = int(input("Enter the number of prime numbers to print: "))
    print_n_primes(n)


jarvis/
├── main.py
├── requirements.txt
├── README.md
├── INSTALLATION.md
├── CONFIGURATION.md
├── SECURITY.md
├── TOOLS.md
├── TROUBLESHOOTING.md
├── config/
│   ├── default_config.json
│   └── permissions.json
├── core/
│   ├── __init__.py
│   ├── orchestrator.py
│   └── event_bus.py
├── ai/
│   ├── __init__.py
│   ├── provider.py
│   ├── intent_detector.py
│   └── local_provider.py
├── tools/
│   ├── __init__.py
│   ├── base.py
│   ├── registry.py
│   ├── application_tools.py
│   ├── file_tools.py
│   ├── system_tools.py
│   ├── browser_tools.py
│   ├── terminal_tools.py
│   └── screenshot_tools.py
├── security/
│   ├── __init__.py
│   ├── permissions.py
│   ├── command_validator.py
│   └── audit_log.py
├── voice/
│   ├── __init__.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── widgets.py
│   ├── styles.py
│   └── dialogs.py
├── system/
│   ├── __init__.py
│   ├── monitor.py
│   └── info.py
├── memory/
│   ├── __init__.py
│   └── history.py
├── logging_setup/
│   ├── __init__.py
│   └── logger.py
└── tests/
    ├── __init__.py
    ├── test_permissions.py
    ├── test_command_validator.py
    ├── test_file_tools.py
    ├── test_application_tools.py
    ├── test_system_monitor.py
    ├── test_ai_tools.py
    ├── test_confirmation.py
    ├── test_config.py
    └── test_error_handling.py
