from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class HuggingFaceLLM:

    def __init__(self):

        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        print("Loading model...")
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype=torch.float32
        )

        print("Model loaded successfully!")

    def generate(self, prompt):

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True
        )

        output = self.model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=120,
            temperature=0.7,
            do_sample=True
        )

        generated = output[0][inputs["input_ids"].shape[-1]:]

        result = self.tokenizer.decode(
            generated,
            skip_special_tokens=True
        )

        return result