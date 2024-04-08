import re
import time

colored_Text = "\x1b[38;2;255;0;0mG\x1b[0m\x1b[38;2;245;0;9mr\x1b[0m\x1b[38;2;236;0;18ma\x1b[0m\x1b[38;2;226;0;27md\x1b[0m\x1b[38;2;217;0;37mi\x1b[0m\x1b[38;2;207;0;46me\x1b[0m\x1b[38;2;198;0;55mn\x1b[0m\x1b[38;2;188;0;64mt\x1b[0m\x1b[38;2;179;0;74m \x1b[0m\x1b[38;2;170;0;83mt\x1b[0m\x1b[38;2;160;0;92me\x1b[0m\x1b[38;2;151;0;101mx\x1b[0m\x1b[38;2;141;0;111mt\x1b[0m\x1b[38;2;132;0;120m \x1b[0m\x1b[38;2;122;0;129mG\x1b[0m\x1b[38;2;113;0;138mr\x1b[0m\x1b[38;2;103;0;148ma\x1b[0m\x1b[38;2;94;0;157md\x1b[0m\x1b[38;2;85;0;166mi\x1b[0m\x1b[38;2;75;0;175me\x1b[0m\x1b[38;2;66;0;185mn\x1b[0m\x1b[38;2;56;0;194mt\x1b[0m\x1b[38;2;47;0;203m \x1b[0m\x1b[38;2;37;0;212mt\x1b[0m\x1b[38;2;28;0;222me\x1b[0m\x1b[38;2;18;0;231mx\x1b[0m\x1b[38;2;9;0;240mt\x1b[0m"
# print(colored_Text)

pattern = "\x1b\[38;2;[0-9;]+m"


class PinkColor:
    def __init__(self) -> None:
        self.animate = self.Animation

    def gradient_text(self, text: str, colors_array: list[tuple[int, int, int]]) -> str:
        num_colors = len(colors_array)
        text_length = len(text)
        color_step = [[(colors_array[i + 1][j] - colors_array[i][j]) / text_length for j in range(3)] for i in
                      range(num_colors - 1)]
        colored_text = ""

        for i in range(text_length):
            color_index = min(int(i / (text_length / (num_colors - 1))), num_colors - 2)
            color = [int(colors_array[color_index][k] + color_step[color_index][k] * (
                    i - color_index * (text_length / (num_colors - 1)))) for k in range(3)]
            colored_text += f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m{text[i]}\x1b[0m"

        return colored_text

    class Animation:
        def __init__(self) -> None:
            pass

    def wave(self, pattern: str, text: str, sleep_time: float) -> None:
        all_matches = re.findall(pattern, text)
        while True:
            for i in range(len(all_matches)):
                new_text = text
                for j in range(len(all_matches)):
                    new_text = new_text.replace(all_matches[j], all_matches[(j + 1) % len(all_matches)])
                    print(new_text, end="", flush=True)
                    time.sleep(sleep_time)
                    print("\r", end="", flush=True)
                    text = new_text

    import time

    def flicker_text(self, text: str, colors: list[tuple[int, int, int]]) -> None:
        for frame in range(len(text)):
            animated_text = self.gradient_text(text, colors)
            i = 0
            while True:
                print(animated_text[i], end="")
                i += 1
                if i >= len(animated_text):
                    i = 0
                    time.sleep(0.00099)  # Adjust speed of animation here
                    print("\r", end="")
                time.sleep(0.0099)  # Adjust speed of animation here

    def wave_gradient_text(self, text: str, colors: list[tuple[int, int, int]]) -> None:
        wave_length = len(text) // 3  # Adjust wave length here
        wave_count = 0

        while True:
            for i in range(len(text)):
                color_index = (i + wave_count) % len(colors)
                color = colors[color_index]
                colored_char = f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m{text[i]}\x1b[0m"
                print(colored_char, end="")
            wave_count = (wave_count + 1) % wave_length
            time.sleep(0.009)  # Adjust speed of animation here
            print("\r", end="")


