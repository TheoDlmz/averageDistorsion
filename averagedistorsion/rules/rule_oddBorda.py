import numpy as np
from averagedistorsion.rules.rule_ranking import RuleRanking
from averagedistorsion.utils.cached import DeleteCacheMixin, cached_property


class RuleOddBorda(RuleRanking):
    """
    The OddBorda rule
    """

    name = "OddBorda"

    @cached_property
    def ranking_(self):
        n, m = self.matrix_.shape
        score = np.zeros(m)
        for row in self.matrix_:
            r = np.argsort(row)
            for i in range(1, m):
                score[r[i]] += 2*i-1

        return np.argsort(score)[::-1]
