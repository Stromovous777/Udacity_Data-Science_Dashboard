from pathlib import Path

project_root = Path(__file__).parent.parent

test = Path(project_root / 'python-package' / 'employee_events' / 'employee_events.db')

print(test)