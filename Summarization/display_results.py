# To display the generated summary side-by-side with the reference summary and original document.

import pandas as pd

display(
    pd.DataFrame.from_dict(summarization_results)
    .rename({"summary_text": "generated_summary"}, axis=1)
    .join(pd.DataFrame.from_dict(xsum_sample))[
        ["generated_summary", "summary", "document"]
    ]
)
