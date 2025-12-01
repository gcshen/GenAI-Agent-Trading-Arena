# Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents

<div align="center">

[[arXiv]](https://arxiv.org/abs/2502.17967)
[[PDF]](https://arxiv.org/pdf/2502.17967)

[![Python Version](https://img.shields.io/badge/Python-3.10-blue.svg)]()
[![GitHub license](https://img.shields.io/badge/MIT-blue)]()

![](images/Agent_Trading_Arena.png)

</div>

The Agent Trading Arena is a closed-loop, prior-free human-like trading environment designed to evaluate and advance self-play-capable financial agents.

# Preparation

## Python Install

```
git clone https://github.com/wekjsdvnm/Agent-Trading-Arena
cd Agent-Trading-Arena
pip install -r requirement.txt
```

## Set OpenRouter API Key:

Set your OpenRouter key as an environment variable (recommended):

```
export OPENROUTER_API_KEY="your_openrouter_api_key"
# optional overrides:
# export OPENROUTER_BASE_URL="https://openrouter.ai/api/v1"
# export OPENROUTER_MODEL="openai/gpt-5-mini"
```

The default model used by the code is `openai/gpt-5-mini` via OpenRouter. You can get a key from [OpenRouter](https://openrouter.ai/keys).

# Experiment

## Run the code

```
cd Agent-Trading-Arena
sh run.sh
```

# Citation

If you find our work useful, please consider citing us!

```
@misc{ma2025agenttradingarena,
      title={Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents}, 
      author={Tianmi Ma and Jiawei Du and Wenxin Huang and Wenjie Wang and Liang Xie and Xian Zhong and Joey Tianyi Zhou},
      year={2025},
      journal={arXiv preprint arXiv: 2502.17967},
}
```
# GenAI-Agent-Trading-Arena
