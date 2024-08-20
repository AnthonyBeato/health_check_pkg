#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue
import psutil
import socket

hostname = socket.gethostname()

# Funcion para retornar tiempo en hh:mm:ss 
def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 

class DiagnosticsPublisher(Node):

    def __init__(self):
        super().__init__('diagnostics_publisher')
        self.publisher_ = self.create_publisher(DiagnosticArray, 'diagnostics', 10)
        timer_period = 10.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Obtener uso de CPU y memoria  
        cpu_usage = psutil.cpu_percent(interval=None)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        # battery_info = psutil.sensors_battery()
        # battery_level = battery_info.percent
        # battery_time_left = battery_info.secsLeft

        msg = DiagnosticArray()
        status = DiagnosticStatus()
        
        status.name = f'{hostname} Diagnostics'
        status.hardware_id = hostname
        status.level = DiagnosticStatus.OK
        status.message = "System is running smoothly"
        
        # Añade más información de diagnóstico según sea necesario
        status.values.append(KeyValue(key="CPU Usage", value=f"{cpu_usage}%"))
        status.values.append(KeyValue(key="Memory Usage", value=f"{memory_usage}%"))
        # status.values.append(KeyValue(key="Battery Level", value=f"{battery_level}%"))    
        # status.values.append(KeyValue(key="Battery Time Left", value=f"{convertTime(battery_time_left)}"))            

        msg.status.append(status)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing diagnostics for: "%s"' % hostname)

def main(args=None):
    rclpy.init(args=args)
    diagnostics_publisher = DiagnosticsPublisher()
    rclpy.spin(diagnostics_publisher)
    diagnostics_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
