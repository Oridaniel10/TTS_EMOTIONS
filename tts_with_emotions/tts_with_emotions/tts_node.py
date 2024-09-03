import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from bark import generate_audio
from scipy.io.wavfile import write as write_wav
import os
import time
import re


class TTSNode(Node):
    def __init__(self):
        super().__init__("tts_node")
        self.subscription = self.create_subscription(
            String, "play_audio", self.text_to_speech_callback, 10
        )
        self.get_logger().info("\033[92m###### TTS NODE ACTIVE######\033[0m")

        # env!!!!!!!!!!!!!!!
        os.environ["SUNO_USE_SMALL_MODELS"] = "True"
        os.environ["SUNO_OFFLOAD_CPU"] = "True"

    def text_to_speech_callback(self, msg):
        text = msg.data
        self.get_logger().info(f'Received text: "{text}"')

        # Generate a safe filename by replacing spaces with underscores and removing special characters
        safe_text = re.sub(r"[^a-zA-Z0-9_]", "", text.replace(" ", "_"))

        # Limiting the filename length to avoid issues with very long text
        if len(safe_text) > 50:
            safe_text = safe_text[:50]

        # Generate audio with Alice voice
        audio_array = generate_audio(text, history_prompt="v2/en_speaker_3")

        # Saving the audio
        output_file = os.path.join(
            os.path.expanduser("~"), f"{safe_text}_{int(time.time() * 1000)}.wav"
        )
        write_wav(output_file, 24000, audio_array)

        self.get_logger().info(f'Saved audio to "{output_file}"')

        # Play the file
        os.system(f"aplay {output_file}")
        self.get_logger().info(
            "\033[92mWAITING FOR NEXT TEXT - COME ON! TALK TO ME\033[0m"
        )

        # Optionally remove the file after playing it
        # os.remove(output_file)


def main(args=None):
    rclpy.init(args=args)
    node = TTSNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

# format!
# "data: \"I'm really glad to see you today! I wish you a good day\""
