"""Simple offline translation utilities."""

from pathlib import Path
from typing import Optional

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Translator:
    """Load a HuggingFace translation model for offline use."""

    def __init__(self, model_dir: str):
        self.model_dir = Path(model_dir)
        if not self.model_dir.exists():
            raise FileNotFoundError(
                f"Model directory '{self.model_dir}' does not exist."
            )
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_dir)

    def translate(self, text: str, max_length: Optional[int] = 512) -> str:
        """Translate a single piece of text."""
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
