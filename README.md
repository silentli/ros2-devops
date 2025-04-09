# ros2-devops

The project includes a sample ROS2 publisher node, a Prometheus exporter node that listens to ROS topics, and a Prometheus server to scrape and display metrics.

## Features

- ROS2 Humble environment with Python-based nodes
- `talker` node that publishes random integers to `/random_number`
- `ros_exporter` node that subscribes to `/random_number` and exposes it as a Prometheus metric
- Prometheus server with configurable scrape interval


## File Structure

```text
ros2-devops/
├── ros2_ws/                    # ROS2 workspace
│   └── src/
│       └── demo_package/       # ROS2 Python package
│           ├── demo_package/   # Python module
│           │   ├── talker.py
│           │   └── __init__.py
│           └── ...
├── monitoring/                 # Prometheus exporter script
│   └── ros_exporter.py
├── prometheus/                 # Prometheus configuration
│   └── prometheus.yml
├── docker/                     # Dockerfiles and entrypoint
│   ├── Dockerfile.ros_node
│   ├── Dockerfile.ros_exporter
│   └── entrypoint.sh
├── compose.yaml
└── README.md
```

## Getting Started

### Prerequisites

- Docker

### Build and Run

Clone the repository and start the services:

```bash
cd ros2-devops
docker compose up --build
```

The Prometheus server, available at http://localhost:9090

