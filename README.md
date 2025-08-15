# word-wrap-ja

This tool wraps Japanese text based on visual width. It separates the
text using morphological analysis to maximize readability by avoiding
breaks in the middle of words.

## Example

    ollama run qwen3 "Write a short Japnaese paragraph" --hidethinking | word-wrap-ja 40
    朝の静けさが空を染める。風が木々の葉を
    揺らし、花の香りが心地よいリズムで届く。
    この瞬間、時間は止まり、心は自然の恵みに
    包まれる。
