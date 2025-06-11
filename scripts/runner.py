import uvicorn

"""
Módulo responsável por inicializar o servidor FastAPI.

Este módulo contém funções para configurar e executar o servidor FastAPI
usando Uvicorn de forma programática.
"""
def start_server():
    """
    Inicia o servidor FastAPI usando Uvicorn de forma programática.
    
    Esta função configura e executa o servidor FastAPI com as seguintes características:
    - Host: 127.0.0.1 (localhost)
    - Porta: 8000
    - Modo de desenvolvimento com reload automático habilitado
    - Carrega a aplicação do módulo 'src.main:app'
    
    Returns:
        None
        
    Example:
        >>> start_server()
        Starting Uvicorn server in development mode with reload...
        INFO:     Uvicorn running on http://127.0.0.1:8000
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