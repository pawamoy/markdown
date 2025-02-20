import timeit
import matplotlib.pyplot as plt
from importlib import reload
from pathlib import Path
import subprocess

from markdown import core, postprocessors


def benchmark(sizes):
    processor = reload(postprocessors).RawHtmlPostprocessor(md=reload(core).Markdown())

    empty_string = ""
    placeholders = "".join(f"\x02wzxhzdk:{i}\x03" for i in range(10))

    def process():
        processor.run(empty_string)
        processor.run(placeholders)

    results = []

    for size in sizes:
        print(f"Running benchmark for size {size}")
        processor.md.htmlStash.rawHtmlBlocks = ["<code>"] * size
        processor.md.htmlStash.html_counter = size
        time_taken = timeit.timeit(process, number=10) / 10  # Average over 10 runs
        results.append(time_taken)
        processor.md.reset()

    return results


sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000]

plt.figure(figsize=(10, 6))


print("Running benchmark for baseline")
plt.plot(sizes, benchmark(sizes), label="1-baseline")

for patch in sorted(Path(".").glob("*.patch")):
    print(f"Applying patch {patch}")
    subprocess.run(["git", "apply", str(patch)], check=True)
    plt.plot(sizes, benchmark(sizes), label=str(patch))

plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Benchmark: RawHTMLPostprocessor")
plt.legend()
plt.grid(True)
plt.show()
