# To display the translation results side-by-side with the ground-truth `English` column from the dataset.

translation_results_df = pd.DataFrame.from_dict(translation_results).join(
    jpn_sample.to_pandas()
)
display(translation_results_df)
