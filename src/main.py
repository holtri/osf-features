from config import *
import pandas as pd
import numpy as np
import os
import subprocess
import glob
import logging
from sklearn.preprocessing import minmax_scale
import urllib.request


logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s')


def check_elki():
    if not os.path.isfile(ELKI_EXECUTABLE):
        logging.info(f"ELKI binary not found. Downloading from {ELKI_DOWNLOAD_URL}")
        urllib.request.urlretrieve(ELKI_DOWNLOAD_URL, ELKI_EXECUTABLE)
        logging.info(f"Saved to {ELKI_EXECUTABLE}")
    else:
        logging.info(f"Using ELKI binary {ELKI_EXECUTABLE}")


def calculate_osf(filename):
    if INCLUDE_RAW:
        raw = pd.read_csv(filename, header=None)
        labels = raw.iloc[:, -1]
        out = raw.iloc[:, 0:-1]
        out.columns = ["X" + str(x) for x in out.columns]
    else:
        out = pd.DataFrame()

    for k in K_RANGE:
        for name, cmd in algorithms.items():
            result = subprocess.run(
                ['java', '-jar', ELKI_EXECUTABLE, 'KDDCLIApplication', '-dbc.in', filename, '-time', '-algorithm', cmd['name'],
                 cmd['param'], str(k),
                 '-evaluator', 'NoAutomaticEvaluation', '-resulthandler', 'tutorial.outlier.SimpleScoreDumper'],
                stdout=subprocess.PIPE, universal_newlines=True)
            scores = [x.split(' ')[1] for x in result.stdout.split('\n')[0:-1] if not x.startswith("de")]
            scores = np.where(np.array(scores) == 'Infinity', np.nan, np.array(scores)).astype('float64')
            scores[np.isnan(scores)] = np.nanmax(scores)
            out[name + "-" + str(k)] = minmax_scale(scores) if NORMALIZE_OSF else scores
    out['label'] = labels
    return out


def process_file(file):
    logging.info(f"Processing '{file}'")
    output = calculate_osf(file)
    input_path, input_file = os.path.split(file)
    output_file = input_file.split(".")[0] + '_OSF.csv'
    output_dir = os.path.join(OUTPUT_ROOT, input_path.split(os.sep)[-1])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output.to_csv(output_dir + os.sep + output_file, index=False)


def main():
    check_elki()
    logging.info(f"Processing files in '{INPUT_ROOT}'.")
    logging.info(f"Output into '{OUTPUT_ROOT}'.")
    logging.info(f"Include input attributes: '{INCLUDE_RAW}'.")
    logging.info(f"Normalize OSF: '{NORMALIZE_OSF}'.")

    os.makedirs(os.path.join(OUTPUT_ROOT, ''), exist_ok=True)

    for file in [f for f in glob.glob(os.path.join(INPUT_ROOT, '**', '*.csv'), recursive=True)]:
        process_file(file)


if __name__ == "__main__":
    main()