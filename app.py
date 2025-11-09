from flask import Flask, jsonify
import load_test_tasks as t

app = Flask(__name__)

@app.post("/execute")
def execute():
    try:
        result = t.execute_tasks()
        return jsonify({"ok": True, "result": result}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.post("/cpu")
def cpu_only():
    try:
        t.data_processing()
        t.computation_task()
        return jsonify(ok=True), 200
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

@app.post("/io")
def io_only():
    try:
        t.file_io()
        t.logging_task()
        return jsonify(ok=True), 200
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

@app.post("/api")
def api_only():
    try:
        code = t.api_request()
        return jsonify(ok=(code == 200), code=code), (200 if code == 200 else 500)
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500