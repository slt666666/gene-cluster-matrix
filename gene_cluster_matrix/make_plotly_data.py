import numpy as np
import pandas as pd

def calc_distance(position, order):
    
    # extract id order before sort by position
    position = position.sort_values(by=["chr", "start"])
    pos_ids = position.id.values

    # make matrices of start position & end position
    chrs = position["chr"].values
    dim = position.shape[0]
    start_position = position.loc[:, "start"]
    end_position = position.loc[:, "end"]
    start_matrix = np.repeat(np.array(start_position), dim).reshape(dim, dim).T
    end_matrix = np.repeat(np.array(end_position), dim).reshape(dim, dim)

    # make distance matrix, and distance between overlap genes (distance < 0) convert to 0
    distance = start_matrix - end_matrix
    distance = np.triu(distance, 1)
    distance = np.where(distance > 0, distance, 0)
    distance = pd.DataFrame(distance, index=chrs, columns=chrs)

    # set np.nan to diffrent chromosome gene pair
    for each_chr in distance.columns:
        distance.loc[distance.index != each_chr, each_chr] = np.nan

    distance = np.array(distance)
    distance[np.diag_indices(distance.shape[0])] = np.nan
    distance = distance + distance.T
    distance = np.flip(distance, 0)

    # ordered by id order
    distance = pd.DataFrame(distance, index=pos_ids[::-1], columns=pos_ids)
    distance = distance.loc[order[::-1], order]

    return distance

def heatmap_matrix(distance, threshold):
    z_data = np.array(distance)
    z_data[np.isnan(z_data)] = threshold
    z_data[z_data > threshold] = threshold
    return z_data

def hover_text(distance, order):
    hovertext = list()
    for yi, yy in enumerate(order[::-1]):
        hovertext.append(list())
        for xi, xx in enumerate(order):
            ### basic hover text
            hovertext[-1].append('1: {}<br />2: {}<br />Distance: {}'.format(
                    yy,
                    xx,
                    distance.iloc[yi, xi]
                )
            )
    hovertext = np.array(hovertext)
    return hovertext