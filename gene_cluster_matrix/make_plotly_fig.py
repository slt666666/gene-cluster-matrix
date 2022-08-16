import itertools
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots

from .make_tree import make_tree_figure


# Following functions generate gene cluster matrix by heatmap object of plotly.
# The distance between genes is expressed by the color of heatmap.
# If tree file is provided, the image of tree is displayed in top and left side of heatmap.
# heatmap() function generate basic matrix of gene clusters.
# heatmap_with_tree() function generate matrix of gene clusters and tree images.

def heatmap_object(z_data, text, order):
    # parameters of heatmap
    params = dict(
        x=order,
        y=order[::-1],
        z=z_data,
        text=text,
        hoverinfo="text",
        colorscale="Reds",
        reversescale=True,
        colorbar=dict(
            len=0.7,
            title=dict(
                text='distance',
            ),
            yanchor="bottom",
            y=0
        ),
    )
    # generate heatmap object
    trace = go.Heatmap(params)
    return trace

def line_object(clade, x, y):
    # add separate lines of clade
    lines = []
    gene_num = clade.shape[0]
    start = -0.5
    for k, g in itertools.groupby(clade.values):
        # calculate position of each line
        start += len(list(g))
        # vertical lines
        lines.append(
            dict(
                type="line",
                xref=x,
                yref=y,
                x0=start,
                y0=-0.5,
                x1=start,
                y1=gene_num-0.5,
                opacity=0.5,
                line=dict(
                    color="gray",
                    width=0.5
                )
            )
        )
        # horizontal lines
        lines.append(
            dict(
                type="line",
                xref=x,
                yref=y,
                x0=-0.5,
                y0=gene_num-1-start,
                x1=gene_num-0.5,
                y1=gene_num-1-start,
                opacity=0.75,
                line=dict(
                    color="gray",
                    width=0.5
                )
            )
        )
    return lines

def heatmap(z_data, text, order, out, clade):
    # generate heatmap object
    trace = heatmap_object(z_data, text, order)
    data = [trace]

    # setting layout for basic heatmap
    layout = go.Layout(
        margin=dict(
            l=130,
            t=160
        ),
        width=750,
        height=750,
        autosize=False,
        xaxis=dict(
            mirror="allticks",
            side="top",
            showgrid=False,
            tickfont=dict(
                size=8
            )
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(
                size=8
            )
        ),
    )

    # generate Figure object
    fig = go.Figure(
        data=data,
        layout=layout
    )

    # add clade separate lines
    if clade != None:
        clade_df = pd.read_csv(clade, index_col=0)
        lines = line_object(clade_df.loc[order, :], "x", "y")
        fig.update_layout(shapes=lines)

    # generate html file
    plot(fig, filename="{}.html".format(out))

def heatmap_with_tree(z_data, text, order, out, tree, clade):

    # generate heatmap object
    trace = heatmap_object(z_data, text, order)
    data = [trace]

    # generate 2x2 subplots
    fig = make_subplots(
        rows=2, cols=2,
        row_heights=[0.2, 0.8],
        column_widths=[0.2, 0.8],
        horizontal_spacing=0.1*max([len(i) for i in order])/16,
        vertical_spacing=0.11*max([len(i) for i in order])/16,
        shared_xaxes=True,
        shared_yaxes=True,
    )

    # add figure [1,1]
    fig.add_trace(
        go.Scatter(x=np.array([0,1]), y=np.array([0,1]), opacity=0, hoverinfo="none"),
        row=1, col=1
    )
    # add figure [1,2]
    fig.add_trace(
        go.Scatter(x=order, y=np.repeat(0, len(order)), opacity=0, hoverinfo="none", visible='legendonly'),
        row=1, col=2
    )
    # add figure [2,1]
    fig.add_trace(
        go.Scatter(x=np.repeat(0, len(order)), y=order, opacity=0, hoverinfo="none", visible='legendonly'),
        row=2, col=1
    )
    # add matrix [2,2]
    fig.add_trace(trace, row=2, col=2)

    # setting layout for subplots of matrix and trees
    layout = go.Layout(
        margin=dict(
            l=0,
            t=0,
        ),
        width=750,
        height=750,
        autosize=False,
        xaxis4=dict(
            mirror="allticks",
            side="top",
            showgrid=False,
            tickfont=dict(
                size=8
            ),
            automargin=False,
        ),
        yaxis4=dict(
            showgrid=False,
            tickfont=dict(
                size=8
            ),
            side="left",
            automargin=False,
        ),
        plot_bgcolor="white",
        showlegend=False,
    )
    fig.update_layout(layout)

    # generate png image file of phylogenetic tree
    top_tree, left_tree = make_tree_figure(tree, out, clade)
    # add top tree
    fig.add_layout_image(
        dict(
            source=top_tree,
            xref="x2", yref="y2",
            x=-0.5, y=0,
            sizex=len(order), sizey=len(order),
            xanchor="left", yanchor="bottom",
            layer="above",
        )
    )
    # add left tree
    fig.add_layout_image(
        dict(
            source=left_tree,
            xref="x3", yref="y3",
            x=1, y=-0.5,
            sizex=len(order), sizey=len(order),
            xanchor="right", yanchor="bottom",
            layer="above",
        )
    )

    # show only ticklabels in [2, 2] subplot.
    fig.update_layout(xaxis_showticklabels=False, xaxis2_showticklabels=False, xaxis3_showticklabels=False, xaxis4_showticklabels=True)
    fig.update_layout(yaxis_showticklabels=False, yaxis2_showticklabels=False, yaxis3_showticklabels=False, yaxis4_showticklabels=True)

    # add clade separate lines
    if clade != None:
        clade_df = pd.read_csv(clade, index_col=0)
        lines = line_object(clade_df.loc[order, :], "x4", "y4")
        fig.update_layout(shapes=lines)

    # generate html output file
    plot(fig, filename="{}_with_tree.html".format(out))