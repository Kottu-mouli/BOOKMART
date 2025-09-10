# test_import.py
try:
    from students.wsgi import application
    print("✅ Import successful!")
except ModuleNotFoundError as e:
    print("❌ ModuleNotFoundError:", e)
except Exception as e:
    print("⚠️ Other error:", e)