#!/usr/bin/env python
"""Test script to verify all dependencies are installed and working on Windows."""

import sys

def test_imports():
    """Test all critical imports."""
    print("Testing imports...")
    
    try:
        import flask
        try:
            version = flask.__version__
            print(f"[OK] Flask {version}")
        except AttributeError:
            print("[OK] Flask")
    except ImportError as e:
        print(f"[FAIL] Flask: {e}")
        return False
    
    try:
        import werkzeug
        try:
            version = werkzeug.__version__
            print(f"[OK] Werkzeug {version}")
        except AttributeError:
            print("[OK] Werkzeug")
    except ImportError as e:
        print(f"[FAIL] Werkzeug: {e}")
        return False
    
    try:
        import fitz  # PyMuPDF
        print("[OK] PyMuPDF (fitz)")
    except ImportError as e:
        print(f"[FAIL] PyMuPDF: {e}")
        return False
    
    try:
        import docx
        print("[OK] python-docx")
    except ImportError as e:
        print(f"[FAIL] python-docx: {e}")
        return False
    
    try:
        import openai
        print(f"[OK] openai {openai.__version__}")
    except ImportError as e:
        print(f"[FAIL] openai: {e}")
        return False
    
    try:
        import fire
        print("[OK] fire")
    except ImportError as e:
        print(f"[FAIL] fire: {e}")
        return False
    
    try:
        import loguru
        print("[OK] loguru")
    except ImportError as e:
        print(f"[FAIL] loguru: {e}")
        return False
    
    try:
        import datasets
        print(f"[OK] datasets {datasets.__version__}")
    except ImportError as e:
        print(f"[FAIL] datasets: {e}")
        return False
    
    try:
        import typer
        print("[OK] typer")
    except ImportError as e:
        print(f"[FAIL] typer: {e}")
        return False
    
    try:
        import rich
        try:
            version = rich.__version__
            print(f"[OK] rich {version}")
        except AttributeError:
            print("[OK] rich")
    except ImportError as e:
        print(f"[FAIL] rich: {e}")
        return False
    
    try:
        import dotenv
        print("[OK] python-dotenv")
    except ImportError as e:
        print(f"[FAIL] python-dotenv: {e}")
        return False
    
    try:
        import requests
        print(f"[OK] requests {requests.__version__}")
    except ImportError as e:
        print(f"[FAIL] requests: {e}")
        return False
    
    try:
        from flask_sqlalchemy import SQLAlchemy
        print("[OK] Flask-SQLAlchemy")
    except ImportError as e:
        print(f"[FAIL] Flask-SQLAlchemy: {e}")
        return False
    
    try:
        # Apply compatibility fix before importing
        import werkzeug
        if not hasattr(werkzeug, 'secure_filename'):
            from werkzeug.utils import secure_filename as _secure_filename
            werkzeug.secure_filename = _secure_filename
        if not hasattr(werkzeug, 'FileStorage'):
            from werkzeug.datastructures import FileStorage
            werkzeug.FileStorage = FileStorage
        
        from flask_uploads import UploadSet
        print("[OK] Flask-Uploads")
    except ImportError as e:
        print(f"[FAIL] Flask-Uploads: {e}")
        return False
    
    try:
        from flask_migrate import Migrate
        print("[OK] Flask-Migrate")
    except ImportError as e:
        print(f"[FAIL] Flask-Migrate: {e}")
        return False
    
    return True

def test_app():
    """Test Flask app import."""
    print("\nTesting Flask app...")
    try:
        from app import app
        print("[OK] Flask app imports successfully")
        print(f"[OK] App name: {app.name}")
        return True
    except Exception as e:
        print(f"[FAIL] Flask app import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_directories():
    """Test required directories exist."""
    import os
    print("\nTesting directories...")
    
    dirs = ['instance', 'uploads']
    all_exist = True
    
    for dir_name in dirs:
        if os.path.exists(dir_name):
            print(f"[OK] {dir_name}/ exists")
        else:
            print(f"[FAIL] {dir_name}/ missing")
            all_exist = False
    
    return all_exist

if __name__ == "__main__":
    print("=" * 50)
    print("MoA Groq Chatbot - Installation Test")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print("=" * 50)
    
    success = True
    success &= test_imports()
    success &= test_directories()
    success &= test_app()
    
    print("\n" + "=" * 50)
    if success:
        print("[OK] All tests passed! Installation is complete.")
        print("You can now run the application using:")
        print("  - python app.py")
        print("  - run.bat (Windows)")
        print("  - .\\run.ps1 (PowerShell)")
    else:
        print("[FAIL] Some tests failed. Please check the errors above.")
    print("=" * 50)
    
    sys.exit(0 if success else 1)

