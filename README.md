# UAV_Deconfliction

This project aims to address the problem of UAV (Unmanned Aerial Vehicle) deconfliction, ensuring safe and efficient operation of multiple UAVs in shared airspace.

To run the application:
1. open command prompt and change directory to 'src'
2. run command 'python main.py'

## Project Structure

- `config/`  
  - `config.py` – Configuration parameters for UAVs and simulation.
- `src/`  
  - `main.py` – Main entry point for the UAV deconfliction system.
  - `collision_detection.py` – Collision detection logic and utilities.
  - `handle_input_data.py` – Handles input data for primary UAV.
  - `simulationUavDB.py` – Simulation UAV data definitions.
  - `waypoint_plot.py` – 3D plotting of UAV paths.
- `uav_info_def/`  
  - `__init__.py` – Package initializer for UAV info definitions.
  - `uav_info.py` – UAV data structures (position, time window, etc.).
- `test/`  
  - `test_main.py` – Unit tests for main functionality.
- `uav_deconfliction_research.txt` – Research content and references.
- `architecture design decision.pptx` – Architecture and design documentation.


