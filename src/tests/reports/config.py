# import pytest
# from colorama import Fore, Style, init
#
# init(autoreset=True)
#
# results = {}
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#    
#     if report.when == "call":
#         markers = [m.name for m in item.iter_markers()]
#         category_name = markers[0] if markers else "General"
#
#         if category_name not in results:
#             results[category_name] = []
#
#         results[category_name].append((item.name, report.outcome))
#
# def pytest_sessionfinish(session, exitstatus):
#     print("\n\n===== TEST RESULTS =====")
#     for category, tests in results.items():
#         print(f"{Fore.CYAN}{category.capitalize()}:")
#         for i, (name, status) in enumerate(tests, 1):
#             if status == "passed":
#                 status_color = Fore.GREEN
#             elif status == "failed":
#                 status_color = Fore.RED
#             else:
#                 status_color = Fore.YELLOW
#             print(f" {i}. {name.replace('_', ' ').capitalize()} {status_color}{status.upper()}{Style.RESET_ALL}")
#     print("========================\n")
import pytest
from collections import defaultdict
from colorama import Fore, Style, init

init(autoreset=True)

MAIN_CATEGORIES = {"stocks", "users"}
SUB_CATEGORIES = {"api", "model", "auth"}

ICONS = {
    "passed": "✅",
    "failed": "❌",
    "skipped": "⚠️",
}

results = defaultdict(lambda: defaultdict(list))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    markers = {m.name for m in item.own_markers}

    main = next((m for m in markers if m in MAIN_CATEGORIES), "general")
    sub = next((m for m in markers if m in SUB_CATEGORIES), "general")

    results[main][sub].append((item.name, report.outcome))


def format_test_name(name, width=40):
    clean = name.replace("_", " ")
    dots = "." * max(2, width - len(clean))
    return f"{clean} {dots}"


def pytest_sessionfinish(session, exitstatus):
    print("\n\n===== TEST RESULTS =====\n")

    for main_i, (main, subs) in enumerate(sorted(results.items())):
        print(f"📦 {main.capitalize()}")

        sub_items = list(sorted(subs.items()))
        for sub_i, (sub, tests) in enumerate(sub_items):
            is_last_sub = sub_i == len(sub_items) - 1
            prefix = " └──" if is_last_sub else " ├──"

            print(f"{prefix} {Fore.CYAN}{sub.upper()}{Style.RESET_ALL}")

            for test_i, (name, status) in enumerate(tests):
                is_last_test = test_i == len(tests) - 1
                sub_prefix = "      └──" if is_last_test else "      ├──"

                icon = ICONS.get(status, "⚠️")

                if status == "passed":
                    color = Fore.GREEN
                elif status == "failed":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW

                formatted_name = format_test_name(name)

                print(
                    f"{sub_prefix} {formatted_name} {color}{icon} {status.upper()}{Style.RESET_ALL}"
                )

        print()

    print("========================\n")
