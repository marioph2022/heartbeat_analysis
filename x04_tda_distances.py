import pandas as pd
from gtda.diagrams import PairwiseDistance

class DistanceMatrix:

    def compute_pw_distance(self, metric, diagrams):
        days_limit = diagrams.shape[0] + 1

        # PairwiseDistance(metric='landscape', metric_params=None, order=2.0, n_jobs=None)
        pw_dst = PairwiseDistance(metric=metric, n_jobs=10)
        
        df_dst = pd.DataFrame(pw_dst.fit_transform(diagrams), columns=[x for x in range(1,days_limit)])
        
        return pw_dst, df_dst