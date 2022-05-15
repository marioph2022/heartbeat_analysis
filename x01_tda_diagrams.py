import numpy as np
import pandas as pd

from gtda.diagrams import PairwiseDistance
from gtda.diagrams import NumberOfPoints
from gtda.diagrams import PersistenceEntropy
from gtda.diagrams import NumberOfPoints
from gtda.diagrams import PersistenceEntropy
from gtda.diagrams import Silhouette

from gtda.diagrams import BettiCurve

class DiagramFeatures:

    diagrams = None

    def __init__(self, diagrams):
        self.diagrams = diagrams

    def get_barcode(self):
        nbr0 = self.diagrams.shape[0]
        nbr1 = self.diagrams.shape[1]
        nbr2 = self.diagrams.shape[2]
        df2 = pd.DataFrame(self.diagrams.reshape(-1, nbr1 * nbr2))
        drop_list = [df2[idx].name for idx in range(0, nbr1 * nbr2) if (df2[idx][0] == 0.0 or df2[idx][0] == 1.0)]
        df3 = df2.drop(drop_list, axis=1)
        return df3.values.reshape(nbr0, len(df3.columns), -1)

    # ----------------------------------------------
    # Get the betti curves from persistence homology
    # ----------------------------------------------
    def get_betti_areas(self):
        bc = BettiCurve()
        bc_repr = bc.fit_transform(self.diagrams)
        
        bc_area = []
        for idx in range(bc_repr.shape[0]):
            bc_area = self.compute_auc(bc.samplings_[0], bc_repr[idx])
            bc_area.append(bc_area)
        

    # ----------------------------------------------
    # compute the aprox area under the betti curve
    # ----------------------------------------------
    def compute_auc(radio_array, height_array):
        # compute the distance of each interval: this will be --> bc.samplings_[idx + 1] - bc.samplings_[idx], 0 <= idx <= 99
        radio_diff = np.delete(radio_array, 0) - np.delete(radio_array, -1)

        # compute the difference between two consecutive betti numbers:  this will be --> betti_curves[0][idx + 1] - betti_curves[0][idx], 0 <= idx <= 99 (the index of the curve will also vary from 0 to 100)
        betti_number_diff = np.delete(height_array.reshape(-1), -1) - np.delete(height_array.reshape(-1), 0)

        # compute the area of the upper triangles that are an approx to the betti curve
        triangle_area = np.multiply(radio_diff, betti_number_diff) * .5

        # compute the area of the rectangles that are under the betti curve
        rectangle_area = np.multiply(radio_diff, np.delete(height_array.reshape(-1), 0))
        return triangle_area + rectangle_area

    # -----------------------------------------------
    # Get the nbr of points from persistence homology
    # -----------------------------------------------
    def get_number_points(self):
        nbr_of_points = NumberOfPoints()
        nbr_of_points_repr = nbr_of_points.fit_transform(self.diagrams)
        return nbr_of_points_repr

    # ---------------------------
    # Get the persistence entropy
    # ---------------------------
    def get_entropy(self):
        entropy = PersistenceEntropy()
        entropy_repr = entropy.fit_transform(self.diagrams)
        return entropy_repr
        
    # ----------------------------------------------
    # Get the betti curves from persistence homology
    # ----------------------------------------------
    def get_silhouette(self):
        silhouette = Silhouette()
        silhouette_repr = silhouette.fit_transform(self.diagrams)
        return silhouette_repr
        

    # ---------------------------------------------------
    # Get the distance from persistence homology diagrams
    # --------------------------------------------------
    def get_pairwise_dst(self, metric_type):
        per_dst = PairwiseDistance(metric=metric_type, n_jobs=8)
        return per_dst.fit_transform(self.diagrams)







        

