from setuptools import setup

package_name = "tts_with_emotions"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools", "pyttsx3"],
    zip_safe=True,
    maintainer="ori",
    maintainer_email="orizxzx@gmail.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "tts_node = tts_with_emotions.tts_node:main",
            "speaker_node = tts_with_emotions.speaker_node:main",
        ],
    },
)
