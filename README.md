# Spin-Glass Chaos

This repository demonstrates chaotic renormalization group (RG) flows in the spin-glass phase, providing calculations for the Lyapunov exponent and the runaway exponent.

## Overview

In spin-glass systems, competing interactions between ferromagnetic and antiferromagnetic bonds lead to a highly frustrated magnetic state. These systems are particularly challenging due to their nontrivial ground states and chaotic behavior during renormalization. This project focuses on the study of chaotic RG flows in spin-glass phases, where the system exhibits unpredictable and complex behaviors as frustration increases.

This repo explores hierarchical Ising models, where both ferromagnetic and antiferromagnetic interactions are present. These models are exactly solvable and exhibit nonclassical phase transitions at finite temperatures. In this work, I use Ising models with a varying $s$-parameter, representing spin-s Ising models, where $s$ can take values such as $1/2$, $1$, $3/2$, $2$, $5/2$, etc.

## Key Features

- **Chaotic Renormalization Group Flows:** As frustration increases at low temperatures, chaotic trajectories emerge during the RG process, where correlations between spins evolve unpredictably at different length scales.
- **Lyapunov and Runaway Exponents**: Calculation of these exponents provides insights into the sensitivity to initial conditions and the stability of the RG flows.
- **Microscopic Description of Spin-Glass**: A detailed picture of the spin-glass phase is developed, showing how noncontiguous spins become pinned into distinct infinite subsets.

## Model Details

I study the competing interactions between ferromagnetic and antiferromagnetic bonds in hierarchical spin-s Ising models, which allow for exact solutions. The primary model parameters are $s$, representing spin number, and $p$, representing the concentration of antiferromagnetic bonds. As $p$ increases, the frustration in the system also increases, reaching a maximum at $p=0.5$.

### Key Observations:

- **Phase Transition:** As $p$ approaches $0.5$, the system undergoes a transition into a spin-glass phase at low temperatures.
- **Frustration:** The spin-glass phase is marked by maximum frustration due to the competing ferromagnetic and antiferromagnetic interactions.
- **Chaotic RG Flows:** In this phase, the RG trajectories exhibit chaotic behavior. Strong and weak spin correlations are encountered at successively larger length scales, in a seemingly random sequence.
- **Nonclassical Behavior:** Unlike classical phase transitions, the spin-glass phase transition occurs with no simple order parameter, and the system's behavior is driven by complex correlations over long distances.

## Exponents

- **Lyapunov Exponent:** Quantifies the chaotic nature of the RG flows, describing how small changes in initial conditions lead to diverging trajectories over the RG iterations. It quantifies how rapidly two infinitesimally close trajectories in the system's state space diverge over time. In the context of spin glasses, the Lyapunov exponent reflects the chaotic nature of the renormalization group (RG) flows. If the system has a positive Lyapunov exponent, small perturbations in the system's parameters can lead to large, unpredictable changes in the system's parameters or RG trajectory. This is a hallmark of the chaotic spin-glass phase.

- **Runaway Exponent:** Quantifies how fast the system is "running away" from a critical fixed point. A higher runaway exponent indicates a faster escape from the fixed point, reflecting a stronger divergence in the system's parameters. In a spin-glass system, a large runaway exponent corresponds to a highly unstable regime, where even small perturbations in the system (like bond concentration or temperature changes) lead to dramatic shifts in the behavior of the system, often resulting in chaotic or unpredictable spin correlations.

## Applications

This repository is valuable for researchers and students working on statistical mechanics, condensed matter physics, and complex systems. It provides a framework for studying chaotic systems using exact solutions and RG techniques.

## Installation and Usage

Clone the repository:
`git clone https://github.com/yourusername/spin-glass-chaos.git`

Navigate to the project directory:
`cd spin-glass-chaos`

Install the required dependencies:
`pip install -r requirements.txt`

Run the cells in spin-glass_chaos.ipynb playing with the parameters, and explore the RG behavior.

## Results

- Chaotic RG flow for spin number $s=1/2$ and the antiferromagnetic bond concentration $p=0.5$.
- Lyapunov exponent and runaway exponent calculations for maximum level of frustration, which occurs at $p=0.5$.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.