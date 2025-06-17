import os
import importlib

def show_postgres_menu():
    print("=== PostgreSQL Tools ===")

    current_dir = os.path.dirname(__file__)
    entries = os.listdir(current_dir)

    actions = {}
    index = 1
    print("0. Back")

    for entry in entries:
        full_path = os.path.join(current_dir, entry)

        # ملفات .py
        if entry.endswith(".py") and entry not in ("main.py", "__init__.py"):
            name = entry[:-3]
            label = name.replace("_", " ").capitalize()
            actions[str(index)] = ("file", name)
            print(f"{index}. {label}")
            index += 1

        # مجلدات فيها main.py أو __init__.py
        elif os.path.isdir(full_path) and (
            "main.py" in os.listdir(full_path) or "__init__.py" in os.listdir(full_path)
        ):
            label = entry.replace("_", " ").capitalize()
            actions[str(index)] = ("folder", entry)
            print(f"{index}. {label} (module)")
            index += 1

    choice = input("Select: ").strip()

    if choice == "0":
        return
    elif choice in actions:
        action_type, module_name = actions[choice]
        try:
            if action_type == "file":
                module = importlib.import_module(f".{module_name}", package=__package__)
            else:
                module = importlib.import_module(f".{module_name}.main", package=__package__)
            
            if hasattr(module, "main"):
                module.main()
            elif hasattr(module, "run"):
                module.run()
            else:
                print(f"❌ Module '{module_name}' has no main() or run() function.")
        except Exception as e:
            print(f"❌ Error loading module '{module_name}': {e}")
    else:
        print("Invalid choice.")
