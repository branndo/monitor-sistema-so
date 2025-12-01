# 🖥️ Monitor Básico del Sistema - Sistemas Operativos

## 📋 Descripción
Herramienta de monitorización en tiempo real para sistemas operativos desarrollada en Python. Muestra métricas esenciales del sistema de manera clara y accesible.

## 🚀 Características
- 📊 **Monitoreo de CPU** en tiempo real
- 💾 **Uso de memoria RAM** con porcentaje y valores 
- 🔄 **Procesos activos** en el sistema en uso
- 💿 **Espacio en disco** utilizado y disponible 
- 🌐 **Estadísticas de red** - tráfico entrante y tambien el saliente

## 🛠️ Tecnologías Utilizadas
- **Python 3.6**
- **Librería psutil** para obtención de métricas del sistema
- **Git** para control de versiones

## 📦 Instalación

### Prerrequisitos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual

### Pasos de instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/monitor-sistema-so.git

# Navegar al directorio
cd monitor-sistema-so

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el monitor
python monitor.py

````
### Salida Esperada
-Maquina de La Pulga Chiapaneca
- MONITOR DEL SISTEMA - 11:31:11
- 
==================================================

-CPU: 12.1%

-MEMORIA: 42.7% (18GB libres de 31GB)

-PROCESOS ACTIVOS: 270

-DISCO: 60.3% usado (369GB libres de 930GB)

-RED: ↓2082MB ↑79MB

==================================================

-Presiona Ctrl+C para salir :v
