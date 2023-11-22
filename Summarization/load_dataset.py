# to load a dataset the chosen model will use

xsum_dataset = load_dataset(
    "xsum", version="1.2.0", cache_dir=DA.paths.datasets
)  # Note: We specify cache_dir to use predownloaded data.
xsum_sample = xsum_dataset["train"].select(range(10))
display(xsum_sample.to_pandas())
