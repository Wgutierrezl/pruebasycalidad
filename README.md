### Para correr el archivo correctamente, seguir los siguientes pasos:
1. Ubicarse en la ruta del archivo

2. En la consola, crear un entorno virtual con el comando:
    ```python
    Python -m venv venv
    ```

3. Activar el entorno virtual
```bash
    .\venv\Scripts\activate
```

4. Instalar los requerimientos encontrados en 'requirements.txt'
    ```python
    pip install -r requirements.txt
    ```

5. Seleccionar el web Driver necesario dependiendo del navegador a usar, ya sea Firefox, Chrome, etc.

6. Correr el archivo automation.py
    ```Python
    py automation.py
    ```

## Recomendaciones:
Seguir el siguiente orden de pruebas: registerAutomation -> LogIn -> newAccounts