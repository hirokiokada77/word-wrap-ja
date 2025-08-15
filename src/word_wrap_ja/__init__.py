import argparse
import sys

from janome.tokenizer import Tokenizer
from wcwidth import wcswidth

PROHIBIT_LINE_START_CHARS = set("、。，．」』）】〉》’”")


def wrap_text(text: str, max_width: int) -> str:
    tokenizer = Tokenizer()
    lines = []

    for line in text.splitlines():
        tokens = tokenizer.tokenize(line)
        current_line = []
        current_width = 0

        for token in tokens:
            word = token.surface
            word_width = wcswidth(word)
            if word_width < 0:
                word_width = len(word)

            if current_width > 0 and current_width + word_width > max_width:
                if current_line and word in PROHIBIT_LINE_START_CHARS:
                    current_line.append(word)
                    lines.append("".join(current_line))
                    current_line = []
                    current_width = 0
                else:
                    lines.append("".join(current_line))
                    current_line = [word]
                    current_width = word_width
            else:
                current_line.append(word)
                current_width += word_width

        if current_line:
            lines.append("".join(current_line))

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "max_width",
        type=int,
        help="maximum display width per line (full-width=2, half-width=1)",
    )
    args = parser.parse_args()

    input_text = sys.stdin.read()
    wrapped_text = wrap_text(input_text, args.max_width)
    print(wrapped_text)


if __name__ == "__main__":
    main()
