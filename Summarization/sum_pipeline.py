#  to create a pipeline using an existing LLM and then apply the pipeline to the sample batch of articles in 'xsum_sample'

# Constructor a summarization pipeline
summarizer = pipeline(
  task="summarization",
  model="google/pegasus-xsum",
  min_length=20,
  max_length=40,
  truncation=True,
)

# Apply the pipeline to the batch of articles in `xsum_sample`
summarization_results = summarizer(xsum_sample["document"])
summarization_results
