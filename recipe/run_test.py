import subprocess

def test_data_dir():
    ob_results = subprocess.run(
        [
            'obabel',
            '-:c1ccccc1',
            '-osmi',
            '-xt',
            '--append',
            'logP',
        ],
        capture_output=True
    )
    print(ob_results)
    assert b'Could not find contribution data file' not in ob_results.stderr
    print("Passed test_data_dir")

if __name__ == "__main__":
    test_data_dir()
