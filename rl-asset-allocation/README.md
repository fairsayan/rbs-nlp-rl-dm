# Reinforcement Learning for Asset Allocation Lab

## Overview
This laboratory demonstrates how to use Reinforcement Learning (RL) to create an intelligent agent that learns optimal portfolio allocation strategies. The agent learns to maximize cumulative returns while considering risk, transaction costs, and market dynamics.

## Objectives
- Understand the difference between supervised learning and RL in finance
- Implement a custom trading environment using OpenAI Gym
- Train an RL agent using stable-baselines3 algorithms
- Compare RL performance against traditional baseline strategies
- Analyze risk-adjusted returns and transaction costs

## Key Concepts
- **Sequential Decision Making**: Unlike supervised learning, RL agents make decisions over time
- **Portfolio Allocation**: Dynamically adjusting asset weights based on market conditions
- **Risk Management**: Balancing returns with volatility and drawdown
- **Transaction Costs**: Realistic modeling of trading friction

## Environment Setup
The notebook uses a custom portfolio management environment where:
- **State**: Current prices, portfolio weights, technical indicators
- **Actions**: New allocation percentages across assets
- **Rewards**: Risk-adjusted returns minus transaction costs

## Assets Analyzed
- SPY (S&P 500 ETF)
- AAPL (Apple Inc.)
- MSFT (Microsoft Corp.)
- GOOGL (Alphabet Inc.)

## Algorithms Used
- **PPO (Proximal Policy Optimization)**: Main RL algorithm
- **DQN (Deep Q-Network)**: Alternative approach for comparison
- **Baseline Strategies**: Buy-and-hold, Equal weight portfolio

## Key Features
- Real market data from Yahoo Finance
- Custom trading environment with realistic constraints
- Transaction cost modeling
- Comprehensive performance metrics (Sharpe ratio, max drawdown)
- Interactive visualizations of portfolio evolution
- Out-of-sample testing to avoid overfitting

## Requirements
See the main repository requirements.txt for dependencies.

## Usage
Run the notebook cells sequentially to:
1. Load and preprocess market data
2. Set up the trading environment
3. Train the RL agent
4. Evaluate performance against baselines
5. Visualize results and analyze strategies
