# RL Scheduling Workflow

This directory contains the active reinforcement-learning workflow for DAG scheduling experiments. Build the simulator first from the repository root:

```bash
cmake -S . -B build
cmake --build build
```

Then run commands from `app/RL` so relative output paths are created in the expected locations.

## Main Entry Points

- `PPO_train.py`: run one PPO training configuration and append schedulability results to a CSV.
- `PPO_exp.py`: launch batches of `PPO_train.py` runs across selected seeds and utilization values.
- `dagedf.py`: EDF baseline for DAG tasks.
- `dagsjf.py`: SJF and RM baselines.
- `AJCT.py`: replay saved trajectories and compute response-time metrics.

Example single run:

```bash
python PPO_train.py --seed 14134 --uti 3.0 --episodes 500 --processor_config "0:2,7:2" --task_count 10
```

Example batch run:

```bash
python PPO_exp.py
```

## Core Modules

- `dagenv.py`: RL environment, processor request handling, rewards, task generation, and simulator-client interaction.
- `fused_graph.py`: converts current DAG task states into a fused PyTorch Geometric graph.
- `gnn.py`: actor/value GNN definitions.
- `PPO_agent.py`: PPO action sampling and update logic.
- `PPO_utils.py`: advantage calculation and optional plotting helpers.
- `PPO_inference.py`, `PPO_eval.py`: policy evaluation helpers.

## Data and Outputs

The `task_data*.pkl` files are startup data for Python-driven simulator workflows; keep them in place. Other `.pkl` files, `PPO_runs/`, `Rewards/`, `Schedule_list/`, `env_trajectory/`, `logs/`, and CSV outputs are generated experiment artifacts.
