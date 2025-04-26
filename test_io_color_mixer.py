import unittest
import subprocess
import sys

class TestColorMixerIO(unittest.TestCase):

    def run_program(self, inputs):
        """Helper to run the student program with provided input and return output."""
        result = subprocess.run(
            [sys.executable, "color_mixer.py"],
            input="\n".join(inputs),
            capture_output=True,
            text=True
        )
        return result.stdout

    def test_word_input_red_yellow(self):
        output = self.run_program(["word", "red", "yellow"])
        self.assertIn("resulting color is orange", output)

    def test_word_input_blue_yellow(self):
        output = self.run_program(["word", "blue", "yellow"])
        self.assertIn("resulting color is green", output)

    def test_word_input_same_color(self):
        output = self.run_program(["word", "red", "red"])
        self.assertIn("COLOR1 AND COLOR2 CANNOT BE THE SAME!", output)

    def test_word_input_invalid_first_color(self):
        output = self.run_program(["word", "grey", "blue"])
        self.assertIn("COLOR 1 CHOICE INVALID - PROGRAM ENDING!", output)

    def test_word_input_invalid_second_color(self):
        output = self.run_program(["word", "red", "orange"])
        self.assertIn("COLOR 2 CHOICE INVALID - PROGRAM ENDING!", output)

    def test_number_input_valid(self):
        output = self.run_program(["number", "2", "3"])
        self.assertIn("resulting color is green", output)

    def test_number_input_same_color(self):
        output = self.run_program(["number", "1", "1"])
        self.assertIn("COLOR1 AND COLOR2 CANNOT BE THE SAME!", output)

    def test_number_input_invalid_choice(self):
        output = self.run_program(["number", "4", "1"])
        self.assertIn("COLOR 1 CHOICE INVALID - PROGRAM ENDING!", output)

    def test_invalid_input_type(self):
        output = self.run_program(["letters"])
        self.assertIn("INVALID INPUT TYPE - PROGRAM ENDING!", output)

if __name__ == "__main__":
    unittest.main()
