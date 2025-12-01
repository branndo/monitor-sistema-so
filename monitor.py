import psutil
import time
import os
from datetime import datetime

class MonitorSistema:
    def __init__(self):
        self.intervalo = 2
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def crear_barra(self, porcentaje, ancho=30):
    #Crea una barra de progreso gráfica
        completo = int(porcentaje * ancho / 100)
    # Usar caracteres para las barras
        barra = "#" * completo + "-" * (ancho - completo)
        return barra
    
    def consumo_procesador(self):
        return psutil.cpu_percent(interval=1)
    
    def consumo_memoria(self):
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
        
        print("=" * 40)
        print("MONITOR DE RECURSOS DEL SISTEMA")
        print("=" * 40)
        
        # Obtener datos del sistema, ojo con los tipos de datos
        cpu = self.consumo_procesador()
        memoria = self.consumo_memoria()
        procesos = self.obtener_procesos()
        disco = self.obtener_disco()
        red = self.obtener_red()
        
        # Crear barras de progreso  no ocupamos librerias externas
        barra_cpu = self.crear_barra(cpu)
        barra_memoria = self.crear_barra(memoria['porcentaje'])
        barra_disco = self.crear_barra(disco['porcentaje'])
        
        # Mostrar con barras
        print(f"\nCPU:")
        print(f"  [{barra_cpu}]")
        print(f"  {cpu:.1f}%")
        
        print(f"\nMEMORIA:")
        print(f"  [{barra_memoria}]")
        print(f"  {memoria['porcentaje']:.1f}%  ({memoria['disponible']} GB libres de {memoria['total']} GB)")
        
        print(f"\nPROCESOS:")
        print(f"  {procesos} procesos activos")
        
        print(f"\nALMACENAMIENTO:")
        print(f"  [{barra_disco}]")
        print(f"  {disco['porcentaje']:.1f}%  ({disco['libre']} GB libres de {disco['total']} GB)")
        
        print(f"  Recibidos: {red['bytes_recibidos']:>5} MB")
        print(f"  Enviados:  {red['bytes_enviados']:>5} MB")
        
        # Separador
        print("\n" + "-" * 50)
        print(f"Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Presionar Ctrl + C para salir :v")
    
    def ejecutar(self):
        try:
            while True:
                self.mostrar_info()
                time.sleep(self.intervalo)
        except KeyboardInterrupt:
            print("\n\nMonitor terminado.")
        

if __name__ == "__main__":
    monitor = MonitorSistema()
    monitor.ejecutar()