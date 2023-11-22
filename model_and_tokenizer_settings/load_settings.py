# Load data, tokenizer, and model.

from transformers import T5Tokenizer, T5ForConditionalGeneration

xsum_dataset = load_dataset("xsum", version="1.2.0", cache_dir=DA.paths.datasets)
xsum_sample = xsum_dataset["train"].select(range(10))

tokenizer = T5Tokenizer.from_pretrained("t5-small", cache_dir=DA.paths.datasets)
model = T5ForConditionalGeneration.from_pretrained(
    "t5-small", cache_dir=DA.paths.datasets
)

# Prepare articles for T5, which requires a "summarize: " prefix.
articles = list(map(lambda article: "summarize: " + article, xsum_sample["document"]))
