import numpy as np
import pandas as pd
import altair as alt

alt.data_transformers.disable_max_rows()
def create_state_visualization(vals, slider_label="Iteration"):
    """
    Create state visualization for hopfield network

    Parameters
    ----------
    vals : array-like
        The states to be visualized in the heatmap provided in a list.

    Returns
    -------
    alt.Chart
        An Altair heatmap chart object.
    """

    n_iters = len(vals)
    n_vals_per_iter = len(vals[0])
    size = int(np.sqrt(n_vals_per_iter))
    iters = np.repeat(np.arange(n_iters), n_vals_per_iter)
    cols = np.tile(np.repeat(np.arange(size), size), n_iters)
    rows = np.tile(np.tile(np.arange(size), size), n_iters)
    flattened = [v for vs in vals for v in vs]

    if n_iters > 1:
        # Create a DataFrame from the data
        df = pd.DataFrame({"x": cols, "y": rows, "value": flattened, "iteration": iters})

        # Create a slider selection
        slider = alt.binding_range(min=0, max=n_iters-1, step=1, name=f"{slider_label}: ")
        selector = alt.param(name="SelectorName", bind=slider, value=0)

        # Create the heatmap
        heatmap = (
            alt.Chart(df)
            .mark_rect()
            .encode(
                x=alt.X("x:O", axis=None),
                y=alt.Y("y:O", axis=None),
                color=alt.Color("value:Q", scale=alt.Scale(scheme="viridis"), legend=None),
            )
            .add_params(selector)
            .transform_filter(alt.datum.iteration == selector)
            .properties(width=400, height=400)
        )
    else:
        # Create a DataFrame from the data
        df = pd.DataFrame(
            {"x": cols, "y": rows, "value": flattened}
        )

        # Create the heatmap
        heatmap = (
            alt.Chart(df)
            .mark_rect()
            .encode(
                x=alt.X("x:O", axis=None),
                y=alt.Y("y:O", axis=None),
                color=alt.Color(
                    "value:Q", scale=alt.Scale(scheme="viridis"), legend=None
                ),
            )
            .properties(width=400, height=400)
        )

    return heatmap
