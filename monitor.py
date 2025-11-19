import psutil
import time
import os
from datetime import datetime

class MonitorSistema:
    def __init__(self):
        self.intervalo = 2
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def obtener_uso_cpu(self):
        return psutil.cpu_percent(interval=1)
    
    def obtener_uso_memoria(self):
        memoria = psutil.virtual_memory()
        return {
            'total': memoria.total // (1024**3),
            'disponible': memoria.available // (1024**3),
            'porcentaje': memoria.percent
        }
    
    def obtener_procesos(self):
        return len(psutil.pids())
    
    def obtener_disco(self):
        disco = psutil.disk_usage('/')
        return {
            'total': disco.total // (1024**3),
            'libre': disco.free // (1024**3),
            'porcentaje': disco.percent
        }
    
    def obtener_red(self):
        red = psutil.net_io_counters()
        return {
            'bytes_enviados': red.bytes_sent // (1024**2),
            'bytes_recibidos': red.bytes_recv // (1024**2)
        }
    
    def mostrar_info(self):
        self.limpiar_pantalla()
        
        print("=" * 50)
        print(f"MONITOR DEL SISTEMA - {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 50)
        
        cpu_uso = self.obtener_uso_cpu()
        print(f"CPU: {cpu_uso}%")
        
        memoria = self.obtener_uso_memoria()
        print(f"MEMORIA: {memoria['porcentaje']}% ({memoria['disponible']}GB libres de {memoria['total']}GB)")
        
        procesos = self.obtener_procesos()
        print(f"PROCESOS ACTIVOS: {procesos}")
        
        disco = self.obtener_disco()
        print(f"DISCO: {disco['porcentaje']}% usado ({disco['libre']}GB libres de {disco['total']}GB)")
        
        red = self.obtener_red()
        print(f"RED: ↓{red['bytes_recibidos']}MB ↑{red['bytes_enviados']}MB")
        
        print("=" * 50)
        print("Presiona Ctrl+C para salir")
    
    def ejecutar(self):
        try:
            while True:
                self.mostrar_info()
                time.sleep(self.intervalo)
        except KeyboardInterrupt:
            print("\nMonitor terminado")

if __name__ == "__main__":
    monitor = MonitorSistema()
    monitor.ejecutar()