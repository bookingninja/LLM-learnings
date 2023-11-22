few_shot_pipeline = pipeline(
    task="text-generation",
    model="EleutherAI/gpt-neo-1.3B",
    max_new_tokens=50,
    model_kwargs={"cache_dir": DA.paths.datasets},
)  # Uses a predownloaded model

# Get the token ID for "###", which we will use as the EOS token below.  (Recall we did this in the demo notebook.)
eos_token_id = few_shot_pipeline.tokenizer.encode("###")[0]
