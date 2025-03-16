import subprocess
import os
import webbrowser

def start_backend():
    subprocess.Popen(["python", "backend/main.py"])

def open_browser():
    # Get the path to the index.html file within the packaged application
    # This assumes index.html is in the same directory as run.py
    # and the backend is in a subdirectory called 'backend'
    
    # Get the directory of the currently running script (run.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to index.html
    index_path = os.path.join(script_dir, "index.html")

    # Open the index.html file using the default browser
    try:
        webbrowser.open("file://" + index_path) # Use file:// for local files
    except Exception as e:
        print(f"Error opening index.html: {e}")

if __name__ == "__main__":
    start_backend()
    open_browser()
