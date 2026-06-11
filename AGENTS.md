# Repository Guidelines

## Project Structure & Module Organization

This repository contains a heterogeneous scheduling simulator with C++ core code and Python experiment drivers. Core simulator classes live in `src/cpp/` (`simulator`, `scheduler`, `processor`, `task`, and `segment`). The executable entry point is `test/main.cpp`, which builds into `build/main`. Python scheduler examples and utilities are in `src/python/`. Benchmark scripts are under `app/benchmark/`; RL environments, PPO training code, CSVs, plots, and saved schedules are under `app/RL/`. Avoid committing cache files or local build artifacts.

## Build, Test, and Development Commands

- `cmake -S . -B build`: configure the C++ project and generate build files.
- `cmake --build build`: compile the `main` executable from `src/cpp/*.cpp` and `test/main.cpp`.
- `./build/main int`: start the interactive simulator command interface.
- `python src/python/scheduler.py`: run the Python scheduling example against `build/main`.
- `python app/benchmark/driver.py -algo rm -u 20 -c 2 -e 2 -g 2 -o results.csv`: run one benchmark configuration.

Build before running Python clients that spawn the simulator.

## Coding Style & Naming Conventions

C++ uses C++20. Follow the existing brace style, four-space indentation, and class-oriented file pairing (`processor.h`/`processor.cpp`). Use existing simulator names such as `Task`, `Processor`, `Segment`, and typed aliases from headers. Python follows PEP 8 with four-space indentation; keep experiment entry points explicit through `argparse`. There is no configured formatter or linter, so keep edits consistent with nearby code.

## Testing Guidelines

There is no formal unit-test framework. Treat `cmake --build build` as the minimum compile check. For behavior changes, run an interactive or scripted simulation and record the exact command and workload. Add C++ regression harnesses under `test/` when practical, and keep Python checks small enough to reproduce without long RL training runs.

## Commit & Pull Request Guidelines

Recent history uses short imperative messages, sometimes with Conventional Commit prefixes, such as `fix reward shaping`, `feat: dag environment and agent`, and `add noop penalty`. Prefer `feat:`, `fix:`, or a concise imperative phrase. Pull requests should describe changed scheduler behavior, list verification commands, call out generated data files, and link related issues or experiment notes.

## Security & Configuration Tips

Avoid hard-coded absolute paths in new code; prefer paths relative to the repository root or script directory. Do not commit large transient outputs from `PPO_runs/`, `Rewards/`, logs, checkpoints, or caches unless they are required evidence for a specific experiment.
