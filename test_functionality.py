import unittest
import io
import algorithm

class AlgorithmTest(unittest.TestCase):

  def test_functionality(self):
    # Create a mock user input string.

    mock_user_input = "0.5, 1, 1.5, 2, 2.5"

    # Create a mock stdout object.

    mock_stdout = io.StringIO()

    # Patch the `input()` function to return the mock user input string.

    with unittest.mock.patch("builtins.input", return_value=mock_user_input):
      # Call the `algorithm.py` file.

      algorithm.main()

    # Get the output from the mock stdout object.

    actual_output = mock_stdout.getvalue()

    # Check that the output contains the expected periodic times.

    expected_output = """
[0.5, 1, 1.5, 2, 2.5]
[1.5707963267948966, 3.141592653589793, 4.71238898038469, 6.283185307179586, 7.853981633974483]
"""

    self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
  unittest.main()
