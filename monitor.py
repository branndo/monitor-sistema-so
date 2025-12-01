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

    '''
        datos = {
        "CPU": f"{self.obtener_uso_cpu():.1f}%",
        "Memoria": f"{self.obtener_uso_memoria()['porcentaje']:.1f}%",
        "Procesos": str(self.obtener_procesos()),
        "Disco": f"{self.obtener_disco()['porcentaje']:.1f}%"
    }
    '''
    #Limpia la pantalla. ojito es  para que no se vea feito en la terminal.
    def mostrar_info(self):
        self.limpiar_pantalla()

    def crear_barra(self, porcentaje, ancho=30):
        """Crea una barra de progreso gráfica"""
        completo = int(porcentaje * ancho / 100)
        barra = "█" * completo + "░" * (ancho - completo)
        return barra
        
        print("=" * 50)
        print("=" * 50)
        print("MONITOR DE RECURSOS DEL SISTEMA")
        print(f"MONITOR DEL SISTEMA - {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 50)
        print("=" * 50)
        
        
        # Obtener datos
        cpu = self.obtener_uso_cpu()
        cpu_uso = self.obtener_uso_cpu()
        print(f"CPU: {cpu_uso}%")
        
        memoria = self.obtener_uso_memoria()
        memoria = self.obtener_uso_memoria()
        print(f"MEMORIA: {memoria['porcentaje']}% ({memoria['disponible']}GB libres de {memoria['total']}GB)")
        
        procesos = self.obtener_procesos()
        procesos = self.obtener_procesos()
        print(f"PROCESOS ACTIVOS: {procesos}")
        
        disco = self.obtener_disco()
        disco = self.obtener_disco()
        print(f"DISCO: {disco['porcentaje']}% usado ({disco['libre']}GB libres de {disco['total']}GB)")
        
        red = self.obtener_red()
        red = self.obtener_red()
        print(f"RED: ↓{red['bytes_recibidos']}MB ↑{red['bytes_enviados']}MB")
        
        
        # Creacion de barras para hacerrlo mas grafico posible 
        barra_cpu = self.crear_barra(cpu)
        barra_memoria = self.crear_barra(memoria['porcentaje'])
        barra_disco = self.crear_barra(disco['porcentaje'])
        
        # Mostrando las barras por cada seccion 
        print(f"\nCPU:")
        print(f"  [{barra_cpu}]")
        print(f"  {cpu:.1f}%")
        
        print(f"\nMEMORIA:")
        print(f"  [{barra_memoria}]")
        print(f"  {memoria['porcentaje']:.1f}%  ({memoria['disponible']} GB libres de {memoria['total']} GB)")
        
        print(f"\nPROCESOS:")
        print(f"  {procesos} todos los procesos activos")
        
        print(f"\nALMACENAMIENTO:")
        print(f"  [{barra_disco}]")
        print(f"  {disco['porcentaje']:.1f}%  ({disco['libre']} GB libres de {disco['total']} GB)")
        
        print(f"\nRED:")
        print(f"  ↓ {red['bytes_recibidos']:>5} MB recibidos")
        print(f"  ↑ {red['bytes_enviados']:>5} MB enviados")
        
        # Comanddo para acabar el proceso, no es CTRL Z
        print("\n" + "-" * 50)
        print("=" * 50)
        print(f"Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Presionar Ctrl + C terminar el proceso.")
    
    
    def ejecutar(self):
    def ejecutar(self):
        try:
        try:
            while True:
            while True:
                self.mostrar_info()
                self.mostrar_info()
                time.sleep(self.intervalo)
                time.sleep(self.intervalo)
        except KeyboardInterrupt:
        except KeyboardInterrupt:
            print("\n\nMonitor finalizado.")
            
if __name__ == "__main__":
if __name__ == "__main__":
    monitor = MonitorSistema()
    monitor = MonitorSistema()
    monitor.ejecutar()
