import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os


class SpeakerNode(Node):
    def __init__(self):
        super().__init__("speaker_node")
        self.subscription = self.create_subscription(
            String, "speech_done", self.play_audio_callback, 10
        )

    def play_audio_callback(self, msg):
        audio_file_path = msg.data
        self.get_logger().info(f'Playing audio file: "{audio_file_path}"')

        # הפעלת קובץ ה-WAV
        if os.path.exists(audio_file_path):
            os.system(f"aplay {audio_file_path}")
        else:
            self.get_logger().error(f'Audio file "{audio_file_path}" not found.')


def main(args=None):
    rclpy.init(args=args)
    node = SpeakerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
