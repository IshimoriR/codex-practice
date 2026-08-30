import unittest

import app


class DeleteTaskTest(unittest.TestCase):
    def setUp(self):
        app.tasks.clear()
        app.add_task("task 1")
        app.add_task("task 2")

    def test_deletes_task_at_valid_index(self):
        app.delete_task(0)

        self.assertEqual(
            app.tasks,
            [{"name": "task 2", "completed": False}],
        )

    def test_ignores_out_of_range_index(self):
        expected = app.tasks.copy()

        app.delete_task(99)
        app.delete_task(-1)

        self.assertEqual(app.tasks, expected)

    def test_ignores_bool(self):
        expected = app.tasks.copy()

        app.delete_task(True)
        app.delete_task(False)

        self.assertEqual(app.tasks, expected)

    def test_ignores_other_invalid_values(self):
        expected = app.tasks.copy()

        for value in (0.0, "0", None):
            with self.subTest(value=value):
                app.delete_task(value)
                self.assertEqual(app.tasks, expected)


if __name__ == "__main__":
    unittest.main()
