import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile

class HeartbeatListener(Node):

    def __init__(self):
        super().__init__('heartbeat_listener')
        self.subscription = self.create_subscription(
            String,
            'heartbeat',
            self.listener_callback,
            QoSProfile(depth=10))
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    heartbeat_listener = HeartbeatListener()
    rclpy.spin(heartbeat_listener)
    heartbeat_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
