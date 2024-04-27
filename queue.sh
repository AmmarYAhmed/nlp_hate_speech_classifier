#!/bin/bash
# The interpreter used to execute the script

#“#SBATCH” directives that convey submission options:

#SBATCH --job-name=gpt2_accuracy
#SBATCH --account=eecs595w24_class
#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --time=04:00:00
#SBATCH --mem-per-cpu=32G
#SBATCH --mail-type=BEGIN,END
#SBATCH --output=gpt2_accuracy.out

# The application(s) to execute along with its input arguments and options:

/bin/hostname
echo “hello world”
nvidia-smi
export HF_TOKEN='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'
export WANDB_API_KEY="84e73c2c5a4f8521a171a30a325ef52061276a77"
python3 train_script.py


# pip install huggingface_hub
# python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"
