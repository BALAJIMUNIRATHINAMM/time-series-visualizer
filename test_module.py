import unittest
import time_series_visualizer
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class TestTimeSeriesVisualizer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Load dataset once for all tests."""
        cls.df = pd.read_csv("data/fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
        lower_bound = cls.df["value"].quantile(0.025)
        upper_bound = cls.df["value"].quantile(0.975)
        cls.df = cls.df[(cls.df["value"] >= lower_bound) & (cls.df["value"] <= upper_bound)]

    def test_line_plot(self):
        """Test if the line plot is generated without errors."""
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_bar_plot(self):
        """Test if the bar plot is generated correctly."""
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)

    def test_box_plot(self):
        """Test if the box plots are generated correctly."""
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsInstance(fig, plt.Figure)
        plt.close(fig)


if __name__ == "__main__":
    unittest.main()
