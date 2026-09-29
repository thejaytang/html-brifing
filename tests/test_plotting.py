"""Exercise the bundled plotting resources, not a user's separately installed copy."""
import sys
import tempfile
import unittest
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'plugins/html-brifing/skills/academic-research-plotting/scripts'))
from research_plot_style import apply_academic_style, get_preset, figure_size
from export_figure import export_figure
from audit_figure import audit_figure


class BundledPlotting(unittest.TestCase):
    def tearDown(self):
        plt.close('all')

    def test_preset_and_style(self):
        apply_academic_style()
        self.assertEqual(plt.rcParams['axes.labelsize'], get_preset()['axis_label_size'])
        self.assertGreater(figure_size('double')[0], figure_size('single')[0])

    def test_png_svg_export(self):
        fig, ax = plt.subplots(layout='constrained')
        ax.plot([1, 2, 3], [4, 5, 7], marker='o')
        ax.set(xlabel='Example batch', ylabel='Observed items', title='Fictional packaging check')
        with tempfile.TemporaryDirectory() as tmp:
            files = export_figure(fig, Path(tmp) / 'figure', formats=('png', 'svg'))
            self.assertTrue(files[0].read_bytes().startswith(b'\x89PNG\r\n\x1a\n'))
            self.assertIn('<svg', files[1].read_text())
            self.assertIn('Observed items', files[1].read_text())

    def test_audit_catches_missing_labels(self):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [2, 3])
        self.assertTrue({'missing_xlabel', 'missing_ylabel'} <= {i.code for i in audit_figure(fig)})
        ax.set(xlabel='Batch', ylabel='Items')
        self.assertFalse({'missing_xlabel', 'missing_ylabel'} & {i.code for i in audit_figure(fig)})

    def test_unsupported_export_writes_nothing(self):
        fig, _ = plt.subplots()
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                export_figure(fig, Path(tmp) / 'figure', formats=('png', 'unsupported'))
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
