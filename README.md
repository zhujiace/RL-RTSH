# HeterSchedulerSim

Temporal scheduling simulator for heterogeneous real-time workloads, with a reinforcement-learning workflow for DAG scheduling experiments.

## Repository Layout

- `src/`: simulator implementation and Python client bindings. This is the simulator layer; avoid changing it unless a simulator feature or API change is explicitly required.
- `test/`: C++ executable entry point for the simulator command interface.
- `app/RL/`: main reinforcement-learning code and experiment scripts.
- `app/RL/task_data*.pkl`: startup data used by Python-driven simulator workflows. Keep these files in place.

## Build the Simulator

```bash
cmake -S . -B build
cmake --build build
```

The build produces `build/main`, which is used directly by the Python RL environment.

## Simulator Interactive Usage

```bash
./build/main int
```

Available command groups include:

| Type | Commands |
| --- | --- |
| query | `queryCurrentTimeStamp`, `queryProcessorStates`, `queryTaskExecutionStates`, `queryTaskState`, `querySSTaskStates`, `doesTaskMissDeadline` |
| control | `startSimulation`, `updateProcessorAndTask`, `setSimulationTimeBound`, `quit` |
| schedule | `createProcessor`, `createHeterSSTask`, `scheduleSegmentOnProcessor` |

## Reinforcement Learning Workflow

Run RL commands from `app/RL` after building the simulator:

```bash
cd app/RL
python PPO_train.py --seed 14134 --uti 3.0 --episodes 500 --processor_config "0:2,7:2" --task_count 10
```

Main RL files:

- `PPO_train.py`: single PPO training run.
- `PPO_exp.py`: batch experiments that launch `PPO_train.py`.
- `dagenv.py`: DAG scheduling environment backed by `build/main`.
- `fused_graph.py`, `gnn.py`, `PPO_agent.py`: graph construction, GNN policy/value models, and PPO updates.
- `dagedf.py`, `dagsjf.py`: EDF/SJF/RM baseline schedulers.
- `AJCT.py`: average job completion/response-time analysis for saved schedules.

Generated CSVs, TensorBoard runs, reward plots, logs, and schedule traces are experiment outputs and should stay out of the main code path.
