# Fine-Tuning

Adapting pre-trained LLMs to specific tasks or domains.

## Contents

- **full-finetuning/** - Training all model parameters
- **peft-lora/** - Parameter-Efficient Fine-Tuning with LoRA
- **instruction-tuning/** - Training models to follow instructions
- **evaluation/** - Evaluating fine-tuned models

## Why Fine-Tune?

- Adapt to specific domain
- Improve performance on task
- Customize model behavior
- Reduce prompt engineering needs

## Full Fine-Tuning

- Update all model parameters
- Requires significant compute
- Best performance
- Risk of catastrophic forgetting

## PEFT/LoRA

- Parameter-Efficient Fine-Tuning
- Low-Rank Adaptation (LoRA)
- Train only small adapter layers
- Much more efficient
- Nearly as effective

## Instruction Tuning

- Train models to follow instructions
- Improves zero-shot performance
- Better at following prompts
- Foundation for ChatGPT-like models

## When to Fine-Tune

- Domain-specific applications
- Need for consistent formatting
- Specialized vocabulary
- Performance requirements

## Evaluation

- Task-specific metrics
- Compare to baseline
- Test generalization
- Monitor for overfitting
