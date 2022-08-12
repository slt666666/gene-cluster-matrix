import plotly.graph_objs as go
from plotly.offline import plot


def heatmap(z_data, text, order, out, tree_file=None):
    ### base of heatmap
    params = dict(
        x=order,
        y=order[::-1],
        z=z_data,
        text=text,
        hoverinfo="text"
    )

    ### additional parameters of heatmap
    parameters = dict(
            colorscale="Reds",
            reversescale=True
        )
    params.update(parameters)

    trace = go.Heatmap(params)
    data = [trace]

    # ### add separate lines of clade
    # lines, colorlist = [], []
    # gene_num = NLR_clades.shape[0]
    # start = -0.5
    # for i, each_clade in enumerate(NLR_clades.clade.unique()):

    #     ### color list of clade line
    #     colorlist.append("rgb"+str(tuple(np.random.random(size=3)*256)))

    #     start += NLR_clades.clade.value_counts()[each_clade]

    #     ### vertical lines
    #     lines.append(
    #         dict(
    #             type="line",
    #             xref="x",
    #             yref="y",
    #             x0=start,
    #             y0=-0.5,
    #             x1=start,
    #             y1=gene_num-0.5,
    #             opacity=0.5,
    #             line=dict(
    #                 color="gray", #colorlist[i],
    #                 width=0.5
    #             )
    #         )
    #     )
    #     lines.append(
    #         dict(
    #             type="line",
    #             xref="x",
    #             yref="y",
    #             x0=-0.5,
    #             y0=gene_num-1-start,
    #             x1=gene_num-0.5,
    #             y1=gene_num-1-start,
    #             opacity=0.75,
    #             line=dict(
    #                 color="gray", #colorlist[i],
    #                 width=0.5
    #             )
    #         )
    #     )

    ### setting layout
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
    #     shapes=lines
    )

    fig = go.Figure(
        data=data,
        layout=layout
    )

    ### draw
    fig.show()
    plot(fig, filename="../data/Tomato_NLR_cluster.html")