import uvicorn

def start_server():
    """
    Inicia o servidor FastAPI usando Uvicorn de forma programática.
    """
    print("Starting Uvicorn server in development mode with reload...")
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    start_server()