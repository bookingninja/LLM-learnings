def display_summaries(decoded_summaries: list) -> None:
    """Helper method to display ground-truth and generated summaries side-by-side"""
    results_df = pd.DataFrame(zip(xsum_sample["summary"], decoded_summaries))
    results_df.columns = ["Summary", "Generated"]
    display(results_df)
