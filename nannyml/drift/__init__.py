#  Author:   Niels Nuyttens  <niels@nannyml.com>
#
#  License: Apache Software License 2.0

"""NannyML drift calculation module.

This module currently contains the following implementations of drift calculation:

- Statistical drift calculation: calculation using Kolmogorov-Smirnov test for continuous samples and Chi-squared test
for nominal categorical tests.

"""

from ._base import BaseDriftCalculator, DriftCalculator
from .statistical_drift_calculator import StatisticalDriftCalculator
