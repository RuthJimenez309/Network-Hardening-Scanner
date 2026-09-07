#  Informe Técnico de Auditoría de Red

Este reporte ejecutivo detalla el estado actual de seguridad de los puertos lógicos de la máquina evaluada, aplicando directrices internacionales de endurecimiento de sistemas (**Hardening**).

## ⏱ Detalles del Escaneo
* **Fecha de Ejecución:** 2026-09-06 21:45:57
* **Host Objetivo:** `127.0.0.1` (Localhost)
* **Herramienta:** Network-Hardening-Scanner (Mini-Nmap)

##  Tabla de Hallazgos
| Puerto | Servicio Estimado | Estado Actual | Evaluación de Riesgo |
| :--- | :--- | :--- | :--- |
| 21 | FTP |  Cerrado |  Seguro |
| 22 | SSH |  Cerrado |  Seguro |
| 23 | Telnet |  Cerrado |  Seguro |
| 25 | SMTP |  Cerrado |  Seguro |
| 53 | DNS |  Cerrado |  Seguro |
| 80 | HTTP |  Cerrado |  Seguro |
| 110 | POP3 |  Cerrado |  Seguro |
| 135 | RPC |  **ABIERTO** |  **Riesgo Potencial** |
| 139 | NetBIOS |  Cerrado |  Seguro |
| 443 | HTTPS |  Cerrado |  Seguro |
| 445 | SMB |  **ABIERTO** |  **Riesgo Potencial** |
| 1433 | MSSQL |  Cerrado |  Seguro |
| 3306 | MySQL |  **ABIERTO** |  **Riesgo Potencial** |
| 3389 | RDP (Escritorio Remoto) |  Cerrado |  Seguro |
| 8080 | HTTP-Alt |  Cerrado |  Seguro |

##  Plan de Acción y Recomendaciones de Hardening
Se han detectado puertos abiertos en el sistema. Se recomienda aplicar las siguientes medidas correctivas de forma inmediata para mitigar vectores de ataque:

###  Puerto 135 (RPC)
* **Recomendación:** Restringir el tráfico de RPC solo a hosts de administración interna mediante listas de control de acceso (ACL) de red.

###  Puerto 445 (SMB)
* **Recomendación:** ¡CRÍTICO! Mitigar riesgos tipo EternalBlue desactivando SMBv1. Forzar firmas SMBv2/v3 y bloquear el acceso desde el exterior.

###  Puerto 3306 (MySQL)
* **Recomendación:** Bloquear conexiones externas completas (bind-address = 127.0.0.1) y exigir contraseñas complejas mediante validación de plugins.

