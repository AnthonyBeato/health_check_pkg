import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile
import socket

hostname = socket.gethostname()

class HeartbeatPublisher(Node):

    def __init__(self):
        super().__init__('heartbeat_publisher')
        self.publisher_ = self.create_publisher(String, 'heartbeat', QoSProfile(depth=10))
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = f"{hostname}: alive"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    heartbeat_publisher = HeartbeatPublisher()
    rclpy.spin(heartbeat_publisher)
    heartbeat_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
