# Kaggle-Competition Repository

Welcome to the Kaggle-Competition repository! This repository is dedicated to open-source solutions, code, and resources for various Kaggle competitions. The goal is to provide a centralized location for collaboration, learning, and sharing insights related to Kaggle challenges.

## About Kaggle Competitions

[Kaggle](https://www.kaggle.com/) is a popular platform for data science competitions, machine learning challenges, and community-driven data projects. Competitions cover a wide range of topics, from image classification to natural language processing and more. This repository aims to bring together solutions and ideas from different competitions.

## Repository Structure

The repository is organized by competition name, with each competition having its own dedicated directory. This structure allows for clear separation of code, notebooks, and resources specific to each competition.

### How to Use

1. Clone the repository to your local machine:
   ```bash
   git clone git@github.com:adityajideveloper/kaggle-competition.git
   ```

2. Creating Python Virtual Envirnoment:
   ```bash
   python3 -m venv .venv
   ```

3. Starting Virtual Envirnoment:
   ```bash
   source .venv/bin/activate
   ```

3. Installing required packages:
    ```bash
    pip3 install -r requirements.txt
    ```

4. Installing PyTorch: <br/>
    Please refer to [PyTorch](https://pytorch.org/get-started/locally/) before installing as per your system requirements.

    ```bash
    pip3 install torch torchvision torchaudio
    ```

    With `CUDA 11.7 on winows`:

    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
    ```

    With `CUDA 11.7 on Linux`:

    ```bash
    pip3 install torch torchvision torchaudio
    ```

    With `ROCm 5.4.2 on Linux`:

    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2
    ```

    *There are more installation methods, please refer to [PyTorch Getting Started Page](https://pytorch.org/get-started/locally/).*

5. Explore the competition-specific directories, notebooks, and code samples.

### Contribution Guidelines

Contributions to this repository are welcome! If you've participated in a Kaggle competition and would like to share your solution or insights, follow these steps:

1. Fork the repository.

2. Create a new branch for your competition:
   ```
   git checkout -b competition-<competition-name>-contribution
   ```

3. Add your code, notebooks, and resources to the competition's directory.

4. Commit your changes with a descriptive message:
   ```
   git commit -m "Added solution for <competition-name>"
   ```

5. Push your changes to your forked repository:
   ```
   git push origin competition-<competition-name>-contribution
   ```

6. Create a pull request to the main repository.

Please ensure that your contributions follow best practices, are well-documented, and adhere to the competition rules and guidelines.

## Contact

Feel free to reach out to me if you have any questions, suggestions, or feedback related to this repository. You can also connect with me on [Twitter](https://twitter.com/adityakumar0912).