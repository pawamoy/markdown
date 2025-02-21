import timeit
import matplotlib.pyplot as plt
from importlib import reload
from pathlib import Path
import subprocess
import random

from markdown import core, postprocessors

size = 5000


def benchmark(nesting_ratios):
    processor = reload(postprocessors).RawHtmlPostprocessor(md=reload(core).Markdown())

    results = []

    for ratio in nesting_ratios:
        print(f"Running benchmark with ratio {ratio}, stash size {size}")
        processor.md.htmlStash.rawHtmlBlocks = ["<code>"] * size
        processor.md.htmlStash.html_counter = size
        for _ in range(int(size * ratio)):
            index = random.choice(range(size))
            target = index + 3
            processor.md.htmlStash.rawHtmlBlocks[index] = f"<div>\x02wzxhzdk:{target}\x03</div>"
        placeholders = "".join(f"<p>\x02wzxhzdk:{i}\x03</p>" for i in range(size))
        time_taken = timeit.timeit(lambda: processor.run(placeholders), number=10) / 10  # Average over 10 runs
        results.append(time_taken)
        processor.md.reset()

    return results


ratios = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.22, 0.24, 0.26, 0.28, 0.3, 0.32, 0.34, 0.36, 0.38, 0.4, 0.42, 0.44, 0.46, 0.48, 0.5]

plt.figure(figsize=(10, 6))


print("Running benchmark for baseline")
plt.plot(ratios, benchmark(ratios), label="1-baseline")

for patch in sorted(Path(".").glob("*.patch")):
    print(f"Applying patch {patch}")
    subprocess.run(["git", "apply", str(patch)], check=True)
    plt.plot(ratios, benchmark(ratios), label=str(patch))

plt.xlabel(f"Placeholders nesting ratio (stash size: {size})")
plt.ylabel("Time (seconds)")
plt.title("Benchmark: RawHTMLPostprocessor")
plt.legend()
plt.grid(True)
plt.show()
