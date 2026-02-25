import uvicorn
import os
import sys

if __name__ == "__main__":
    # Add the parent directory to the path to ensure correct module resolution
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(backend_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    # Change to the backend directory
    os.chdir(backend_dir)
    
    # Run the app using the correct module path
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
