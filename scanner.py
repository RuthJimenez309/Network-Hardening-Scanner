import socket
import sys
from datetime import datetime

def mostrar_interfaz_visual(objetivo):
    """Genera un banner visual estético para la terminal."""
    linea_decorativa = "=" * 60
    print(linea_decorativa)
    print(f"║{'NETWORK HARDENING SCANNER (MINI-NMAP)':^58}║")
    print(f"║{'Auditoría de Seguridad de Puertos Locales':^58}║")
    print(linea_decorativa)
    print(f" [+] Objetivo Escaneado : {objetivo}")
    print(f" [+] Tiempo de Inicio   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(linea_decorativa)
    print(f" {'PUERTO':<10} {'ESTADO':<15} {'SERVICIO ESTIMADO'}")
    print("-" * 60)

def escanear_puertos():
    objetivo = "127.0.0.1"
    
    puertos_comunes = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080]
    
    servicios = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS",
        443: "HTTPS", 445: "SMB", 1433: "MSSQL", 3306: "MySQL",
        3389: "RDP (Escritorio Remoto)", 8080: "HTTP-Alt"
    }

    mitigaciones_seguridad = {
        21: "Desactivar FTP anónimo, migrar a SFTP (Puerto 22) y aplicar cifrado TLS robusto.",
        22: "Deshabilitar autenticación por contraseña (usar llaves SSH), cambiar el puerto por defecto y bloquear el acceso root directo.",
        23: "¡ALTA VULNERABILIDAD! Telnet transmite datos en texto plano. Desactivar inmediatamente y migrar a SSH.",
        25: "Configurar TLS forzado, implementar SPF/DKIM/DMARC y restringir retransmisiones no autorizadas (Open Relay).",
        53: "Restringir transferencias de zona DNS (AXFR), habilitar DNSSEC y mitigar ataques de amplificación DNS.",
        80: "Migrar el tráfico a HTTPS (Puerto 443) mediante redirecciones forzadas (HSTS) y desactivar firmas del servidor web.",
        110: "Migrar a POP3S (Puerto 995) con cifrado SSL/TLS obligatorio para proteger las credenciales de correo.",
        135: "Restringir el tráfico de RPC solo a hosts de administración interna mediante listas de control de acceso (ACL) de red.",
        139: "Desactivar NetBIOS sobre TCP/IP si no es estrictamente necesario; priorizar el uso de firmas SMBv3.",
        443: "Deshabilitar protocolos obsoletos (SSLv3, TLS 1.0, TLS 1.1) y configurar suites de cifrado modernas (Cipher Suites).",
        445: "¡CRÍTICO! Mitigar riesgos tipo EternalBlue desactivando SMBv1. Forzar firmas SMBv2/v3 y bloquear el acceso desde el exterior.",
        1433: "Cambiar la cuenta de administración 'sa', forzar conexiones cifradas SSL y restringir el acceso por IP fija corporativa.",
        3306: "Bloquear conexiones externas completas (bind-address = 127.0.0.1) y exigir contraseñas complejas mediante validación de plugins.",
        3389: "Habilitar Autenticación a Nivel de Red (NLA), limitar los intentos de inicio de sesión y configurar una VPN para el acceso remoto.",
        8080: "Asegurar las consolas de administración expuestas en este puerto intermedio y eliminar configuraciones por defecto."
    }

    mostrar_interfaz_visual(objetivo)
    filas_tabla_md = []
    lista_mitigaciones_md = []

    try:
        for puerto in puertos_comunes:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            
            resultado = s.connect_ex((objetivo, puerto))
            nombre_servicio = servicios.get(puerto, "Desconocido")
            
            if resultado == 0:
                estado_consola = " ABIERTO"
                estado_md = " **ABIERTO**"
                riesgo_md = " **Riesgo Potencial**"
                print(f" [>] {puerto:<7} {estado_consola:<15} {nombre_servicio}")
                
                recomendacion = mitigaciones_seguridad.get(puerto, "Revisar la documentación técnica del servicio expuesto.")
                lista_mitigaciones_md.append(f"###  Puerto {puerto} ({nombre_servicio})\n* **Recomendación:** {recomendacion}\n\n")
            else:
                estado_consola = " CERRADO"
                estado_md = " Cerrado"
                riesgo_md = " Seguro"
                print(f" [>] {puerto:<7} {estado_consola:<15} {nombre_servicio}")
            
            filas_tabla_md.append(f"| {puerto} | {nombre_servicio} | {estado_md} | {riesgo_md} |\n")
            s.close()
            
    except KeyboardInterrupt:
        print("\n [!] Escaneo cancelado por el usuario.")
        sys.exit()
    except socket.error:
        print("\n [!] No se pudo conectar al host.")
        sys.exit()

    print("=" * 60)
    print(f"║{'ESCANEO FINALIZADO EXITOSAMENTE':^58}║")
    print("=" * 60)

    nombre_archivo = "reporte_hardening.md"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"#  Informe Técnico de Auditoría de Red\n\n")
        archivo.write(f"Este reporte ejecutivo detalla el estado actual de seguridad de los puertos lógicos de la máquina evaluada, aplicando directrices internacionales de endurecimiento de sistemas (**Hardening**).\n\n")
        archivo.write(f"## ⏱ Detalles del Escaneo\n")
        archivo.write(f"* **Fecha de Ejecución:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        archivo.write(f"* **Host Objetivo:** `{objetivo}` (Localhost)\n")
        archivo.write(f"* **Herramienta:** Network-Hardening-Scanner (Mini-Nmap)\n\n")
        
        archivo.write(f"##  Tabla de Hallazgos\n")
        archivo.write(f"| Puerto | Servicio Estimado | Estado Actual | Evaluación de Riesgo |\n")
        archivo.write(f"| :--- | :--- | :--- | :--- |\n")
        archivo.writelines(filas_tabla_md)
        archivo.write("\n")
        
        archivo.write(f"##  Plan de Acción y Recomendaciones de Hardening\n")
        if lista_mitigaciones_md:
            archivo.write("Se han detectado puertos abiertos en el sistema. Se recomienda aplicar las siguientes medidas correctivas de forma inmediata para mitigar vectores de ataque:\n\n")
            archivo.writelines(lista_mitigaciones_md)
        else:
            archivo.write(" **¡Excelente!** No se detectaron puertos abiertos en el rango común auditado. El firewall local y las políticas de red bloquean de manera efectiva los intentos de conexión de estas firmas lógicas.\n")
    
    print(f"\n [] Reporte avanzado de ciberseguridad exportado en: {nombre_archivo}")

if __name__ == "__main__":
    escanear_puertos()
