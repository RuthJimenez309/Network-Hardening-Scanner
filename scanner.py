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
    
    # Lista de puertos lógicos comunes a auditar
    puertos_comunes = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080]
    
    servicios = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS",
        443: "HTTPS", 445: "SMB", 1433: "MSSQL", 3306: "MySQL",
        3389: "RDP (Escritorio Remoto)", 8080: "HTTP-Alt"
    }

    mostrar_interfaz_visual(objetivo)
    resultados_reporte = []

    try:
        for puerto in puertos_comunes:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            
            resultado = s.connect_ex((objetivo, puerto))
            nombre_servicio = servicios.get(puerto, "Desconocido")
            
            if resultado == 0:
                estado = " ABIERTO"
                print(f" [>] {puerto:<7} {estado:<15} {nombre_servicio}")
                resultados_reporte.append(f"Puerto {puerto} ({nombre_servicio}): ABIERTO - Requiere revisión de Hardening.\n")
            else:
                estado = " CERRADO"
                print(f" [>] {puerto:<7} {estado:<15} {nombre_servicio}")
                resultados_reporte.append(f"Puerto {puerto} ({nombre_servicio}): CERRADO - Seguro.\n")
            
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

    # Guardar reporte automático para las evidencias de tu portafolio
    nombre_archivo = "reporte_hardening.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"=== REPORTE DE AUDITORÍA DE RED ===\n")
        archivo.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        archivo.write(f"Objetivo: {objetivo}\n")
        archivo.write("=" * 35 + "\n")
        archivo.writelines(resultados_reporte)
    
    print(f"\n [📝] Evidencia guardada con éxito en: {nombre_archivo}")

if __name__ == "__main__":
    escanear_puertos()
