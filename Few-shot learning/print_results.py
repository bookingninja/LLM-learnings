results = few_shot_pipeline(prompt, do_sample=True, eos_token_id=eos_token_id)

print(results[0]["generated_text"])
