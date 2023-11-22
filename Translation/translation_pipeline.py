# To use a model to translate from Japanese to English. This example creates a pipeline using an existing LLM anb then applies the pipeline to the sample batch of Japanese sentences.

# Construct a pipeline for translating Japanese to English.
translation_pipeline = pipeline(
  task="translation",
  model="Helsinki-NLP/opus-mt-jap-en",
)

# Apply your pipeline on the sample of Japanese text in: jpn_sample["Japanese"]
translation_results = translation_pipeline(jpn_sample["Japanese"])
