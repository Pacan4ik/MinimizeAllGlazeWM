import subprocess
import json


def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8',
                                creationflags=subprocess.CREATE_NO_WINDOW)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return None


def get_focused_workspace():
    output = run_command(["glazewm", "query", "workspaces"])
    if output:
        try:
            data = json.loads(output)
            for workspace in data.get("data", {}).get("workspaces", []):
                if workspace.get("hasFocus"):
                    return workspace
        except json.JSONDecodeError:
            pass
    return None


def process_child(child, minimized_any):
    if child.get("type") == "window" and child.get("displayState") == "shown" and "state" in child:
        window_id = child.get("id")
        state_type = child["state"].get("type")

        if window_id and state_type != "minimized":
            run_command(["glazewm", "command", "--id", window_id, "toggle-minimized"])
            minimized_any = True
    elif child.get("type") == "split":
        for sub_child in child.get("children", []):
            minimized_any = process_child(sub_child, minimized_any)

    return minimized_any


def toggle_minimized_for_windows(workspace):
    minimized_any = False

    for child in workspace.get("children", []):
        minimized_any = process_child(child, minimized_any)

    if not minimized_any:
        for child in workspace.get("children", []):
            if "prevState" in child and child["prevState"].get("type") != "minimized":
                window_id = child.get("id")
                if window_id:
                    run_command(["glazewm", "command", "--id", window_id, "toggle-minimized"])


def main():
    ws = get_focused_workspace()
    if ws:
        toggle_minimized_for_windows(ws)


main()
