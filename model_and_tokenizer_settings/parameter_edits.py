##############################################################################
# TODO: Try editing the parameters in this section, and see how they affect the results.
#       You can also copy and edit the cell to compare results across different parameter settings.
#
# We show all parameter settings for ease-of-modification, but in practice, you would only set relevant ones.
inputs = tokenizer(
    articles, max_length=1024, return_tensors="pt", padding=True, truncation=True
)

summary_ids = model.generate(
    inputs.input_ids,
    attention_mask=inputs.attention_mask,
    do_sample=True,
    num_beams=2,
    min_length=0,
    max_length=40,
    top_k=20,
    top_p=0.5,
    temperature=0.7,
)

decoded_summaries = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)
##############################################################################

display_summaries(decoded_summaries)
