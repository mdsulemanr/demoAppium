import unittest
import HtmlTestRunner

if __name__ == '__main__':
    # Discover tests from files starting with test_*.py
    test_suite = unittest.defaultTestLoader.discover('.', pattern='test_*.py')

    # Run tests and generate HTML report
    runner = HtmlTestRunner.HTMLTestRunner(
        output='reports',
        report_name='CalculatorTestReport',
        combine_reports=True,
        add_timestamp=True
    )
    runner.run(test_suite)
