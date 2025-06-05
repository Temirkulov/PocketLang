"""Command line interface for PocketLang translator."""

import argparse

from .translator import Translator


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline translator using pretrained models")
    parser.add_argument("model", help="Path to the local translation model directory")
    parser.add_argument("text", help="Text to translate")
    parser.add_argument(
        "--max-length", type=int, default=512, help="Maximum translation length"
    )
    args = parser.parse_args()

    translator = Translator(args.model)
    translation = translator.translate(args.text, max_length=args.max_length)
    print(translation)


if __name__ == "__main__":
    main()
