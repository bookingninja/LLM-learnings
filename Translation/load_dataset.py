jpn_dataset = load_dataset(
    "Helsinki-NLP/tatoeba_mt",
    version="1.0.0",
    language_pair="eng-jpn",
    cache_dir=DA.paths.datasets,
)
jpn_sample = (
    jpn_dataset["test"]
    .select(range(10))
    .rename_column("sourceString", "English")
    .rename_column("targetString", "Japanese")
    .remove_columns(["sourceLang", "targetlang"])
)
display(jpn_sample.to_pandas())
