import pytest
from colorama import Fore, Style, init

init(autoreset=True)

results = {}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        markers = [m.name for m in item.iter_markers()]
        category_name = markers[0] if markers else "General"

        if category_name not in results:
            results[category_name] = []

        results[category_name].append((item.name, report.outcome))

def pytest_sessionfinish(session, exitstatus):
    print("\n\n===== TEST RESULTS =====")
    for category, tests in results.items():
        print(f"{Fore.CYAN}{category.capitalize()}:")
        for i, (name, status) in enumerate(tests, 1):
            if status == "passed":
                status_color = Fore.GREEN
            elif status == "failed":
                status_color = Fore.RED
            else:
                status_color = Fore.YELLOW
            print(f" {i}. {name.replace('_', ' ').capitalize()} {status_color}{status.upper()}{Style.RESET_ALL}")
    print("========================\n")
