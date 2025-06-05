# PocketLang

PocketLang is a simple offline language translation tool. It uses
pre-trained machine translation models from HuggingFace that can be
stored locally for completely offline usage.

## Installation

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Download a translation model from HuggingFace and place it somewhere
   on your system. For example, to translate from English to German you
   can download `Helsinki-NLP/opus-mt-en-de`:
   ```bash
   transformers-cli download Helsinki-NLP/opus-mt-en-de
   ```
   After downloading, you can copy the model directory to your offline
   machine.

## Usage

Run the CLI with the path to the local model directory and the text you
want to translate:

```bash
python -m pocketlang.cli /path/to/model "Hello, world"
```

The translated text will be printed to the terminal.

## Library Usage

PocketLang can also be used as a Python library:

```python
from pocketlang import Translator

translator = Translator('/path/to/model')
print(translator.translate('Hello, world'))
```
