import os, re, threading

_NOISE = [
    r"is not a recognized feature for this target",
    r"Unable to register cuFFT factory",
    r"Unable to register cuDNN factory",
    r"Unable to register cuBLAS factory",
    r"computation placer already registered",
    r"All log messages before absl::InitializeLog",
    r"could not open file to read NUMA node",
    r"Your kernel may have been built without NUMA support",
    r"Could not identify NUMA node",
    r"TF-TRT Warning",
    r"This TensorFlow binary is optimized",
    r"To enable the following instructions",
    r"ptxas warning",
    r"Registers are spilled to local memory",
    r"XLA service",
    r"StreamExecutor device",
    r"disabling MLIR crash reproducer",
    r"Loaded cuDNN version",
    r"Compiled cluster using XLA",
    r"service\.cc:",
    r"Created device .*with .* memory",
    r"successful NUMA node read",
    r"Skipping the delay kernel",
    r"measurement accuracy will be reduced",
    r"gpu_timer\.cc",
]
_pats = [re.compile(p) for p in _NOISE]

_saved = os.dup(2)
_r, _w = os.pipe()
os.dup2(_w, 2)
os.close(_w)

def _pump():
    real = os.fdopen(_saved, 'w')
    buf = b''
    with os.fdopen(_r, 'rb') as rf:
        while True:
            chunk = rf.read(1)
            if not chunk:
                break
            buf += chunk
            if chunk == b'\n':
                line = buf.decode(errors='replace')
                if not any(p.search(line) for p in _pats):
                    real.write(line); real.flush()
                buf = b''

threading.Thread(target=_pump, daemon=True).start()
