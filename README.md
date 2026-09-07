# Network-Hardening-Scanner 

Este proyecto consiste en un escáner de puertos activo local (mini-Nmap) desarrollado en Python para auditorías de seguridad y endurecimiento de redes (Network Hardening). Su objetivo es identificar ranuras de comunicación lógicas expuestas en la máquina para mitigar riesgos de intrusión.

##  Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Librerías Nativas:** `socket` (Conexiones de red), `sys` (Control del sistema), `datetime` (Estampas de tiempo).
* **Entorno:** PowerShell / VS Code.

##  Cómo Ejecutarlo
1. Clona este repositorio o descarga los archivos.
2. Abre tu terminal en la carpeta del proyecto.
3. Ejecuta el comando:
   ```bash
   python scanner.py
   ```

##  Resultados e Impacto
El script genera automáticamente un archivo llamado `reporte_hardening.txt` tras finalizar el escaneo. Este reporte detalla de forma precisa qué puertos lógicos se encuentran expuestos para aplicar las políticas de remediación correspondientes (como cerrar servicios innecesarios o configurar el Firewall).
