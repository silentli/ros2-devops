from prometheus_client import start_http_server, Gauge
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ROSMetrics(Node):
    def __init__(self):
        super().__init__('ros_metrics')
        self.metric = Gauge('ros_random_number', 'Random number from ROS topic')
        self.create_subscription(Int32, '/random_number', self.update_metric, 10)

    def update_metric(self, msg):
        self.metric.set(msg.data)

def main():
    start_http_server(8000)
    rclpy.init()
    node = ROSMetrics()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
